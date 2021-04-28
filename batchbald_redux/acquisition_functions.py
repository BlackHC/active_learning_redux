# AUTOGENERATED! DO NOT EDIT! File to edit: 09a_acquisition_functions.ipynb (unless otherwise specified).

__all__ = ['PoolPredictions', 'CoreSetPoolPredictions', 'CandidateBatchComputer', 'Random',
           'PoolScorerCandidateBatchComputer', 'BALD', 'TemperedBALD', 'RandomBALD', 'ThompsonBALD', 'BatchBALD',
           'CoreSetPoolScorerCandidateBatchComputer', 'CoreSetBALD', 'TemperedCoreSetBALD', 'BatchCoreSetBALD',
           'EvalCandidateBatchComputer', 'EvaluationPoolScorerCandidateBatchComputer', 'EvalBALD', 'TemperedEvalBALD',
           'BatchEvalBALD', 'EIG', 'TemperedEIG']

# Cell

from dataclasses import dataclass
from enum import Enum
from typing import Union

import numpy as np
import torch
import torch.utils.data

from .batchbald import (
    CandidateBatch,
    get_bald_ical_scores,
    get_bald_scores,
    get_batch_coreset_bald_batch,
    get_batchbald_batch,
    get_batchbaldical_batch,
    get_coreset_bald_scores,
    get_ical_scores,
    get_sampled_tempered_scorers,
    get_thompson_bald_batch,
    get_top_k_scorers,
    get_top_random_scorers,
)
from .black_box_model_training import (
    get_predictions,
    get_predictions_labels,
)

# Cell


@dataclass
class PoolPredictions:
    num_pool_samples: int = 20

    def get_log_probs_N_K_C(self, model, pool_loader, device) -> torch.Tensor:
        log_probs_N_K_C = get_predictions(
            model=model,
            num_samples=self.num_pool_samples,
            # TODO!!!
            num_classes=10,
            loader=pool_loader,
            device=device,
        )
        return log_probs_N_K_C


@dataclass
class CoreSetPoolPredictions:
    num_pool_samples: int = 20

    def get_log_probs_N_K_C_labels_N(self, model, pool_loader, device) -> (torch.Tensor, torch.Tensor):
        log_probs_N_K_C, labels_N = get_predictions_labels(
            model=model,
            num_samples=self.num_pool_samples,
            # TODO!!!
            num_classes=10,
            loader=pool_loader,
            device=device,
        )
        return log_probs_N_K_C, labels_N

# Cell


@dataclass
class CandidateBatchComputer:
    acquisition_size: int

    def compute_candidate_batch(self, model, pool_loader, device) -> CandidateBatch:
        pass

# Cell


@dataclass
class Random(CandidateBatchComputer):
    def compute_candidate_batch(self, model, pool_loader: torch.utils.data.DataLoader, device) -> CandidateBatch:
        num_pool_samples = len(pool_loader.dataset)
        indices = np.random.choice(num_pool_samples, size=self.acquisition_size, replace=False)
        candidate_batch = CandidateBatch([0.0] * self.acquisition_size, indices)
        return candidate_batch

# Cell


@dataclass
class PoolScorerCandidateBatchComputer(CandidateBatchComputer):
    pool_scorer: PoolPredictions

    def compute_candidate_batch(self, model, pool_loader, device) -> CandidateBatch:
        log_probs_N_K_C = self.pool_scorer.get_log_probs_N_K_C(model, pool_loader, device)

        return self.get_candidate_batch(log_probs_N_K_C, device)

    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        raise NotImplementedError()

# Cell


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

# Cell


@dataclass
class BatchBALD(PoolScorerCandidateBatchComputer):
    num_samples: int = 1000000

    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        # Evaluate BALD scores
        candidate_batch = get_batchbald_batch(
            log_probs_N_K_C,
            batch_size=self.acquisition_size,
            num_samples=self.num_samples,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch

# Cell


@dataclass
class CoreSetPoolScorerCandidateBatchComputer(CandidateBatchComputer):
    core_set_pool_scorer: CoreSetPoolPredictions

    def compute_candidate_batch(self, model, pool_loader, device) -> CandidateBatch:
        log_probs_N_K_C, labels_N = self.core_set_pool_scorer.get_log_probs_N_K_C_labels_N(model, pool_loader, device)

        return self.get_candidate_batch(log_probs_N_K_C, labels_N, device)

    def get_candidate_batch(self, log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        raise NotImplementedError()

# Cell


@dataclass
class _CoreSetBALD(CoreSetPoolScorerCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        scores_N = get_coreset_bald_scores(log_probs_N_K_C, labels_N, dtype=torch.double, device=device)

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

# Cell


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

# Cell


@dataclass
class EvalCandidateBatchComputer:
    acquisition_size: int

    def compute_candidate_batch(self, model, eval_model, pool_loader, device) -> CandidateBatch:
        pass

# Cell


@dataclass
class EvaluationPoolScorerCandidateBatchComputer(EvalCandidateBatchComputer):
    pool_scorer: PoolPredictions

    def compute_candidate_batch(self, model, eval_model, pool_loader, device) -> CandidateBatch:
        log_probs_N_K_C = self.pool_scorer.get_log_probs_N_K_C(model, pool_loader, device)
        log_eval_probs_N_K_C = self.pool_scorer.get_log_probs_N_K_C(eval_model, pool_loader, device)

        return self.get_candidate_batch(log_probs_N_K_C, log_eval_probs_N_K_C, device)

    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        raise NotImplementedError()

# Cell


@dataclass
class _EvalBALD(EvalCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        scores_N = get_bald_ical_scores(log_probs_N_K_C, log_eval_probs_N_K_C, dtype=torch.double, device=device)

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

# Cell


@dataclass
class BatchEvalBALD(EvalCandidateBatchComputer):
    num_samples: int = 1000000

    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        candidate_batch = get_batchbaldical_batch(
            log_probs_N_K_C,
            log_eval_probs_N_K_C,
            batch_size=self.acquisition_size,
            num_samples=self.num_samples,
            dtype=torch.double,
            device=device,
        )
        return candidate_batch

# Cell


@dataclass
class _EIG(EvalCandidateBatchComputer):
    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        scores_N = get_ical_scores(log_probs_N_K_C, log_eval_probs_N_K_C, dtype=torch.double, device=device)

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class EIG(_EIG):
    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_top_k_scorers(scores_N, batch_size=self.acquisition_size)


@dataclass
class TemperedEIG(_EIG):
    temperature: float

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_sampled_tempered_scorers(scores_N, batch_size=self.acquisition_size, temperature=self.temperature)