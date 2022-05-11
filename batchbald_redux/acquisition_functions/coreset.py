from dataclasses import dataclass

import numpy as np
import torch
from blackhc.progress_bar import with_progress_bar

from batchbald_redux import joint_entropy
from batchbald_redux.acquisition_functions import CoreSetPoolScorerCandidateBatchComputer, \
    CoreSetEvaluationPoolScorerCandidateBatchComputer, CandidateBatch
from batchbald_redux.acquisition_functions.stochastic_acquisition import get_top_k_scorers, get_sampled_tempered_scorers


def get_coreset_bald_scores_from_predictions(
    log_probs_N_K_C: torch.Tensor, target_probs_N_C: torch.Tensor, *, dtype=None, device=None
) -> torch.Tensor:
    N, K, C = log_probs_N_K_C.shape
    assert target_probs_N_C.shape == (N, C)

    log_probs_N_K_C = log_probs_N_K_C.to(dtype=dtype, device=device)
    target_probs_N_C = target_probs_N_C.to(dtype=dtype, device=device)

    log_prob_mean_N_C = torch.logsumexp(log_probs_N_K_C, dim=1) - np.log(K)

    entropy_N_C = -log_prob_mean_N_C
    conditional_entropy = -torch.mean(log_probs_N_K_C * log_probs_N_K_C.exp(), dim=1) / log_prob_mean_N_C.exp()
    mutual_bits_N_C = entropy_N_C - conditional_entropy

    cross_mutual_information = torch.sum(target_probs_N_C * mutual_bits_N_C, dim=1)

    return cross_mutual_information


def get_coreset_bald_scores(
    log_probs_N_K_C: torch.Tensor, labels_N: torch.Tensor, *, dtype=None, device=None
) -> torch.Tensor:
    N, K, C = log_probs_N_K_C.shape

    labels_N_1_1 = labels_N[:, None, None]
    log_probs_N_K = (
        joint_entropy.gather_expand(log_probs_N_K_C, dim=2, index=labels_N_1_1)
            .squeeze(2)
            .to(dtype=dtype, device=device)
    )

    log_prob_mean_N = torch.logsumexp(log_probs_N_K, dim=1) - np.log(K)

    lhs = -log_prob_mean_N
    rhs = -torch.mean(log_probs_N_K * log_probs_N_K.exp(), dim=1) / log_prob_mean_N.exp()

    coreset_infogain = lhs - rhs

    return coreset_infogain


def get_batch_coreset_bald_batch(
    log_probs_N_K_C: torch.Tensor, labels_N: torch.Tensor, *, batch_size: int, dtype=None, device=None
) -> CandidateBatch:
    # We want to compute (note this does not follow the notation from below):
    # CoreSetBALD = H[y_1, ..., y_n ] - E_p(w) p(y_1, ..., y_n | w) / p(y_1, ..., y_n) H[y_1, ..., y_n | w]
    # H[y_1, ..., y_n | w] = H[y_1, ..., y_{n-1} | w] + H[y_n | w] because y_i _||_ y_j | w
    N, K, C = log_probs_N_K_C.shape

    batch_size = min(batch_size, N)

    candidate_indices = []
    candidate_scores = []

    if batch_size == 0:
        return CandidateBatch(candidate_scores, candidate_indices)

    labels_N_1_1 = labels_N[:, None, None]
    log_probs_N_K = (
        joint_entropy.gather_expand(log_probs_N_K_C, dim=2, index=labels_N_1_1)
            .squeeze(2)
            .to(dtype=dtype, device=device)
    )

    # p((y)_{B-1}|(x)_{B-1}, \omega)
    log_probs_conditional_joint_batch_K = torch.zeros_like(log_probs_N_K[0], dtype=dtype, device=device)

    for i in with_progress_bar(range(batch_size), tqdm_args=dict(desc="BatchCoreSetBALD", leave=False)):
        # p((y)_B|(x)_B, \omega) = p(y_B|x_B, \omega) * p((y)_{B-1}|(x)_{B-1}, \omega)
        log_prob_conditional_joint_N_K = log_probs_N_K + log_probs_conditional_joint_batch_K[None, :]

        # Marginalize over w (but using sum not mean):
        # p((y)_B|(x)_B) = E_p(\omega) p((y)_B|(x)_B, \omega)
        # log_prob_joint_N_1 = log_prob_conditional_joint_N_K.logsumexp(dim=1, keepdim=True) - np.log(K)
        log_prob_joint_pK_N_1 = log_prob_conditional_joint_N_K.logsumexp(dim=1, keepdim=True)
        # \frac{ p((y)_B| (x)_B, \omega) }{ p((y)_B| (x)_B) }
        # log_ratio_N_K = log_prob_conditional_joint_N_K - log_prob_joint_N_1
        # log_ratio_N_K = log_prob_conditional_joint_N_K - log_prob_joint_pK_N_1 + np.log(K)
        log_ratio_mK_N_K = log_prob_conditional_joint_N_K - log_prob_joint_pK_N_1
        # conditional_entropy_joint_N = -torch.mean(log_ratio_N_K.exp() * log_prob_conditional_joint_N_K, dim=1)
        # conditional_entropy_joint_N =
        #       -torch.mean((log_ratio_mK_N_K + np.log(K)).exp() * log_prob_conditional_joint_N_K, dim=1)
        conditional_entropy_joint_N = -torch.sum(log_ratio_mK_N_K.exp() * log_prob_conditional_joint_N_K, dim=1)
        # entropy_joint_N = -log_prob_joint_N_1.squeeze(1)
        # entropy_joint_N = -(log_prob_joint_pK_N_1 - np.log(K)).squeeze(1)
        entropy_joint_N = -log_prob_joint_pK_N_1.squeeze(1) + np.log(K)
        scores_N = entropy_joint_N - conditional_entropy_joint_N

        # Select candidate
        scores_N[candidate_indices] = -float("inf")

        candidate_score, candidate_index = scores_N.max(dim=0)

        candidate_indices.append(candidate_index.item())
        candidate_scores.append(candidate_score.item())

        # Update log_probs_conditional_joint_batch_K
        log_probs_conditional_joint_batch_K = log_prob_conditional_joint_N_K[candidate_index]

    return CandidateBatch(candidate_scores, candidate_indices)


def get_coreset_eig_scores(
    *,
    training_log_probs_N_K_C: torch.Tensor,
    eval_log_probs_N_K_C: torch.Tensor,
    labels_N: torch.Tensor,
    dtype=None,
    device=None
) -> torch.Tensor:
    # We want to compute I[y_eval; y_batch].
    # I[y_eval; y_train] = H[y_batch] - H[y_batch|y_eval]
    N, K, C = training_log_probs_N_K_C.shape

    labels_N_1_1 = labels_N[:, None, None]
    training_log_probs_N_K = (
        joint_entropy.gather_expand(training_log_probs_N_K_C, dim=2, index=labels_N_1_1)
            .squeeze(2)
            .to(dtype=dtype, device=device)
    )
    training_log_prob_mean_N = torch.logsumexp(training_log_probs_N_K, dim=1) - np.log(K)

    eval_log_probs_N_K = (
        joint_entropy.gather_expand(eval_log_probs_N_K_C, dim=2, index=labels_N_1_1)
            .squeeze(2)
            .to(dtype=dtype, device=device)
    )
    eval_log_prob_mean_N = torch.logsumexp(eval_log_probs_N_K, dim=1) - np.log(K)

    pig = -training_log_prob_mean_N + eval_log_prob_mean_N

    return pig


def get_coreset_eig_bald_scores(
    *,
    training_log_probs_N_K_C: torch.Tensor,
    eval_log_probs_N_K_C: torch.Tensor,
    labels_N: torch.Tensor,
    dtype=None,
    device=None
) -> torch.Tensor:
    # We want to compute I[y_eval; y_batch; W].
    # I[y_eval; y_batch; W] = I[y_batch; W] - I[y_batch; W|y_eval]
    training_coreset = get_coreset_bald_scores(training_log_probs_N_K_C, labels_N=labels_N, dtype=dtype, device=device)
    eval_coreset = get_coreset_bald_scores(eval_log_probs_N_K_C, labels_N=labels_N, dtype=dtype, device=device)
    return training_coreset - eval_coreset


@dataclass
class _CoreSetBALD(CoreSetPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        if len(labels_N.shape) == 1:
            scores_N = get_coreset_bald_scores(log_probs_N_K_C, labels_N, dtype=torch.double, device=device)
        else:
            scores_N = get_coreset_bald_scores_from_predictions(
                log_probs_N_K_C, labels_N, dtype=torch.double, device=device
            )

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class CoreSetBALD(_CoreSetBALD):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class TemperedCoreSetBALD(_CoreSetBALD):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)


@dataclass
class BatchCoreSetBALD(CoreSetPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        candidate_batch = get_batch_coreset_bald_batch(
            log_probs_N_K_C,
            labels_N,
            batch_size=self.acquisition_size,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch


@dataclass
class _CoreSetPIGBALD(CoreSetEvaluationPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, training_log_probs_N_K_C, eval_log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        scores_N = get_coreset_eig_bald_scores(
            training_log_probs_N_K_C=training_log_probs_N_K_C,
            eval_log_probs_N_K_C=eval_log_probs_N_K_C,
            labels_N=labels_N,
            dtype=torch.double,
            device=device,
        )
        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class CoreSetPIGBALD(_CoreSetPIGBALD):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class TemperedCoreSetPIGBALD(_CoreSetPIGBALD):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)


@dataclass
class _CoreSetPIG(CoreSetEvaluationPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, training_log_probs_N_K_C, eval_log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        scores_N = get_coreset_eig_scores(
            training_log_probs_N_K_C=training_log_probs_N_K_C,
            eval_log_probs_N_K_C=eval_log_probs_N_K_C,
            labels_N=labels_N,
            dtype=torch.double,
            device=device,
        )
        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class CoreSetPIG(_CoreSetPIG):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class TemperedCoreSetPIG(_CoreSetPIG):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)
