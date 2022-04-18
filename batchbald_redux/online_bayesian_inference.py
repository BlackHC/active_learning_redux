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
                                       additional_training_indices: List[int], num_samples_list: List[int],
                                       num_trials: int,
                                       up_factor: int, eval_batchsize: int, device) -> List[OBIPerformance]:
    log_probs_N_M_C, labels_N = get_obi_predictions_labels(model, test_dataset=test_dataset, train_dataset=train_dataset,
                                                           additional_training_indices=additional_training_indices,
                                                           num_samples=num_samples_list[-1] * up_factor,
                                                           eval_batchsize=eval_batchsize,
                                                           device=device)

    num_additional_training_indices = len(additional_training_indices)
    return eval_obi_simple(log_probs_N_M_C=log_probs_N_M_C, labels_N=labels_N,
                           num_additional_training_indices=num_additional_training_indices,
                           num_samples_list=num_samples_list, num_trials=num_trials,
                           real_training_set_size=real_training_set_size)


def get_obi_predictions_labels(model, *, test_dataset, train_dataset, additional_training_indices, num_samples,
                               eval_batchsize, device):
    # TODO: rewrite this to use the newer TrainedModel interface!
    sub_train_set = train_dataset.subset(additional_training_indices)
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

def eval_obi_simple(log_probs_N_M_C, labels_N, num_additional_training_indices, num_samples_list, num_trials,
                    real_training_set_size):
    N, M, C = log_probs_N_M_C.shape
    #log_probs_N_M_C = log_probs_N_M_C.double()

    results = []
    for online_training_set_size in range(num_additional_training_indices + 1):
        for num_samples in num_samples_list:
            for trial in range(num_trials):
                print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(M, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :]
                # Fully independent.
                #trial_log_probs_N_m_C = torch.logsumexp(trial_log_probs_N_m_C, dim=1, keepdim=True) - np.log(num_samples)

                true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(online_training_set_size)), :,
                                           labels_N[:online_training_set_size]]
                # true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(len(trial_log_probs_N_m_C))), :,
                #                            labels_N]
                # make the log probs more amenable to being summed up
                true_train_log_probs_n_m = torch.sort(true_train_log_probs_n_m, dim=0, descending=False).values
                mix_weights_m = torch.sum(true_train_log_probs_n_m, dim=0)
                mix_weights_m_max = torch.max(mix_weights_m)

                #print(mix_weights_m_max, (torch.logsumexp(mix_weights_m, dim=0) - np.log(len(mix_weights_m))) / online_training_set_size)
                #sns.kdeplot((mix_weights_m - mix_weights_m_max).numpy(), ).set_title(f"{online_training_set_size}/{num_samples}/{trial}")
                # plt.hist(mix_weights_m.numpy())
                # plt.show()

                joint_log_probs_n_m_C = (mix_weights_m[None, :, None] - mix_weights_m_max
                                         + trial_log_probs_N_m_C[num_additional_training_indices:]) #[:, mix_weights_m >= mix_weights_m_max - 0.1, :]
                del mix_weights_m
                #predictions_n = torch.argmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                predictions_n = torch.argmax(torch.sum(joint_log_probs_n_m_C.exp(), dim=1), dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[num_additional_training_indices:]).type(torch.float)).cpu().item()
                posterior_log_probs_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                crossentropy = -torch.mean(posterior_log_probs_n_C[list(range(len(posterior_log_probs_n_C))),
                                                                   labels_N[
                                                                   num_additional_training_indices:]]).cpu().item()
                del predictions_n

                result = OBIPerformance(total_training_set_size=real_training_set_size + online_training_set_size,
                                        real_training_set_size=real_training_set_size,
                                        online_training_set_size=online_training_set_size,
                                        trial_index=trial,
                                        num_samples=num_samples,
                                        accuracy=accuracy,
                                        crossentropy=crossentropy)
                print(result)
                results.append(result)
    return results
