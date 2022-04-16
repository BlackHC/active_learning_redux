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
    # TODO: rewrite this to use the newer TrainedModel interface!
    num_additional_training_indices = len(additional_training_indices)
    sub_train_set = train_dataset.subset(additional_training_indices)
    joint_set = sub_train_set + test_dataset

    joint_loader = torch.utils.data.DataLoader(
        joint_set, batch_size=eval_batchsize, drop_last=False, shuffle=False
    )

    total_samples = max(num_samples_list) * up_factor
    log_probs_N_M_C, labels_N = model.get_predictions_labels(num_samples=total_samples, loader=joint_loader,
                                                             device=device,
                                                             storage_device="cpu")

    results = []
    for online_training_set_size in range(num_additional_training_indices + 1):
        for num_samples in num_samples_list:
            for trial in range(num_trials):
                print(f"Online Training Size/Num Samples/Trial: {online_training_set_size}/{num_samples}/{trial}")
                sample_subset = np.random.choice(total_samples, num_samples, replace=False)
                trial_log_probs_N_m_C = log_probs_N_M_C[:, sample_subset, :].double()
                true_train_log_probs_n_m = trial_log_probs_N_m_C[list(range(online_training_set_size)), :,
                                           labels_N[:online_training_set_size]]
                # make the log probs more amenable to being summed up
                true_train_log_probs_n_m = torch.sort(true_train_log_probs_n_m, dim=0, descending=False).values
                mix_weights_m = torch.sum(true_train_log_probs_n_m, dim=0)
                mix_weights_m_max = torch.max(mix_weights_m)
                joint_log_probs_n_m_C = (mix_weights_m[None, :, None] - mix_weights_m_max
                                         + trial_log_probs_N_m_C[num_additional_training_indices:])
                predictions_n = torch.argmax(torch.sum(joint_log_probs_n_m_C.exp(), dim=1), dim=1)
                accuracy = torch.mean(
                    (predictions_n == labels_N[num_additional_training_indices:]).type(torch.float)).cpu().item()
                posterior_log_probs_n_C = torch.log_softmax(torch.logsumexp(joint_log_probs_n_m_C, dim=1), dim=1)
                crossentropy = -torch.mean(posterior_log_probs_n_C[list(range(len(posterior_log_probs_n_C))),
                                                                   labels_N[
                                                                   num_additional_training_indices:]]).cpu().item()

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
