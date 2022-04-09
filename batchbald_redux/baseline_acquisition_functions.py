import math
from dataclasses import dataclass

import torch.utils.data

from .batchbald import CandidateBatch, StochasticMode, get_stochastic_samples
from .trained_model import TrainedModel
from .acquisition_functions import CandidateBatchComputer, PoolScorerCandidateBatchComputer
from .consistent_mc_dropout import GradEmbeddingType

# copied from https://github.com/JordanAsh/badge/blob/master/query_strategies/badge_sampling.py
# by Jordan Ash
import torch
from scipy import stats
import numpy as np
from sklearn.metrics import pairwise_distances


# kmeans ++ initialization
def init_centers(X, K):
    ind = np.argmax([np.linalg.norm(s, 2) for s in X])
    mu = [X[ind]]
    indsAll = [ind]
    centInds = [0.] * len(X)
    cent = 0
    print('#Samps\tTotal Distance')
    while len(mu) < K:
        if len(mu) == 1:
            D2 = pairwise_distances(X, mu).ravel().astype(float)
        else:
            newD = pairwise_distances(X, [mu[-1]]).ravel().astype(float)
            for i in range(len(X)):
                if D2[i] > newD[i]:
                    centInds[i] = cent
                    D2[i] = newD[i]
        print(str(len(mu)) + '\t' + str(sum(D2)), flush=True)
        # if sum(D2) == 0.0:
        #    pdb.set_trace()
        D2 = D2.ravel().astype(float)
        Ddist = (D2 ** 2) / sum(D2 ** 2)
        customDist = stats.rv_discrete(name='custm', values=(np.arange(len(D2)), Ddist))
        ind = customDist.rvs(size=1)[0]
        while ind in indsAll: ind = customDist.rvs(size=1)[0]
        mu.append(X[ind])
        indsAll.append(ind)
        cent += 1
    return indsAll


@dataclass
class BADGE(CandidateBatchComputer):
    def compute_candidate_batch(
        self, model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
    ) -> CandidateBatch:
        grad_embeddings = model.get_grad_embeddings(pool_loader, num_samples=0, loss=torch.nn.functional.nll_loss,
                                                    model_labels=True, grad_embedding_type=GradEmbeddingType.LINEAR,
                                                    device=device, storage_device="cpu")
        chosen_indices = init_centers(grad_embeddings.squeeze(1).numpy(), self.acquisition_size)

        return CandidateBatch(indices=chosen_indices, scores=[0.0] * len(chosen_indices))


@dataclass
class StochasticScoringFunction(PoolScorerCandidateBatchComputer):
    coldness: float
    stochastic_mode: StochasticMode

    def get_candidate_batch(self, log_probs_N_K_C, device) -> CandidateBatch:
        # Ignore the device (because get_stochastic_samples needs a cpu device!)
        scores_N = self.compute_scores(log_probs_N_K_C, device="cpu")

        candidate_batch = self.extract_candidates(scores_N)

        return candidate_batch

    def extract_candidates(self, scores_N) -> CandidateBatch:
        return get_stochastic_samples(scores_N, batch_size=self.acquisition_size, coldness=self.coldness,
                                      mode=self.stochastic_mode)

    def compute_scores(self, log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
        raise NotImplementedError()


def get_variation_ratios(log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
    mean_probs_N_C = torch.mean(log_probs_N_K_C.to(device).exp(), dim=1)
    return 1. - torch.max(mean_probs_N_C, dim=1)[0]


@dataclass
class VariationRatios(StochasticScoringFunction):
    def compute_scores(self, log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
        return get_variation_ratios(log_probs_N_K_C=log_probs_N_K_C, device=device)


def get_margin_scores(log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
    mean_probs_N_C = torch.mean(log_probs_N_K_C.to(device).exp(), dim=1)
    top_2_probs_N_2 = torch.topk(mean_probs_N_C, k=2, dim=1, sorted=True)[0]
    margin_scores_N = top_2_probs_N_2[:, 0] - top_2_probs_N_2[:, 1]
    return 1. - margin_scores_N


@dataclass
class Margin(StochasticScoringFunction):
    def compute_scores(self, log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
        return get_margin_scores(log_probs_N_K_C=log_probs_N_K_C, device=device)


def get_stddev_scores(log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
    stddev_B_C = torch.std(log_probs_N_K_C.to(device).double().exp(), dim=1)
    return torch.sum(stddev_B_C, dim=1)


@dataclass
class StdDev(StochasticScoringFunction):
    def compute_scores(self, log_probs_N_K_C: torch.Tensor, *, device) -> torch.Tensor:
        return get_stddev_scores(log_probs_N_K_C=log_probs_N_K_C, device=device)


# class DistilBayesianModelAdapter(torch.nn.Module):
#     wrapped_model: BayesianModule
#     embedding_dims: int
#
#     def __init__(self, wrappped_model: BayesianModule, embedding_dims: int):
#         super().__init__()
#
#         self.embedding_dims = embedding_dims
#         self.wrappped_model: BayesianModule = wrappped_model
#
#     def get_embedding_dim(self):
#         return self.embedding_dims
#
#     def forward(self, x, last=False, freeze=False):
#         output_B_K_C = self.wrappped_model(x, num_samples=0, return_embedding=last, freeze_encoder=freeze)
#         return output_B_K_C.squeeze(1)
#
#
# @dataclass
# class DistilStrategyAdapter(CandidateBatchComputer):
#     distil_strategy: Type[Strategy]
#     distil_strategy_args: List[str]
#
#     def compute_candidate_batch(
#         self, model: TrainedModel, pool_loader: torch.utils.data.DataLoader, device
#     ) -> CandidateBatch:
#         assert isinstance(model, TrainedBayesianModel), "Only Bayesian models supported currently (not ensembles)!"
#
#         bayesian_model: BayesianModule = model.model
#
#         bayesian_model.to(device=device)
#
#         for batch_data, _ in pool_loader:
#             break
#         with torch.no_grad():
#             _, embedding = bayesian_model(batch_data.to(device=device), num_samples=0, return_embedding=True)
#         embedding_dims = embedding.shape[2]
#
#         model_adapter = DistilBayesianModelAdapter(bayesian_model, embedding_dims)
#
#         unlabeled_dataset = LabeledToUnlabeledDataset(pool_loader.dataset)
#         self.distil_strategy(None, None, unlabeled_x=)
