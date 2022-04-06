"""
For active learning, we need to split the available training data between a
training set and a pool set of (unlabelled) data, which we score using our
model and acquisition function and add to the training set peu a peu.
"""

__all__ = ['ActiveLearningData', 'RandomFixedLengthSampler']

from typing import List

import numpy as np
import torch
import torch.utils.data as data


class ActiveLearningData:
    """Splits `dataset` into an active dataset and an available dataset."""

    base_dataset: data.Dataset
    training_dataset: data.Subset
    pool_dataset: data.Subset
    training_mask: np.ndarray
    pool_mask: np.ndarray

    def __init__(self, dataset: data.Dataset):
        super().__init__()
        self.base_dataset = dataset
        self.training_mask = np.full((len(dataset),), False)
        self.pool_mask = np.full((len(dataset),), True)

        # TODO: use dataset challenges here?
        self.training_dataset = data.Subset(self.base_dataset, None)
        self.pool_dataset = data.Subset(self.base_dataset, None)

        self._update_indices()

    def _update_indices(self):
        self.training_dataset.indices = np.nonzero(self.training_mask)[0]
        self.pool_dataset.indices = np.nonzero(self.pool_mask)[0]

    def get_base_indices(self, pool_indices: List[int]) -> List[int]:
        """Transform indices (in `pool_dataset`) to indices in the original `dataset`."""
        indices = self.pool_dataset.indices[pool_indices]
        return indices

    def acquire(self, pool_indices):
        """
        Acquire elements from the pool dataset into the training dataset.

        Add them to training dataset & remove them from the pool dataset.
        """
        base_indices = self.get_base_indices(pool_indices)
        self.acquire_base_indices(base_indices)

    def acquire_base_indices(self, base_indices):
        self.training_mask[base_indices] = True
        self.pool_mask[base_indices] = False
        self._update_indices()

    def remove_from_pool(self, pool_indices):
        base_indices = self.get_base_indices(pool_indices)

        self.remove_base_indices(base_indices)

    def remove_base_indices(self, dataset_indices):
        self.pool_mask[dataset_indices] = False
        self._update_indices()

    def get_random_pool_indices(self, size) -> torch.LongTensor:
        assert 0 <= size <= len(self.pool_dataset)
        pool_indices = torch.randperm(len(self.pool_dataset))[:size]
        return pool_indices

    def extract_dataset_from_pool(self, size) -> data.Dataset:
        """
        Extract a dataset randomly from the pool dataset and make those indices unavailable.

        Useful for extracting a validation set.
        """
        return self.extract_dataset_from_pool_from_indices(self.get_random_pool_indices(size))

    def extract_dataset_from_pool_from_indices(self, pool_indices) -> data.Dataset:
        """
        Extract a dataset from the pool dataset and make those indices unavailable.

        Useful for extracting a validation set.
        """
        dataset_indices = self.get_base_indices(pool_indices)

        return self.extract_dataset_from_base_indices(dataset_indices)

    def extract_dataset_from_base_indices(self, base_indices) -> data.Dataset:
        self.remove_base_indices(base_indices)
        return data.Subset(self.base_dataset, base_indices)

    def __repr__(self):
        return f"ActiveLearningData(base_dataset={self.base_dataset}, num_training_samples={len(self.training_dataset)}, num_pool_samples={len(self.pool_dataset)})"


class RandomFixedLengthSampler(data.Sampler):
    """
    Sometimes, you really want to do more with little data without increasing the number of epochs.
    This sampler takes a `dataset` and draws `target_length` samples from it (with repetition).
    """

    dataset: data.Dataset
    target_length: int

    def __init__(self, dataset: data.Dataset, target_length: int):
        super().__init__(dataset)
        self.dataset = dataset
        self.target_length = target_length

    def __iter__(self):
        # Ensure that we don't lose data by accident.
        if self.target_length < len(self.dataset):
            return iter(torch.randperm(len(self.dataset)).tolist())

        # Sample slightly more indices to avoid biasing towards start of dataset.
        # Have the same number of duplicates for each sample.
        indices = torch.randperm(self.target_length + (-self.target_length % len(self.dataset)))

        return iter((indices[: self.target_length] % len(self.dataset)).tolist())

    def __len__(self):
        return max(self.target_length, len(self.dataset))