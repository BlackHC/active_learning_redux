__all__ = ['ModelOptimizer', 'ModelOptimizerFactory']


from dataclasses import dataclass
from typing import Union

import torch
import torch.nn
import torch.optim
from torch import nn as nn
from torch.nn import functional as F
from torchvision import models

from .consistent_mc_dropout import (
    BayesianModule,
    ConsistentMCDropout,
    ConsistentMCDropout2d,
)


@dataclass
class ModelOptimizer:
    model: Union[torch.nn.Module, BayesianModule]
    optimizer: torch.optim.Optimizer


class ModelOptimizerFactory:
    def create_model_optimizer(self) -> ModelOptimizer:
        raise NotImplementedError
