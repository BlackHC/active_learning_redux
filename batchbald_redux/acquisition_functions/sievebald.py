from dataclasses import dataclass

import torch

from batchbald_redux import joint_entropy
from batchbald_redux.acquisition_functions import PoolScorerCandidateBatchComputer, CandidateBatch
from batchbald_redux.joint_entropy import compute_conditional_entropy, compute_entropy


def get_sieve_bald_batch(log_probs_N_K_C: torch.Tensor, *, batch_size: int, dtype=None, device=None) -> CandidateBatch:
    N, K, C = log_probs_N_K_C.shape
    batch_size = min(batch_size, N)

    candidate_scores = []
    candidate_indices = []

    entropies_N = compute_entropy(log_probs_N_K_C)

    # we start with BALD scores
    scores_N = entropies_N - compute_conditional_entropy(log_probs_N_K_C)

    last_score = 0.0
    for _ in range(batch_size):
        # Pick the highest scorer.
        # This is amenable to lazy greedy and lazier than lazy greedy, though we do not implement this here. (Yet)
        candidate_score, candidate_index = scores_N.max(dim=0)

        # TODO: break here if candidate_score < 0 at this point!

        candidate_score += last_score
        last_score = candidate_score

        candidate_indices.append(candidate_index.item())
        candidate_scores.append(candidate_score.item())

        # Update the acquired item's score so it is not picked again.
        scores_N[candidate_index] = -float("inf")

        # Decrease scores for other items
        joint_entropy_helper = joint_entropy.ExactJointEntropy.empty(K, device=device, dtype=dtype)
        joint_entropy_helper.add_variables(log_probs_N_K_C[candidate_index : candidate_index + 1])
        joint_entropies_N = joint_entropy_helper.compute_batch(log_probs_N_K_C)
        dual_mi_N = entropies_N + entropies_N[candidate_index] - joint_entropies_N

        scores_N -= dual_mi_N

    return CandidateBatch(candidate_scores, candidate_indices)


@dataclass
class SieveBALD(PoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        # Evaluate BALD scores
        candidate_batch = get_sieve_bald_batch(
            log_probs_N_K_C,
            batch_size=self.acquisition_size,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch