# AUTOGENERATED! DO NOT EDIT! File to edit: 07c_train_eval_model.ipynb (unless otherwise specified).

__all__ = ['TrainEvalModel', 'TrainSelfDistillationEvalModel', 'TrainRandomLabelEvalModel', 'TrainExplicitEvalModel']

# Cell
from dataclasses import dataclass
from typing import Type

import torch
import torch.nn
import torch.utils.data

from .active_learning import RandomFixedLengthSampler
from .black_box_model_training import train
from .consistent_mc_dropout import get_log_mean_probs
from .dataset_challenges import (
    RandomLabelsDataset,
    ReplaceTargetsDataset,
)
from .model_optimizer_factory import ModelOptimizerFactory
from .trained_model import TrainedMCDropoutModel, TrainedModel

# Cell


class TrainEvalModel:
    def __call__(self, *, training_log, device) -> TrainedModel:
        raise NotImplementedError()


@dataclass
class TrainSelfDistillationEvalModel(TrainEvalModel):
    num_pool_samples: int
    num_training_samples: int
    num_validation_samples: int
    num_patience_epochs: int
    max_epochs: int
    training_dataset: torch.utils.data.Dataset
    eval_dataset: torch.utils.data.Dataset
    validation_loader: torch.utils.data.DataLoader
    training_batch_size: int
    model_optimizer_factory: Type[ModelOptimizerFactory]
    trained_model: TrainedModel
    min_samples_per_epoch: int

    def __call__(self, *, training_log, device):
        train_eval_dataset = torch.utils.data.ConcatDataset([self.training_dataset, self.eval_dataset])
        train_eval_loader = torch.utils.data.DataLoader(train_eval_dataset, batch_size=512, drop_last=False)

        eval_log_probs_N_C = get_log_mean_probs(
            self.trained_model.get_log_probs_N_K_C(train_eval_loader, device=device)
        )

        eval_self_distillation_dataset = ReplaceTargetsDataset(dataset=train_eval_dataset, targets=eval_log_probs_N_C)
        train_eval_self_distillation_loader = torch.utils.data.DataLoader(
            eval_self_distillation_dataset,
            batch_size=self.training_batch_size,
            sampler=RandomFixedLengthSampler(eval_self_distillation_dataset, self.min_samples_per_epoch),
            drop_last=True,
        )

        eval_model_optimizer = self.model_optimizer_factory().create_model_optimizer()

        loss = torch.nn.KLDivLoss(log_target=True, reduction="batchmean")

        train(
            model=eval_model_optimizer.model,
            optimizer=eval_model_optimizer.optimizer,
            loss=loss,
            validation_loss=torch.nn.NLLLoss(),
            training_samples=self.num_training_samples,
            validation_samples=self.num_validation_samples,
            train_loader=train_eval_self_distillation_loader,
            validation_loader=self.validation_loader,
            patience=self.num_patience_epochs,
            max_epochs=self.max_epochs,
            device=device,
            training_log=training_log,
        )

        return TrainedMCDropoutModel(num_samples=self.num_pool_samples, model=eval_model_optimizer.model)


@dataclass
class TrainRandomLabelEvalModel(TrainEvalModel):
    num_pool_samples: int
    num_training_samples: int
    num_validation_samples: int
    num_patience_epochs: int
    max_epochs: int
    training_dataset: torch.utils.data.Dataset
    eval_dataset: torch.utils.data.Dataset
    validation_loader: torch.utils.data.DataLoader
    training_batch_size: int
    model_optimizer_factory: ModelOptimizerFactory

    def __call__(self, *, training_log, device):
        # TODO: support one_hot!
        # TODO: different seed needed!
        train_eval_dataset = torch.utils.data.ConcatDataset(
            [self.training_dataset, RandomLabelsDataset(self.eval_dataset, seed=0)]
        )
        train_eval_loader = torch.utils.data.DataLoader(
            train_eval_dataset, batch_size=self.training_batch_size, drop_last=True, shuffle=True
        )

        eval_model_optimizer = self.model_optimizer_factory.create_model_optimizer()

        loss = torch.nn.NLLLoss()

        train(
            model=eval_model_optimizer.model,
            optimizer=eval_model_optimizer.optimizer,
            loss=loss,
            validation_loss=loss,
            training_samples=self.num_training_samples,
            validation_samples=self.num_validation_samples,
            train_loader=train_eval_loader,
            validation_loader=self.validation_loader,
            patience=self.num_patience_epochs,
            max_epochs=self.max_epochs,
            device=device,
            training_log=training_log,
        )

        return TrainedMCDropoutModel(num_samples=self.num_pool_samples, model=eval_model_optimizer.model)


@dataclass
class TrainExplicitEvalModel(TrainEvalModel):
    num_pool_samples: int
    num_training_samples: int
    num_validation_samples: int
    num_patience_epochs: int
    max_epochs: int
    training_dataset: torch.utils.data.Dataset
    eval_dataset: torch.utils.data.Dataset
    validation_loader: torch.utils.data.DataLoader
    training_batch_size: int
    model_optimizer_factory: ModelOptimizerFactory

    def __call__(self, *, training_log, device):
        # TODO: support one_hot!
        # TODO: different seed needed!
        train_eval_dataset = torch.utils.data.ConcatDataset([self.training_dataset, self.eval_dataset])
        train_eval_loader = torch.utils.data.DataLoader(
            train_eval_dataset, batch_size=self.training_batch_size, drop_last=True, shuffle=True
        )

        eval_model_optimizer = self.model_optimizer_factory.create_model_optimizer()

        loss = torch.nn.NLLLoss()

        train(
            model=eval_model_optimizer.model,
            optimizer=eval_model_optimizer.optimizer,
            loss=loss,
            validation_loss=loss,
            training_samples=self.num_training_samples,
            validation_samples=self.num_validation_samples,
            train_loader=train_eval_loader,
            validation_loader=self.validation_loader,
            patience=self.num_patience_epochs,
            max_epochs=self.max_epochs,
            device=device,
            training_log=training_log,
        )

        return TrainedMCDropoutModel(num_samples=self.num_pool_samples, model=eval_model_optimizer.model)