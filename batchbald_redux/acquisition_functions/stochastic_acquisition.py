from enum import Enum

import numpy as np
import scipy.stats
import torch

from batchbald_redux.acquisition_functions import CandidateBatch


def get_top_k_scorers(scores_N: torch.Tensor, *, batch_size: int) -> CandidateBatch:
    N = len(scores_N)
    batch_size = min(batch_size, N)

    candidate_scores, candidate_indices = torch.topk(scores_N, batch_size)

    return CandidateBatch(candidate_scores.tolist(), candidate_indices.tolist())


def get_sampled_tempered_scorers(scores_N: torch.Tensor, *, temperature: float, batch_size: int) -> CandidateBatch:
    N = len(scores_N)
    batch_size = min(batch_size, N)

    # If we exponentiate scores_N beforehand, we obtain a softmax function here.
    tempered_scores_N = scores_N ** (1 / temperature)
    tempered_scores_N[scores_N < 0] = 0.0
    partition_constant = tempered_scores_N.sum()
    p = tempered_scores_N / partition_constant

    # TODO: change this to use PyTorch instead of numpy?
    candidate_indices = np.random.choice(N, size=batch_size, replace=False, p=p.cpu().numpy())
    candidate_scores = scores_N[candidate_indices]

    return CandidateBatch(candidate_scores.tolist(), candidate_indices.tolist())


def get_random_samples(scores_N: torch.Tensor, *, batch_size: int) -> CandidateBatch:
    N = len(scores_N)
    batch_size = min(batch_size, N)

    indices = np.random.choice(N, size=batch_size, replace=False)
    candidate_batch = CandidateBatch([0.0] * batch_size, indices.tolist())
    return candidate_batch


def get_softmax_samples(scores_N: torch.Tensor, *, coldness: float, batch_size: int) -> CandidateBatch:
    # As coldness -> 0, we obtain random sampling.
    if coldness == 0.0:
        return get_random_samples(scores_N, batch_size=batch_size)

    N = len(scores_N)
    noised_scores_N = scores_N + scipy.stats.gumbel_r.rvs(loc=0, scale=1 / coldness, size=N, random_state=None)

    return get_top_k_scorers(noised_scores_N, batch_size=batch_size)


def get_power_samples(scores_N: torch.Tensor, *, coldness: float, batch_size: int) -> CandidateBatch:
    return get_softmax_samples(torch.log(scores_N), coldness=coldness, batch_size=batch_size)


def get_softrank_samples(scores_N: torch.Tensor, *, coldness: float, batch_size: int) -> CandidateBatch:
    N = len(scores_N)

    sorted_indices_N = torch.argsort(scores_N, descending=True)
    ranks_N = torch.argsort(sorted_indices_N) + 1

    return get_power_samples(1 / ranks_N, coldness=coldness, batch_size=batch_size)


def get_simulation_samples(scores_N: torch.Tensor, *, coldness: float, batch_size: int) -> CandidateBatch:
    # As coldness -> 0, we obtain random sampling.
    if coldness == 0.0:
        return get_random_samples(scores_N, batch_size=batch_size)

    N = len(scores_N)
    batch_size = min(batch_size, N)

    indices = []
    scores = []
    current_scores_N = torch.clone(scores_N)
    for i in range(batch_size):
        score, index = torch.max(current_scores_N, dim=0)
        scores += [score.item()]
        indices += [index.item()]
        current_scores_N = current_scores_N / (1+ scipy.stats.expon.rvs(loc=0, scale=1 / coldness, size=N, random_state=None))
        current_scores_N[index] = float("-inf")

    return CandidateBatch(scores=scores, indices=indices)


class StochasticMode(Enum):
    Power = "Power"
    Softmax = "Softmax"
    Softrank = "Softrank"
    Simulation = "Simulation"
    TopK = "TopK"


def get_stochastic_samples(
    scores_N: torch.Tensor, *, coldness: float, batch_size: int, mode: StochasticMode
) -> CandidateBatch:
    if mode == StochasticMode.Power:
        return get_power_samples(scores_N, coldness=coldness, batch_size=batch_size)
    elif mode == StochasticMode.Softmax:
        return get_softmax_samples(scores_N, coldness=coldness, batch_size=batch_size)
    elif mode == StochasticMode.Softrank:
        return get_softrank_samples(scores_N, coldness=coldness, batch_size=batch_size)
    elif mode == StochasticMode.Simulation:
        return get_simulation_samples(scores_N, coldness=coldness, batch_size=batch_size)
    elif mode == StochasticMode.TopK:
        return get_top_k_scorers(scores_N, batch_size=batch_size)
    else:
        raise ValueError(f"Unknown mode")