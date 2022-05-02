from dataclasses import dataclass
from typing import List

import numpy as np
import torch
import torch.utils.data

from ..trained_model import TrainedModel


@dataclass
class CandidateBatch:
    scores: List[float]
    indices: List[int]


@dataclass
class CandidateBatchComputer:
    acquisition_size: int

    def compute_candidate_batch(
        self, model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        pass


@dataclass
class Random(CandidateBatchComputer):
    def compute_candidate_batch(
        self, model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        num_pool_samples = len(pool_loader.dataset)
        indices = np.random.choice(num_pool_samples, size=self.acquisition_size, replace=False)
        candidate_batch = CandidateBatch([0.0] * self.acquisition_size, indices)
        return candidate_batch


@dataclass
class PoolScorerCandidateBatchComputer(CandidateBatchComputer):
    num_pool_samples: int

    def compute_candidate_batch(
        self, model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        log_probs_N_K_C = model.get_log_probs_N_K_C(pool_loader, self.num_pool_samples, device, "cpu")

        return self.get_candidate_batch(log_probs_N_K_C, device)

    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class CoreSetPoolScorerCandidateBatchComputer(CandidateBatchComputer):
    num_pool_samples: int

    def compute_candidate_batch(
        self, model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        log_probs_N_K_C, labels_N = model.get_log_probs_N_K_C_labels_N(
            pool_loader, self.num_pool_samples, device, "cpu"
        )

        return self.get_candidate_batch(log_probs_N_K_C, labels_N, device)

    def get_candidate_batch(self, log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class EvalDatasetBatchComputer:
    acquisition_size: int

    def compute_candidate_batch(
        self,
        model: TrainedModel,
        pool_loader: torch.utils.data.DataLoader,
        eval_loader: torch.utils.data.DataLoader,
        device,
    ) -> CandidateBatch:
        pass


@dataclass
class EvalModelBatchComputer:
    acquisition_size: int

    def compute_candidate_batch(
        self, model: TrainedModel, eval_model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        pass


@dataclass
class EvaluationPoolScorerCandidateBatchComputer(EvalModelBatchComputer):
    num_pool_samples: int

    def compute_candidate_batch(
        self, model: TrainedModel, eval_model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        log_probs_N_K_C = model.get_log_probs_N_K_C(pool_loader, self.num_pool_samples, device, "cpu")
        log_eval_probs_N_K_C = eval_model.get_log_probs_N_K_C(pool_loader, self.num_pool_samples, device, "cpu")

        return self.get_candidate_batch(log_probs_N_K_C, log_eval_probs_N_K_C, device)

    def get_candidate_batch(self, log_probs_N_K_C, log_eval_probs_N_K_C, device) -> CandidateBatch:
        raise NotImplementedError()


@dataclass
class CoreSetEvaluationPoolScorerCandidateBatchComputer(EvalModelBatchComputer):
    num_pool_samples: int

    def compute_candidate_batch(
        self, model: TrainedModel, eval_model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        training_log_probs_N_K_C, training_labels_N = model.get_log_probs_N_K_C_labels_N(
            pool_loader, self.num_pool_samples, device, "cpu"
        )
        eval_log_probs_N_K_C, eval_labels_N = eval_model.get_log_probs_N_K_C_labels_N(
            pool_loader, self.num_pool_samples, device, "cpu"
        )

        # With high probability, this ensures that we are not shuffling the batches.
        assert torch.equal(training_labels_N, eval_labels_N)

        return self.get_candidate_batch(training_log_probs_N_K_C, eval_log_probs_N_K_C, training_labels_N, device)

    def get_candidate_batch(self, training_log_probs_N_K_C, eval_log_probs_N_K_C, labels_N, device) -> CandidateBatch:
        raise NotImplementedError()
