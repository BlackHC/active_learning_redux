from dataclasses import dataclass

import torch
from blackhc.progress_bar import create_progress_bar
from toma import toma

from batchbald_redux.acquisition_functions import PoolScorerCandidateBatchComputer, CandidateBatch
from batchbald_redux.batchbald import compute_conditional_entropy, compute_entropy
from batchbald_redux.acquisition_functions.stochastic_acquisition import get_top_k_scorers, \
    get_sampled_tempered_scorers, get_stochastic_samples, StochasticMode


def get_bald_batch(log_probs_N_K_C: torch.Tensor, *, batch_size: int, dtype=None, device=None) -> CandidateBatch:
    N, K, C = log_probs_N_K_C.shape

    scores_N = get_bald_scores(log_probs_N_K_C, dtype=dtype, device=device)

    return get_top_k_scorers(scores_N, batch_size=batch_size)


# TODO: remove unused parameters!
def get_bald_scores(log_probs_N_K_C: torch.Tensor, *, dtype=None, device=None) -> torch.Tensor:
    N, K, C = log_probs_N_K_C.shape

    scores_N = -compute_conditional_entropy(log_probs_N_K_C)
    scores_N += compute_entropy(log_probs_N_K_C)

    return scores_N


def compute_each_conditional_entropy(log_probs_N_K_C: torch.Tensor) -> torch.Tensor:
    N, K, C = log_probs_N_K_C.shape

    entropies_N_K = torch.empty((N, K), dtype=torch.double)

    pbar = create_progress_bar(N, tqdm_args=dict(desc="Entropy", leave=False))
    pbar.start()

    @toma.execute.chunked(log_probs_N_K_C, 1024)
    def compute(log_probs_n_K_C, start: int, end: int):
        nats_n_K_C = log_probs_n_K_C * torch.exp(log_probs_n_K_C)

        entropies_N_K[start:end].copy_(-torch.sum(nats_n_K_C, dim=2))
        pbar.update(end - start)

    pbar.finish()

    return entropies_N_K


def get_thompson_bald_batch(
    log_probs_N_K_C: torch.Tensor, *, batch_size: int, dtype=None, device=None
) -> CandidateBatch:
    N, K, C = log_probs_N_K_C.shape
    assert K >= batch_size

    batch_size = min(batch_size, N)

    entropy_N = compute_entropy(log_probs_N_K_C)
    all_conditional_entropies_N_K = compute_each_conditional_entropy(log_probs_N_K_C)

    thompson_bald_scores_N_K = entropy_N[:, None] - all_conditional_entropies_N_K

    candidate_scores, candidate_indices = [], []
    for b in range(batch_size):
        candidate_score, candidate_index = thompson_bald_scores_N_K[:, b].max(dim=0)

        candidate_scores.append(candidate_score.item())
        candidate_indices.append(candidate_index.item())

        thompson_bald_scores_N_K[candidate_index] = -float("inf")

    return CandidateBatch(candidate_scores, candidate_indices)


def get_top_random_scorers(scores_N: torch.Tensor, *, num_classes: int, batch_size: int) -> CandidateBatch:
    N = len(scores_N)
    batch_size = min(batch_size, N)

    L = min(batch_size * num_classes, N)

    candidate_scores, candidate_indices = torch.topk(scores_N, L)

    sub_indices = torch.randperm(L)[:batch_size]

    return CandidateBatch(candidate_scores[sub_indices].tolist(), candidate_indices[sub_indices].tolist())


def get_random_bald_batch(log_probs_N_K_C: torch.Tensor, *, batch_size: int, dtype=None, device=None) -> CandidateBatch:
    N, K, C = log_probs_N_K_C.shape

    scores_N = get_bald_scores(log_probs_N_K_C, dtype=dtype, device=device)

    return get_top_random_scorers(scores_N, num_classes=C, batch_size=batch_size)


@dataclass
class _BALD(PoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        # Evaluate BALD scores
        scores_N = get_bald_scores(log_probs_N_K_C, dtype=torch.double, device=device)

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class BALD(_BALD):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class TemperedBALD(_BALD):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)


@dataclass
class SoftmaxBALD(_BALD):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(
            scores_N.exp(), batch_size=self.acquisition_size, temperature=self.temperature
        )


@dataclass
class StochasticBALD(_BALD):
    coldness: float
    stochastic_mode: StochasticMode

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_stochastic_samples(scores_N, batch_size=self.acquisition_size, coldness=self.coldness, mode=self.stochastic_mode)


@dataclass
class RandomBALD(_BALD):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_random_scorers(scores_N, batch_size=self.acquisition_size, num_classes=10)


@dataclass
class ThompsonBALD(PoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        candidate_batch = get_thompson_bald_batch(
            log_probs_N_K_C,
            batch_size=self.acquisition_size,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch

