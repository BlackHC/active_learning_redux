from dataclasses import dataclass
from typing import List

import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.auto import tqdm

from batchbald_redux.dataset_challenges import AliasDataset
from batchbald_redux.consistent_mc_dropout import BayesianModule


@dataclass
class OBIPerformance:
    total_training_set_size: int
    real_training_set_size: int
    online_training_set_size: int
    trial_index: int
    num_samples: int
    accuracy: float
    crossentropy: float
    kl_best_marginal: float


def evaluate_online_bayesian_inference(model: BayesianModule, *, real_training_set_size: int,
                                       train_dataset: AliasDataset, test_dataset: AliasDataset,
                                       training_indices: List[int], start_index, num_samples_list: List[int],
                                       num_trials: int,
                                       up_factor: int, eval_batchsize: int, device) -> List[OBIPerformance]:
    log_probs_N_M_C, labels_N = get_obi_predictions_labels(model, test_dataset=test_dataset,
                                                           train_dataset=train_dataset,
                                                           training_indices=training_indices,
                                                           num_samples=num_samples_list[-1] * up_factor,
                                                           eval_batchsize=eval_batchsize,
                                                           device=device)

    num_training_indices = len(training_indices)
    obi_simple_results = eval_obi_simple(log_probs_N_M_C=log_probs_N_M_C, labels_N=labels_N,
                                         training_set_size=num_training_indices,
                                         start_index=start_index, end_index=num_training_indices,
                                         num_samples_list=num_samples_list,
                                         num_trials=num_trials,
                                         real_training_set_size=real_training_set_size)
    obi_upperbound_result = eval_best_topk_liklihood_ensemble(log_probs_N_M_C=log_probs_N_M_C,
                                                              labels_N=labels_N,
                                                              training_set_size=num_training_indices,
                                                              real_training_set_size=real_training_set_size,
                                                              k=10)
    return obi_simple_results, obi_upperbound_result


def get_obi_predictions_labels(model, *, test_dataset, train_dataset, training_indices, num_samples,
                               eval_batchsize, device):
    # TODO: rewrite this to use the newer TrainedModel interface!
    sub_train_set = train_dataset.subset(training_indices)
    joint_set = sub_train_set + test_dataset
    joint_loader = torch.utils.data.DataLoader(
        joint_set, batch_size=eval_batchsize, drop_last=False, shuffle=False
    )
    log_probs_N_M_C, labels_N = model.get_predictions_labels(num_samples=num_samples, loader=joint_loader,
                                                             device=device,
                                                             storage_device="cpu")
    return log_probs_N_M_C, labels_N


# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np


def sum_log_probs(log_probs, dim: int):
    # NOTE: assumes that the probs \in (0,1], ie. log_probs \in (-infty, 0]
    sorted_log_probs = torch.sort(log_probs, dim=dim, descending=False).values
    summed_log_probs = torch.sum(sorted_log_probs, dim=dim)
    return summed_log_probs


def eval_validation_convex_optimization(*, log_probs_N_M_C, labels_N, training_set_size, num_samples_list, num_trials,
                                        real_training_set_size, start_index=None, end_index_start=None,
                                        end_index_end=None,
                                        verbose=True):
    start_index = start_index if start_index is not None else 0
    end_index_start = end_index_start if end_index_start is not None else start_index
    end_index_end = end_index_end if end_index_end is not None else training_set_size

    N, M, C = log_probs_N_M_C.shape

    results = []
    # Compute the weights incl the initial training set.
    for trial in tqdm(range(num_trials)):
        for end_index in range(end_index_start, end_index_end + 1):
            online_training_set_size = end_index - start_index
            for num_samples in num_samples_list:
                if verbose:
                    print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(M, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :]

                validation_log_probs_n_m_C = trial_log_probs_N_m_C[start_index:end_index]

                weights_m = torch.nn.Parameter(data=torch.ones(num_samples))
                #optimizer = torch.optim.LBFGS([weights_m], lr=0.05)
                optimizer = torch.optim.AdamW([weights_m], lr=1)
                pbar = tqdm(range(200))
                patience = 15
                best_i = 0
                best_weights = None
                best_objective = float("inf")
                for i in pbar:
                    optimizer.zero_grad()

                    def objective_f(weights_m, validation_log_probs_n_m_C):
                        joint_log_probs_n_m_C = (
                            weights_m[None, :, None] + validation_log_probs_n_m_C)
                        marginal_logits_n_C = torch.logsumexp(joint_log_probs_n_m_C, dim=1)
                        objective = torch.nn.functional.cross_entropy(input=marginal_logits_n_C,
                                                                      target=labels_N[start_index:end_index],
                                                                      reduction="mean")
                        return objective

                    objective = objective_f(weights_m, validation_log_probs_n_m_C)
                    objective.backward()
                    optimizer.step(lambda: objective_f(weights_m, validation_log_probs_n_m_C))
                    pbar.set_description_str(desc=str(objective.item()))

                    if objective.item() <= best_objective:
                        best_objective = objective.item()
                        best_weights = weights_m.detach().clone()
                        best_i = i
                    elif i - best_i > patience:
                        break

                if verbose:
                    print("Restored best weights with objective", best_objective)
                weights_m = best_weights

                joint_log_probs_n_m_C = weights_m[None, :, None] + trial_log_probs_N_m_C[training_set_size:]
                marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                del joint_log_probs_n_m_C

                best_predictive_n_C = trial_log_probs_N_m_C[training_set_size:, torch.argmax(weights_m)]

                kl_best_marginal = torch.nn.functional.kl_div(input=marginal_predictive_n_C, target=best_predictive_n_C,
                                                              reduction="batchmean",
                                                              log_target=True).cpu().item()
                if verbose:
                    print("KL(best || ensemble) =", kl_best_marginal)

                predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
                crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                                   labels_N[
                                                                   training_set_size:]]).cpu().item()

                result = OBIPerformance(total_training_set_size=online_training_set_size + real_training_set_size,
                                        real_training_set_size=real_training_set_size,
                                        online_training_set_size=online_training_set_size,
                                        trial_index=trial,
                                        num_samples=num_samples,
                                        accuracy=accuracy,
                                        crossentropy=crossentropy,
                                        kl_best_marginal=kl_best_marginal)
                if verbose:
                    print(result)
                results.append(result)

    return results


def eval_obi_simple(*, log_probs_N_M_C, labels_N, training_set_size, num_samples_list, num_trials,
                    real_training_set_size, start_index=None, end_index_start=None, end_index_end=None, verbose=True):
    start_index = start_index if start_index is not None else 0
    end_index_start = end_index_start if end_index_start is not None else start_index
    end_index_end = end_index_end if end_index_end is not None else training_set_size

    N, M, C = log_probs_N_M_C.shape

    results = []
    # Compute the weights incl the initial training set.
    for trial in tqdm(range(num_trials)):
        for end_index in range(end_index_start, end_index_end + 1):
            online_training_set_size = end_index - start_index
            for num_samples in num_samples_list:
                if verbose:
                    print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(M, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :]

                true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(start_index, end_index)), :,
                                           labels_N[start_index:end_index]]

                weights_m = sum_log_probs(true_train_log_probs_n_m, dim=0)
                weights_m_max = torch.max(weights_m)

                joint_log_probs_n_m_C = (
                    weights_m[None, :, None] - weights_m_max + trial_log_probs_N_m_C[training_set_size:])
                marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                del joint_log_probs_n_m_C

                best_predictive_n_C = trial_log_probs_N_m_C[training_set_size:, torch.argmax(weights_m)]

                kl_best_marginal = torch.nn.functional.kl_div(input=marginal_predictive_n_C, target=best_predictive_n_C,
                                                              reduction="batchmean",
                                                              log_target=True).cpu().item()
                if verbose:
                    print("KL(best || ensemble) =", kl_best_marginal)

                predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
                crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                                   labels_N[
                                                                   training_set_size:]]).cpu().item()

                result = OBIPerformance(total_training_set_size=online_training_set_size + real_training_set_size,
                                        real_training_set_size=real_training_set_size,
                                        online_training_set_size=online_training_set_size,
                                        trial_index=trial,
                                        num_samples=num_samples,
                                        accuracy=accuracy,
                                        crossentropy=crossentropy,
                                        kl_best_marginal=kl_best_marginal)
                if verbose:
                    print(result)
                results.append(result)

    return results


def eval_obi_simple_topk_ensemble(*, log_probs_N_M_C, labels_N, training_set_size, num_samples_list, num_trials,
                                  real_training_set_size, k: int, start_index=None, end_index_start=None,
                                  end_index_end=None, verbose=True):
    start_index = start_index if start_index is not None else 0
    end_index_start = end_index_start if end_index_start is not None else start_index
    end_index_end = end_index_end if end_index_end is not None else training_set_size

    N, M, C = log_probs_N_M_C.shape

    results = []
    # Compute the weights incl the initial training set.
    for trial in tqdm(range(num_trials)):
        for end_index in range(end_index_start, end_index_end + 1):
            online_training_set_size = end_index - start_index
            for num_samples in num_samples_list:
                if verbose:
                    print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(M, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :]

                true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(start_index, end_index)), :,
                                           labels_N[start_index:end_index]]

                weights_m = sum_log_probs(true_train_log_probs_n_m, dim=0)

                # simply take the top 10.
                topk_samples = torch.topk(weights_m, k=k).indices

                joint_log_probs_n_m_C = trial_log_probs_N_m_C[training_set_size:, topk_samples]
                marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                del joint_log_probs_n_m_C

                best_predictive_n_C = trial_log_probs_N_m_C[training_set_size:, torch.argmax(weights_m)]

                kl_best_marginal = torch.nn.functional.kl_div(input=marginal_predictive_n_C, target=best_predictive_n_C,
                                                              reduction="batchmean",
                                                              log_target=True).cpu().item()
                if verbose:
                    print("KL(best || ensemble) =", kl_best_marginal)

                predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()

                crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                                   labels_N[
                                                                   training_set_size:]]).cpu().item()

                result = OBIPerformance(total_training_set_size=online_training_set_size + real_training_set_size,
                                        real_training_set_size=real_training_set_size,
                                        online_training_set_size=online_training_set_size,
                                        trial_index=trial,
                                        num_samples=num_samples,
                                        accuracy=accuracy,
                                        crossentropy=crossentropy,
                                        kl_best_marginal=kl_best_marginal)
                if verbose:
                    print(result)
                results.append(result)

    return results


def eval_best_topk_likelihood_tempered_posterior(*, log_probs_N_M_C, labels_N, training_set_size,
                                                 real_training_set_size, k: int):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    top_weights = torch.topk(weights_M, k=k).indices

    joint_log_probs_n_M_C = (
        weights_M[None, top_weights, None] / (N - training_set_size) + log_probs_N_M_C[training_set_size:,
                                                                       top_weights])

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_M_C, dim=1), dim=1)

    best_predictive_n_C = log_probs_N_M_C[training_set_size:, top_weights[0]]

    kl_best_marginal = torch.nn.functional.kl_div(input=marginal_predictive_n_C, target=best_predictive_n_C,
                                                  reduction="batchmean",
                                                  log_target=True).cpu().item()
    print("KL(best || ensemble) =", kl_best_marginal)

    predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
    accuracy = torch.mean(
        (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
    crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                       labels_N[training_set_size:]]).cpu().item()
    del predictions_n

    result = OBIPerformance(total_training_set_size=N - training_set_size + real_training_set_size,
                            real_training_set_size=real_training_set_size,
                            online_training_set_size=N - training_set_size,
                            trial_index=0,
                            num_samples=M,
                            accuracy=accuracy,
                            crossentropy=crossentropy,
                            kl_best_marginal=kl_best_marginal)
    print(result)

    return result


def eval_best_topk_likelihood_posterior(*, log_probs_N_M_C, labels_N, training_set_size,
                                        real_training_set_size, k: int):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    top_weights = torch.topk(weights_M, k=k).indices

    joint_log_probs_n_m_C = (weights_M[None, top_weights, None] + log_probs_N_M_C[training_set_size:, top_weights])

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)

    best_predictive_n_C = log_probs_N_M_C[training_set_size:, top_weights[0]]

    kl_best_marginal = torch.nn.functional.kl_div(input=marginal_predictive_n_C, target=best_predictive_n_C,
                                                  reduction="batchmean",
                                                  log_target=True).cpu().item()
    print("KL(best || ensemble) =", kl_best_marginal)

    predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
    accuracy = torch.mean(
        (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
    crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                       labels_N[training_set_size:]]).cpu().item()
    del predictions_n

    result = OBIPerformance(total_training_set_size=N - training_set_size + real_training_set_size,
                            real_training_set_size=real_training_set_size,
                            online_training_set_size=N - training_set_size,
                            trial_index=0,
                            num_samples=M,
                            accuracy=accuracy,
                            crossentropy=crossentropy,
                            kl_best_marginal=kl_best_marginal)
    print(result)

    return result


def eval_best_topk_liklihood_ensemble(*, log_probs_N_M_C, labels_N, training_set_size,
                                      real_training_set_size, k):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    top_weights = torch.topk(weights_M, k=k).indices

    joint_log_probs_n_m_C = log_probs_N_M_C[training_set_size:, top_weights]

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)

    best_predictive_n_C = log_probs_N_M_C[training_set_size:, top_weights[0]]

    kl_best_marginal = torch.nn.functional.kl_div(input=marginal_predictive_n_C, target=best_predictive_n_C,
                                                  reduction="batchmean",
                                                  log_target=True).cpu().item()
    print("KL(best || ensemble) =", kl_best_marginal)

    predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
    accuracy = torch.mean(
        (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
    crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                       labels_N[training_set_size:]]).cpu().item()
    del predictions_n

    result = OBIPerformance(total_training_set_size=N - training_set_size + real_training_set_size,
                            real_training_set_size=real_training_set_size,
                            online_training_set_size=N - training_set_size,
                            trial_index=0,
                            num_samples=M,
                            accuracy=accuracy,
                            crossentropy=crossentropy,
                            kl_best_marginal=kl_best_marginal)
    print(result)

    return result


def get_accuracy_crossentropy(*, log_probs_N_M_C, labels_N, training_set_size):
    N, M, C = log_probs_N_M_C.shape

    predictions_n_M = torch.argmax(log_probs_N_M_C[training_set_size:], dim=2)
    accuracy_M = torch.mean((predictions_n_M == labels_N[training_set_size:, None]).float(), dim=0)
    crossentropy_M = -torch.mean(log_probs_N_M_C[list(range(training_set_size, N)), :,
                                 labels_N[training_set_size:]], dim=0)
    return accuracy_M, crossentropy_M


def eval_best_by_individual_accuracy(*, log_probs_N_M_C, labels_N, training_set_size):
    N, M, C = log_probs_N_M_C.shape

    predictions_n_M = torch.argmax(log_probs_N_M_C[training_set_size:], dim=2)
    accuracy_M = torch.mean((predictions_n_M == labels_N[training_set_size:, None]).float(), dim=0)

    best_accuracy, best_index = torch.max(accuracy_M, dim=0)

    crossentropy = -torch.mean(log_probs_N_M_C[list(range(training_set_size, N)), best_index,
                                               labels_N[training_set_size:]])

    best_accuracy = best_accuracy.cpu().item()
    crossentropy = crossentropy.cpu().item()

    print("Best accuracy: ", best_accuracy)
    print("Crossentropy: ", crossentropy)

    return best_accuracy, crossentropy


def eval_best_by_individual_crossentropy(*, log_probs_N_M_C, labels_N, training_set_size):
    N, M, C = log_probs_N_M_C.shape

    crossentropy_M = -torch.mean(log_probs_N_M_C[list(range(training_set_size, N)), :,
                                 labels_N[training_set_size:]], dim=0)
    best_crossentropy, best_index = torch.min(crossentropy_M, dim=0)
    predictions_n = torch.argmax(log_probs_N_M_C[training_set_size:, best_index, :], dim=1)
    accuracy = torch.mean((predictions_n == labels_N[training_set_size:]).float(), dim=0)

    accuracy = accuracy.cpu().item()
    best_crossentropy = best_crossentropy.cpu().item()
    print("Accuracy: ", accuracy)
    print("Best crossentropy: ", best_crossentropy)
    return accuracy, best_crossentropy


def get_log_likelihoods(*, log_probs_N_M_C, labels_N, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(log_probs_N_M_C)
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(start, end)), :,
                          labels_N[start:end]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0)
    return weights_M


def eval_best_bayesian(*, log_probs_N_M_C, labels_N, training_set_size,
                       real_training_set_size):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    joint_log_probs_n_M_C = (weights_M[None, :, None] + log_probs_N_M_C[training_set_size:])

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_M_C, dim=1), dim=1)

    best_predictive_n_C = log_probs_N_M_C[training_set_size:, torch.argmax(weights_M)]

    kl_best_marginal = torch.nn.functional.kl_div(marginal_predictive_n_C, best_predictive_n_C, reduction="batchmean",
                                                  log_target=True)
    print("KL(best || ensemble) =", kl_best_marginal)

    predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
    accuracy = torch.mean(
        (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
    crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                       labels_N[training_set_size:]]).cpu().item()
    del predictions_n

    result = OBIPerformance(total_training_set_size=N - training_set_size + real_training_set_size,
                            real_training_set_size=real_training_set_size,
                            online_training_set_size=N - training_set_size,
                            trial_index=0,
                            num_samples=M,
                            accuracy=accuracy,
                            crossentropy=crossentropy,
                            kl_best_marginal=kl_best_marginal)
    print(result)

    return result
