# AUTOGENERATED! DO NOT EDIT! File to edit: 08b_experiment_data.ipynb (unless otherwise specified).

__all__ = ['ExperimentData', 'OoDDatasetConfig', 'ExperimentDataConfig', 'load_experiment_data']

# Cell

from dataclasses import dataclass
from typing import List, Optional

import torch
import torch.utils.data
from torch import nn
from torch.utils.data import Dataset

from .active_learning import ActiveLearningData
from .dataset_challenges import (
    AdditiveGaussianNoise,
    AliasDataset,
    NamedDataset,
    get_balanced_sample_indices_by_class,
)
from .datasets import get_dataset

# Cell


@dataclass
class ExperimentData:
    active_learning: ActiveLearningData
    validation_dataset: Dataset
    evaluation_dataset: Dataset
    test_dataset: Dataset

    train_augmentations: nn.Module

    initial_training_set_indices: List[int]
    evaluation_set_indices: List[int]

    ood_dataset: NamedDataset


@dataclass
class OoDDatasetConfig:
    ood_dataset_name: str
    ood_repetitions: float
    ood_exposure: bool


@dataclass
class ExperimentDataConfig:
    id_dataset_name: str
    id_repetitions: float

    initial_training_set_size: int

    validation_set_size: int
    validation_split_random_state: int

    evaluation_set_size: int

    add_dataset_noise: bool

    ood_dataset_config: Optional[OoDDatasetConfig]

    device: str

    def load(self) -> ExperimentData:
        return load_experiment_data(
            id_dataset_name=self.id_dataset_name,
            id_repetitions=self.id_repetitions,
            initial_training_set_size=self.initial_training_set_size,
            validation_set_size=self.validation_set_size,
            validation_split_random_state=self.validation_split_random_state,
            evaluation_set_size=self.evaluation_set_size,
            ood_dataset_config=self.ood_dataset_config,
            device=self.device,
        )


def load_experiment_data(
    *,
    id_dataset_name: str,
    id_repetitions: float,
    initial_training_set_size: int,
    validation_set_size: int,
    validation_split_random_state: int,
    evaluation_set_size: int,
    add_dataset_noise: bool,
    ood_dataset_config: Optional[OoDDatasetConfig],
    device: str,
) -> ExperimentData:
    split_dataset = get_dataset(
        id_dataset_name,
        root="data",
        validation_set_size=validation_set_size,
        validation_split_random_state=validation_split_random_state,
        normalize_like_cifar10=True,
        device_hint=device,
    )

    train_dataset = split_dataset.train

    # TODO: add hook here to further process the train dataset?

    # If we reduce the train set, we need to do so before picking the initial train set.
    if id_repetitions < 1:
        train_dataset = train_dataset * id_repetitions

    num_classes = train_dataset.get_num_classes()
    initial_samples_per_class = initial_training_set_size // num_classes
    evaluation_set_samples_per_class = evaluation_set_size // num_classes
    samples_per_class = initial_samples_per_class + evaluation_set_samples_per_class
    balanced_samples_indices = get_balanced_sample_indices_by_class(
        train_dataset,
        num_classes=num_classes,
        samples_per_class=samples_per_class,
        seed=validation_split_random_state,
    )

    initial_training_set_indices = [
        idx for by_class in balanced_samples_indices.values() for idx in by_class[:initial_samples_per_class]
    ]
    evaluation_set_indices = [
        idx for by_class in balanced_samples_indices.values() for idx in by_class[initial_samples_per_class:]
    ]

    # If we over-sample the train set, we do so after picking the initial train set to avoid duplicates.
    if id_repetitions > 1:
        train_dataset = train_dataset * id_repetitions

    if ood_dataset_config:
        original_ood_dataset = get_dataset(ood_dataset_config.ood_dataset_name, root="data", normalize_like_cifar10=True).train
        if ood_dataset_config.ood_exposure:
            train_dataset = train_dataset.one_hot(device=device)
            ood_dataset = original_ood_dataset.uniform_target(device=device, num_classes=train_dataset.get_num_classes())
        else:
            ood_dataset = original_ood_dataset.constant_target(
                target=torch.tensor(-1, device=device), num_classes=train_dataset.get_num_classes()
            )

        if ood_dataset_config.ood_repetitions != 1:
            ood_dataset = ood_dataset_config.ood_dataset * ood_repetitions

        train_dataset = train_dataset + ood_dataset
    else:
        original_ood_dataset = None

    if add_dataset_noise:
        train_dataset = AdditiveGaussianNoise(train_dataset, 0.1)

    active_learning_data = ActiveLearningData(train_dataset)

    active_learning_data.acquire_base_indices(initial_training_set_indices)

    evaluation_dataset = AliasDataset(
        active_learning_data.extract_dataset_from_base_indices(evaluation_set_indices),
        f"Evaluation Set ({len(evaluation_set_indices)} samples)",
    )

    return ExperimentData(
        active_learning=active_learning_data,
        validation_dataset=split_dataset.validation,
        test_dataset=split_dataset.test,
        evaluation_dataset=evaluation_dataset,
        train_augmentations=split_dataset.train_augmentations,
        initial_training_set_indices=initial_training_set_indices,
        evaluation_set_indices=evaluation_set_indices,
        ood_dataset=original_ood_dataset,
    )