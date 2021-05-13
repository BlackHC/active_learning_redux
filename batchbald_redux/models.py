# AUTOGENERATED! DO NOT EDIT! File to edit: 06b_mnist_models.ipynb (unless otherwise specified).

__all__ = ['BayesianMNISTCNN', 'BayesianMNISTCNN_EBM', 'MnistOptimizerFactory']

# Cell
from dataclasses import dataclass

import torch
import torch.nn
import torch.optim
from torch import nn as nn
from torch.nn import functional as F

from .consistent_mc_dropout import (
    BayesianModule,
    ConsistentMCDropout,
    ConsistentMCDropout2d,
)

from .model_optimizer_factory import ModelOptimizer, ModelOptimizerFactory

# Cell


class BayesianMNISTCNN(BayesianModule):
    def __init__(self, num_classes=10):
        super().__init__()

        self.conv1 = nn.Conv2d(1, 32, kernel_size=5)
        self.conv1_drop = ConsistentMCDropout2d()
        self.conv2 = nn.Conv2d(32, 64, kernel_size=5)
        self.conv2_drop = ConsistentMCDropout2d()
        self.fc1 = nn.Linear(1024, 128)
        self.fc1_drop = ConsistentMCDropout()
        self.fc2 = nn.Linear(128, num_classes)

    def mc_forward_impl(self, input: torch.Tensor):
        input = F.relu(F.max_pool2d(self.conv1_drop(self.conv1(input)), 2))
        input = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(input)), 2))
        input = input.view(-1, 1024)
        input = F.relu(self.fc1_drop(self.fc1(input)))
        input = self.fc2(input)
        input = F.log_softmax(input, dim=1)

        return input

# Cell


class BayesianMNISTCNN_EBM(BayesianModule):
    """Without Softmax."""

    def __init__(self, num_classes=10):
        super().__init__()

        self.conv1 = nn.Conv2d(1, 32, kernel_size=5)
        self.conv1_drop = ConsistentMCDropout2d()
        self.conv2 = nn.Conv2d(32, 64, kernel_size=5)
        self.conv2_drop = ConsistentMCDropout2d()
        self.fc1 = nn.Linear(1024, 128)
        self.fc1_drop = ConsistentMCDropout()
        self.fc2 = nn.Linear(128, num_classes)

    def mc_forward_impl(self, input: torch.Tensor):
        input = F.relu(F.max_pool2d(self.conv1_drop(self.conv1(input)), 2))
        input = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(input)), 2))
        input = input.view(-1, 1024)
        input = F.relu(self.fc1_drop(self.fc1(input)))
        input = self.fc2(input)

        return input

# Cell


@dataclass
class MnistOptimizerFactory(ModelOptimizerFactory):
    def create_model_optimizer(self) -> ModelOptimizer:
        model = BayesianMNISTCNN()
        optimizer = torch.optim.Adam(model.parameters(), weight_decay=5e-4)
        return ModelOptimizer(model=model, optimizer=optimizer)