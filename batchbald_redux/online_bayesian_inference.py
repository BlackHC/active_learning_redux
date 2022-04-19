from dataclasses import dataclass
from typing import List

import torch
import numpy as np

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
    obi_upperbound_result = eval_obi_upper_bound_topk_liklihood_ensemble(log_probs_N_M_C=log_probs_N_M_C,
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


def eval_obi_simple(*, log_probs_N_M_C, labels_N, training_set_size, start_index, num_samples_list, num_trials,
                    real_training_set_size, end_index=None):
    end_index = end_index if end_index is not None else training_set_size

    N, M, C = log_probs_N_M_C.shape

    results = []
    # Compute the weights incl the initial training set.
    for online_training_set_size in range(start_index, end_index + 1):
        for num_samples in num_samples_list:
            for trial in range(num_trials):
                print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(M, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :]

                true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(online_training_set_size)), :,
                                           labels_N[:online_training_set_size]]

                mix_weights_m = sum_log_probs(true_train_log_probs_n_m, dim=0)
                mix_weights_m_max = torch.max(mix_weights_m)

                # print(mix_weights_m_max, (torch.logsumexp(mix_weights_m, dim=0) - np.log(len(mix_weights_m))) /
                # online_training_set_size)
                # sns.kdeplot((mix_weights_m - mix_weights_m_max).numpy(), ).set_title(f"{online_training_set_size}/{
                # num_samples}/{trial}")
                # plt.hist(mix_weights_m.numpy())
                # plt.show()

                joint_log_probs_n_m_C = (
                    mix_weights_m[None, :, None] - mix_weights_m_max + trial_log_probs_N_m_C[training_set_size:])
                marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                del joint_log_probs_n_m_C

                predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()
                crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                                   labels_N[
                                                                   training_set_size:]]).cpu().item()

                result = OBIPerformance(total_training_set_size=online_training_set_size,
                                        real_training_set_size=real_training_set_size,
                                        online_training_set_size=online_training_set_size,
                                        trial_index=trial,
                                        num_samples=num_samples,
                                        accuracy=accuracy,
                                        crossentropy=crossentropy)
                print(result)
                results.append(result)

    return results


def eval_obi_simple_topk_ensemble(*, log_probs_N_M_C, labels_N, training_set_size, start_index, num_samples_list,
                                  num_trials,
                                  real_training_set_size, end_index, k):
    end_index = end_index if end_index is not None else training_set_size

    N, M, C = log_probs_N_M_C.shape

    results = []
    # Compute the weights incl the initial training set.
    for online_training_set_size in range(start_index, end_index + 1):
        for num_samples in num_samples_list:
            for trial in range(num_trials):
                print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(M, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :]

                true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(online_training_set_size)), :,
                                           labels_N[:online_training_set_size]]

                mix_weights_m = sum_log_probs(true_train_log_probs_n_m, dim=0)

                # simply take the top 10.
                topk_samples = torch.topk(mix_weights_m, k=k).indices

                joint_log_probs_n_m_C = trial_log_probs_N_m_C[training_set_size:, topk_samples]
                marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                del joint_log_probs_n_m_C

                predictions_n = torch.argmax(marginal_predictive_n_C, dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[training_set_size:]).type(torch.float)).cpu().item()

                crossentropy = -torch.mean(marginal_predictive_n_C[list(range(len(marginal_predictive_n_C))),
                                                                   labels_N[
                                                                   training_set_size:]]).cpu().item()

                result = OBIPerformance(total_training_set_size=online_training_set_size,
                                        real_training_set_size=real_training_set_size,
                                        online_training_set_size=online_training_set_size,
                                        trial_index=trial,
                                        num_samples=num_samples,
                                        accuracy=accuracy,
                                        crossentropy=crossentropy)
                print(result)
                results.append(result)

    return results


def eval_obi_upper_bound_topk_likelihood_tempered_posterior(*, log_probs_N_M_C, labels_N, training_set_size,
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
                            crossentropy=crossentropy)
    print(result)

    return result


def eval_obi_upper_bound_topk_likelihood_posterior(*, log_probs_N_M_C, labels_N, training_set_size,
                                                   real_training_set_size, k: int):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    top_weights = torch.topk(weights_M, k=k).indices

    joint_log_probs_n_M_C = (weights_M[None, top_weights, None] + log_probs_N_M_C[training_set_size:, top_weights])

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_M_C, dim=1), dim=1)

    best_predictive_n_C = log_probs_N_M_C[training_set_size:, top_weights[0]]

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
                            crossentropy=crossentropy)
    print(result)

    return result


def eval_obi_upper_bound_topk_liklihood_ensemble(*, log_probs_N_M_C, labels_N, training_set_size,
                                                 real_training_set_size, k):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    top_indices = torch.topk(weights_M, k=k).indices

    joint_log_probs_n_M_C = log_probs_N_M_C[training_set_size:, top_indices]

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_M_C, dim=1), dim=1)

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
                            crossentropy=crossentropy)
    print(result)

    return result


def eval_obi_upper_bound_by_individual_accuracy(*, log_probs_N_M_C, labels_N, training_set_size,
                                                real_training_set_size):
    N, M, C = log_probs_N_M_C.shape

    predictions_n_M = torch.argmax(log_probs_N_M_C[training_set_size:], dim=2)
    accuracy_M = torch.mean((predictions_n_M == labels_N[training_set_size:, None]).float(), dim=0)
    best_accuracy, best_index = torch.max(accuracy_M, dim=0)
    print("Best accuracy: ", best_accuracy.cpu().item())

    crossentropy = -torch.mean(log_probs_N_M_C[list(range(training_set_size, N)), best_index,
                                               labels_N[training_set_size:]])
    print("Crossentropy: ", crossentropy.cpu().item())


def eval_obi_upper_bound_by_individual_crossentropy(*, log_probs_N_M_C, labels_N, training_set_size,
                                                    real_training_set_size):
    N, M, C = log_probs_N_M_C.shape

    crossentropy_M = -torch.mean(log_probs_N_M_C[list(range(training_set_size, N)), :,
                                 labels_N[training_set_size:]], dim=0)
    best_crossentropy, best_index = torch.min(crossentropy_M, dim=0)
    print("Best crossentropy: ", best_crossentropy.cpu().item())
    predictions_n = torch.argmax(log_probs_N_M_C[training_set_size:, best_index, :], dim=1)
    accuracy = torch.mean((predictions_n == labels_N[training_set_size:]).float(), dim=0)
    print("Accuracy: ", accuracy.cpu().item())


def eval_obi_upper_bound(*, log_probs_N_M_C, labels_N, training_set_size,
                         real_training_set_size):
    N, M, C = log_probs_N_M_C.shape

    true_likelihood_n_M = log_probs_N_M_C[list(range(training_set_size, N)), :,
                          labels_N[training_set_size:]]
    weights_M = sum_log_probs(true_likelihood_n_M, dim=0).double()

    joint_log_probs_n_M_C = (weights_M[None, :, None] + log_probs_N_M_C[training_set_size:])

    marginal_predictive_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_M_C, dim=1), dim=1)

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
                            crossentropy=crossentropy)
    print(result)

    return result
