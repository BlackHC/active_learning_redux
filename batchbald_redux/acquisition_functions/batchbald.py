from dataclasses import dataclass

import torch
from blackhc.progress_bar import with_progress_bar

from batchbald_redux import joint_entropy
from batchbald_redux.acquisition_functions import PoolScorerCandidateBatchComputer, CandidateBatch
from batchbald_redux.batchbald import compute_conditional_entropy


class BatchBALDScorer:
    log_probs_N_K_C: torch.tensor
    conditional_entropies_N: torch.Tensor
    batch_joint_entropy: joint_entropy.JointEntropy
    batch_conditional_entropies: torch.Tensor

    def __init__(self, log_probs_N_K_C, *, max_size, num_samples: int, dtype=None, device=None):
        N, K, C = log_probs_N_K_C.shape
        self.log_probs_N_K_C = log_probs_N_K_C

        self.conditional_entropies_N = compute_conditional_entropy(self.log_probs_N_K_C)
        self.batch_conditional_entropies = 0

        self.batch_joint_entropy = joint_entropy.DynamicJointEntropy(
            num_samples, max_size, K, C, dtype=dtype, device=device
        )

    def append_to_batch(self, index: int):
        self.batch_joint_entropy.add_variables(self.log_probs_N_K_C[index : index + 1])
        self.batch_conditional_entropies += self.conditional_entropies_N[index].clone()

    def alloc_scores(self) -> torch.Tensor:
        # We always keep these on the CPU.
        scores_N = torch.empty(
            self.log_probs_N_K_C.shape[0],
            dtype=torch.double,
            pin_memory=torch.cuda.is_available(),
        )
        return scores_N

    def compute_scores(self, out_scores_N: torch.Tensor):
        self.batch_joint_entropy.compute_batch(self.log_probs_N_K_C, output_entropies_B=out_scores_N)

        out_scores_N -= self.conditional_entropies_N + self.batch_conditional_entropies

        return out_scores_N


def get_batch_bald_batch(
    log_probs_N_K_C: torch.Tensor, *, batch_size: int, num_samples: int, dtype=None, device=None
) -> CandidateBatch:
    N, K, C = log_probs_N_K_C.shape

    batch_size = min(batch_size, N)

    candidate_indices = []
    candidate_scores = []

    if batch_size == 0:
        return CandidateBatch(candidate_scores, candidate_indices)

    batchbald_scorer = BatchBALDScorer(
        log_probs_N_K_C,
        max_size=batch_size - 1,
        num_samples=num_samples,
        dtype=dtype,
        device=device,
    )

    # We always keep these on the CPU.
    scores_N = batchbald_scorer.alloc_scores()

    for i in with_progress_bar(range(batch_size), tqdm_args=dict(desc="BatchBALD", leave=False)):
        if i > 0:
            latest_index = candidate_indices[-1]
            batchbald_scorer.append_to_batch(latest_index)

        batchbald_scorer.compute_scores(scores_N)
        scores_N[candidate_indices] = -float("inf")

        candidate_score, candidate_index = scores_N.max(dim=0)

        candidate_indices.append(candidate_index.item())
        candidate_scores.append(candidate_score.item())

    return CandidateBatch(candidate_scores, candidate_indices)


@dataclass
class BatchBALD(PoolScorerCandidateBatchComputer):
    num_samples: int = 1000000

    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        # Evaluate BALD scores
        candidate_batch = get_batch_bald_batch(
            log_probs_N_K_C,
            batch_size=self.acquisition_size,
            num_samples=self.num_samples,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch