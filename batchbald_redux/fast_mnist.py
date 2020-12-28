# AUTOGENERATED! DO NOT EDIT! File to edit: 05a_fast_mnist.ipynb (unless otherwise specified).

__all__ = ['FastMNIST']

# Cell

import torch
import torch.utils.data as data
from torch.utils.data import Dataset
from torchvision import datasets, transforms

# Cell
from torchvision.datasets import MNIST


# From https://tinyurl.com/pytorch-fast-mnist
class FastMNIST(MNIST):
    def __init__(self, *args, device, **kwargs):
        super().__init__(*args, **kwargs)

        # Scale data to [0,1]
        self.data = self.data.unsqueeze(1).float().div(255)

        # Normalize it with the usual MNIST mean and std
        self.data = self.data.sub_(0.1307).div_(0.3081)

        # Put both data and targets on GPU in advance
        self.data, self.targets = self.data.to(device), self.targets.to(device)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        img, target = self.data[index], self.targets[index]

        return img, target