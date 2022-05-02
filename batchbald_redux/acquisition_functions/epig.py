from dataclasses import dataclass
from enum import Enum

import torch
import torch.utils
from blackhc.progress_bar import with_progress_bar, create_progress_bar
from toma import toma

from batchbald_redux import joint_entropy
from batchbald_redux.acquisition_functions import EvaluationPoolScorerCandidateBatchComputer, EvalDatasetBatchComputer, \
    CandidateBatch, get_top_random_scorers
from batchbald_redux.acquisition_functions.bald import get_bald_scores
from batchbald_redux.acquisition_functions.batchbald import BatchBALDScorer
from batchbald_redux.batchbald import compute_entropy
from batchbald_redux.acquisition_functions.stochastic_acquisition import get_top_k_scorers, get_sampled_tempered_scorers
from batchbald_redux.trained_model import TrainedModel


def get_joint_probs_N_C_C(pool_probs_N_K_C: torch.Tensor, single_eval_probs_K_C: torch.Tensor):
    K = single_eval_probs_K_C.shape[0]

    pool_log_probs_N_C_K = pool_probs_N_K_C.transpose(1, 2).contiguous()
    joint_probs_N_C_C = pool_log_probs_N_C_K @ single_eval_probs_K_C / K
    return joint_probs_N_C_C


def get_joint_probs_N_C_EC_transposed(pool_probs_N_C_K: torch.Tensor, eval_probs_E_K_C: torch.Tensor):
    N, C, K = pool_probs_N_C_K.shape
    E, K, C = eval_probs_E_K_C.shape
    # joint_probs_N_C_C = torch.empty(N, C, C, dtype=pool_probs_N_C_K.dtype, device=pool_probs_N_C_K.device)
    # for joint_probs_C_C, pool_probs_C_K in zip(joint_probs_N_C_C.split(4096), pool_probs_N_C_K.split(4096)):
    #     joint_probs = pool_probs_C_K @ single_eval_probs_K_C / K
    #     joint_probs_C_C.copy_(joint_probs, non_blocking=True)
    eval_probs_K_EC = eval_probs_E_K_C.transpose(0, 1).reshape(K, E * C)
    # joint_probs_N_C_EC = pool_probs_N_C_K.contiguous() @ eval_probs_K_EC.contiguous() / K
    joint_probs_N_C_EC = pool_probs_N_C_K @ eval_probs_K_EC / K
    return joint_probs_N_C_EC


def get_joint_probs_N_C_C_transposed(pool_probs_N_C_K: torch.Tensor, single_eval_probs_K_C: torch.Tensor):
    K = single_eval_probs_K_C.shape[0]
    joint_probs_N_C_C = pool_probs_N_C_K @ single_eval_probs_K_C / K
    return joint_probs_N_C_C


def get_batch_eval_bald_batch(
    training_log_probs_N_K_C: torch.Tensor,
    eval_log_probs_N_K_C: torch.Tensor,
    *,
    batch_size: int,
    num_samples: int,
    dtype=None,
    device=None,
) -> CandidateBatch:
    assert training_log_probs_N_K_C.shape == eval_log_probs_N_K_C.shape
    N, K, C = training_log_probs_N_K_C.shape

    batch_size = min(batch_size, N)

    candidate_indices = []
    candidate_scores = []

    if batch_size == 0:
        return CandidateBatch(candidate_scores, candidate_indices)

    training_batchbald_scorer = BatchBALDScorer(
        training_log_probs_N_K_C,
        max_size=batch_size - 1,
        num_samples=num_samples,
        dtype=dtype,
        device=device,
    )

    pool_batchbald_scorer = BatchBALDScorer(
        eval_log_probs_N_K_C,
        max_size=batch_size - 1,
        num_samples=num_samples,
        dtype=dtype,
        device=device,
    )

    # We always keep these on the CPU.
    training_scores_N = training_batchbald_scorer.alloc_scores()
    pool_scores_N = pool_batchbald_scorer.alloc_scores()

    for i in with_progress_bar(range(batch_size), tqdm_args=dict(desc="BatchBALD", leave=False)):
        if i > 0:
            latest_index = candidate_indices[-1]
            training_batchbald_scorer.append_to_batch(latest_index)
            pool_batchbald_scorer.append_to_batch(latest_index)

        training_batchbald_scorer.compute_scores(training_scores_N)
        pool_batchbald_scorer.compute_scores(pool_scores_N)

        scores_N = training_scores_N - pool_scores_N
        scores_N[candidate_indices] = -float("inf")

        candidate_score, candidate_index = scores_N.max(dim=0)

        candidate_indices.append(candidate_index.item())
        candidate_scores.append(candidate_score.item())

    return CandidateBatch(candidate_scores, candidate_indices)


def get_eval_bald_scores(
    training_log_probs_N_K_C: torch.Tensor,
    eval_log_probs_N_K_C: torch.Tensor,
    *,
    dtype=None,
    device=None,
) -> torch.Tensor:
    assert training_log_probs_N_K_C.shape == eval_log_probs_N_K_C.shape

    training_scores_N = get_bald_scores(training_log_probs_N_K_C, dtype=dtype, device=device)
    pool_scores_N = get_bald_scores(eval_log_probs_N_K_C, dtype=dtype, device=device)

    scores_N = training_scores_N - pool_scores_N

    return scores_N


def get_eval_bald_batch(
    training_log_probs_N_K_C: torch.Tensor,
    pool_log_probs_N_K_C: torch.Tensor,
    *,
    batch_size: int,
    dtype=None,
    device=None,
) -> CandidateBatch:
    return get_top_k_scorers(
        get_eval_bald_scores(training_log_probs_N_K_C, pool_log_probs_N_K_C, dtype=dtype, device=device),
        batch_size=batch_size,
    )


def get_eig_scores(
    training_log_probs_N_K_C: torch.Tensor,
    pool_log_probs_N_K_C: torch.Tensor,
    *,
    dtype=None,
    device=None,
) -> torch.Tensor:
    assert training_log_probs_N_K_C.shape == pool_log_probs_N_K_C.shape

    N, K, C = training_log_probs_N_K_C.shape

    scores_N = compute_entropy(training_log_probs_N_K_C) - compute_entropy(pool_log_probs_N_K_C)

    return scores_N


# TODO: refactor the BatchBALDScorer to deduplicate some of this?
def get_batch_eig_batch(
    training_log_probs_N_K_C: torch.Tensor,
    pool_log_probs_N_K_C: torch.Tensor,
    *,
    batch_size: int,
    num_samples: int,
    dtype=None,
    device=None,
) -> CandidateBatch:
    assert training_log_probs_N_K_C.shape == pool_log_probs_N_K_C.shape
    N, K, C = training_log_probs_N_K_C.shape

    batch_size = min(batch_size, N)

    candidate_indices = []
    candidate_scores = []

    if batch_size == 0:
        return CandidateBatch(candidate_scores, candidate_indices)

    training_joint_entropy = joint_entropy.DynamicJointEntropy(
        num_samples, batch_size, K, C, dtype=dtype, device=device
    )

    pool_joint_entropy = joint_entropy.DynamicJointEntropy(num_samples, batch_size, K, C, dtype=dtype, device=device)

    # We always keep these on the CPU.
    training_scores_N = torch.empty(
        N,
        dtype=torch.double,
        pin_memory=torch.cuda.is_available(),
    )

    pool_scores_N = torch.empty(
        N,
        dtype=torch.double,
        pin_memory=torch.cuda.is_available(),
    )

    for i in with_progress_bar(range(batch_size), tqdm_args=dict(desc="BatchBALD", leave=False)):
        if i > 0:
            latest_index = candidate_indices[-1]
            training_joint_entropy.add_variables(training_log_probs_N_K_C[latest_index: latest_index + 1])
            pool_joint_entropy.add_variables(pool_log_probs_N_K_C[latest_index: latest_index + 1])

        training_joint_entropy.compute_batch(training_log_probs_N_K_C, output_entropies_B=training_scores_N)
        pool_joint_entropy.compute_batch(pool_log_probs_N_K_C, output_entropies_B=pool_scores_N)

        scores_N = training_scores_N - pool_scores_N
        scores_N[candidate_indices] = -float("inf")

        candidate_score, candidate_index = scores_N.max(dim=0)

        candidate_indices.append(candidate_index.item())
        candidate_scores.append(candidate_score.item())

    return CandidateBatch(candidate_scores, candidate_indices)


class BootstrapType(Enum):
    NO_BOOTSTRAP = 0
    SINGLE_BOOTSTRAP = 1
    PER_POINT_BOOTSTRAP = 2
    FAST_PER_POINT_BOOTSTRAP = 3


@torch.no_grad()
def get_real_naive_epig_scores(
    *,
    bootstrap_type=BootstrapType.NO_BOOTSTRAP,
    bootstrap_factor=1.0,
    pool_log_probs_N_K_C: torch.Tensor,
    eval_log_probs_E_K_C: torch.Tensor,
    dtype=None,
    device=None,
) -> torch.Tensor:
    """Implements naive EPIG: I[Y_acq; Y_eval | x_acq, X_eval]."""
    # I[Y_acq; Y_eval | x_acq, X_eval] = H[Y_acq | x_acq] + E_p(x_eval)[H[Y_eval | x_eval] - H[Y_acq, Y_eval | x_acq,
    # x_eval]]
    N, K, C = pool_log_probs_N_K_C.shape
    E, _, _ = eval_log_probs_E_K_C.shape
    assert (
        pool_log_probs_N_K_C.shape[1:] == pool_log_probs_N_K_C.shape[1:]
    ), "{pool_log_probs_N_K_C.shape[1:]} != {pool_log_probs_N_K_C.shape[1:]}"

    pool_entropies_N = compute_entropy(pool_log_probs_N_K_C).to(device=device, non_blocking=True)

    total_joint_entropies_N = torch.zeros((N,), dtype=dtype, device=device)

    if bootstrap_type != BootstrapType.PER_POINT_BOOTSTRAP:
        pool_probs_N_C_K = (
            pool_log_probs_N_K_C.to(dtype=dtype, device=device, non_blocking=True).exp().transpose(1, 2).contiguous()
        )
        # eval_probs_E_K_C = eval_log_probs_E_K_C.to(device=device, non_blocking=True).exp()

        eval_label_uncertainty = compute_entropy(eval_log_probs_E_K_C).mean(dim=0, keepdim=False)

        if bootstrap_type == BootstrapType.NO_BOOTSTRAP:
            num_eval_samples = E
            eval_range = list(range(E))
        elif bootstrap_type == BootstrapType.SINGLE_BOOTSTRAP:
            num_eval_samples = int(E * bootstrap_factor)
            eval_range = torch.multinomial(torch.tensor(1.0).expand(E), num_samples=num_eval_samples, replacement=True)
        else:
            raise ValueError(f"Unknown bootstrap {bootstrap_type}")

        pbar = create_progress_bar(num_eval_samples, tqdm_args=dict(desc="Evaluation Set", leave=False))
        pbar.start()

        @toma.execute.batch(1024)
        def loop(batchsize: int):
            pbar.reset()

            nonlocal total_joint_entropies_N
            for chunked_eval_log_probs_e_K_C in eval_log_probs_E_K_C[eval_range].split(batchsize):
                chunked_eval_probs_e_K_C = chunked_eval_log_probs_e_K_C.to(
                    dtype=dtype, device=device, non_blocking=True
                ).exp()
                joint_probs_N_E_EC = get_joint_probs_N_C_EC_transposed(pool_probs_N_C_K, chunked_eval_probs_e_K_C)
                weighted_nats_N_C_EC = joint_probs_N_E_EC * -torch.log(joint_probs_N_E_EC)
                weighted_nats_N_C_EC[torch.isnan(weighted_nats_N_C_EC)] = 0.0
                joint_entropy_N = weighted_nats_N_C_EC.sum((1, 2), keepdim=False)
                del weighted_nats_N_C_EC

                total_joint_entropies_N += joint_entropy_N

                pbar.update(len(chunked_eval_probs_e_K_C))

        pbar.finish()

        total_scores_N = pool_entropies_N - total_joint_entropies_N / E + eval_label_uncertainty
    elif bootstrap_type == BootstrapType.PER_POINT_BOOTSTRAP:
        pool_probs_N_K_C = pool_log_probs_N_K_C.to(dtype=dtype, device=device).exp()
        eval_probs_E_C_K = eval_log_probs_E_K_C.to(dtype=dtype, device=device).exp().transpose(1, 2).contiguous()

        eval_label_uncertainty_E = compute_entropy(eval_log_probs_E_K_C)

        total_scores_N = pool_entropies_N

        for i_n in with_progress_bar(range(N), tqdm_args=dict(desc="Pool Set", leave=False)):
            single_pool_probs_K_C = pool_probs_N_K_C[i_n]

            num_eval_samples = int(E * bootstrap_factor)
            eval_indices = torch.multinomial(
                torch.tensor(1.0).expand(E), num_samples=num_eval_samples, replacement=True
            )
            # For debugging:
            # num_eval_samples = E
            # eval_indices = torch.tensor(list(range(E)))

            sampled_eval_probs_F_C_K = eval_probs_E_C_K[eval_indices]

            joint_probs_F_C_C = get_joint_probs_N_C_C_transposed(sampled_eval_probs_F_C_K, single_pool_probs_K_C)
            weighted_nats_F_C_C = joint_probs_F_C_C * -torch.log(joint_probs_F_C_C)
            weighted_nats_F_C_C[torch.isnan(weighted_nats_F_C_C)] = 0.0
            avg_joint_entropy = weighted_nats_F_C_C.sum() / num_eval_samples
            del weighted_nats_F_C_C

            eval_label_uncertainty = eval_label_uncertainty_E[eval_indices].mean(dim=0, keepdim=False)
            total_scores_N[i_n] += eval_label_uncertainty - avg_joint_entropy

    return total_scores_N.to(device="cpu", non_blocking=True)


@dataclass
class _EvalBALD(EvaluationPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        scores_N = get_eval_bald_scores(log_probs_N_K_C, log_eval_probs_N_K_C, dtype=torch.double, device=device)

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class EvalBALD(_EvalBALD):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class TemperedEvalBALD(_EvalBALD):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)


@dataclass
class _EPIG(EvalDatasetBatchComputer):
    num_pool_samples: int
    epig_bootstrap_type: BootstrapType
    epig_bootstrap_factor: float
    epig_dtype: torch.dtype

    def compute_candidate_batch(
        self,
        model: TrainedModel,
        eval_loader: torch.utils.data.DataLoader,
        pool_loader: torch.utils.data.DataLoader,
        device,
    ) -> CandidateBatch:
        log_probs_N_K_C = model.get_log_probs_N_K_C(pool_loader, self.num_pool_samples, device, "cpu")
        if pool_loader == eval_loader:
            log_eval_probs_N_K_C = log_probs_N_K_C
        else:
            log_eval_probs_N_K_C = model.get_log_probs_N_K_C(eval_loader, self.num_pool_samples, device, "cpu")

        # NOTE: we are using floats all the way here. Hopefully this won't be two bad in the two variable case.
        # torch.double vs torch.float is a 10x speed difference (enough to make double infeasible for exps).
        scores_N = get_real_naive_epig_scores(
            bootstrap_type=self.epig_bootstrap_type,
            bootstrap_factor=self.epig_bootstrap_factor,
            pool_log_probs_N_K_C=log_probs_N_K_C,
            eval_log_probs_E_K_C=log_eval_probs_N_K_C,
            dtype=self.epig_dtype,
            device=device,
        )

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class EPIG(_EPIG):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class SoftmaxEPIG(_EPIG):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)


@dataclass
class BatchEvalBALD(EvaluationPoolScorerCandidateBatchComputer):
    num_samples: int = 1000000

    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        candidate_batch = get_batch_eval_bald_batch(
            log_probs_N_K_C,
            log_eval_probs_N_K_C,
            batch_size=self.acquisition_size,
            num_samples=self.num_samples,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch


@dataclass
class _EIG(EvaluationPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        scores_N = get_eig_scores(log_probs_N_K_C, log_eval_probs_N_K_C, dtype=torch.double, device=device)

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class EIG(_EIG):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class BatchEIG(EvaluationPoolScorerCandidateBatchComputer):
    num_samples: int = 1000000

    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        candidate_batch = get_batch_eig_batch(
            log_probs_N_K_C,
            log_eval_probs_N_K_C,
            batch_size=self.acquisition_size,
            num_samples=self.num_samples,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch


@dataclass
class TemperedEIG(_EIG):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)


def get_top_random_eval_bald_batch(
    training_log_probs_N_K_C: torch.Tensor,
    pool_log_probs_N_K_C: torch.Tensor,
    *,
    batch_size: int,
    num_classes: int,
    dtype=None,
    device=None,
) -> CandidateBatch:
    return get_top_random_scorers(
        get_eval_bald_scores(training_log_probs_N_K_C, pool_log_probs_N_K_C, dtype=dtype, device=device),
        batch_size=batch_size,
        num_classes=num_classes,
    )