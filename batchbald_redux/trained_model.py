# AUTOGENERATED! DO NOT EDIT! File to edit: 07a_trained_model.ipynb (unless otherwise specified).

__all__ = ['TrainedModel', 'TrainedBayesianModel', 'TrainedBayesianEnsemble', 'ModelTrainer',
           'BayesianEnsembleModelTrainer']

# Internal Cell
from dataclasses import dataclass
from typing import List, Optional

import torch.nn
from torch.nn import Module
from torch.utils.data import DataLoader, Dataset

from .consistent_mc_dropout import BayesianModule

# Cell


@dataclass
class TrainedModel:
    """Evaluate a trained model."""

    def get_log_probs_N_K_C_labels_N(self, loader: DataLoader, num_samples: int, device: object):
        raise NotImplementedError()

    def get_log_probs_N_K_C(self, loader: DataLoader, num_samples: int, device: object):
        return self.get_log_probs_N_K_C_labels_N(loader, num_samples, device)[0]


@dataclass
class TrainedBayesianModel(TrainedModel):
    model: BayesianModule

    def get_log_probs_N_K_C_labels_N(self, loader: DataLoader, num_samples: int, device: object):
        log_probs_N_K_C, labels_B = self.model.get_predictions_labels(
            num_samples=num_samples,
            loader=loader,
            device=device,
        )

        # NOTE: this wastes memory bandwidth, but is needed for ensembles where more than one model might not fit
        # into memory.
        self.model.to("cpu")

        return log_probs_N_K_C, labels_B


@dataclass
class TrainedBayesianEnsemble(TrainedModel):
    models: List[TrainedModel]

    def get_log_probs_N_K_C_labels_N(self, loader: DataLoader, num_samples: int, device: object):
        ensemble_size = len(self.models)
        member_num_samples = (num_samples + ensemble_size - 1) // ensemble_size

        ensemble_log_probs_N_K_C = []
        ensemble_labels_B = None

        for model in self.models:
            log_probs_N_K_C, labels_B = model.get_log_probs_N_K_C_labels_N(loader=loader, num_samples=member_num_samples, device=device)

            ensemble_log_probs_N_K_C += [log_probs_N_K_C]
            if ensemble_labels_B is not None:
                assert torch.all(ensemble_labels_B == labels_B)
            else:
                ensemble_labels_B = labels_B

        ensemble_log_probs_N_K_C = torch.cat(ensemble_log_probs_N_K_C, dim=1)
        return ensemble_log_probs_N_K_C, ensemble_labels_B


class ModelTrainer:
    def get_train_dataloader(self, dataset: Dataset):
        raise NotImplementedError

    # test|validation|evaluation
    def get_evaluation_dataloader(self, dataset: Dataset):
        raise NotImplementedError

    def get_trained(self, *, train_loader: DataLoader, train_augmentations: Optional[Module],
                    validation_loader: DataLoader, log) -> TrainedModel:
        raise NotImplementedError

    def get_distilled(self, *, prediction_loader: DataLoader, train_augmentations: Optional[Module],
                      validation_loader: DataLoader, log) -> TrainedModel:
        raise NotImplementedError


@dataclass
class BayesianEnsembleModelTrainer(ModelTrainer):
    model_trainer: ModelTrainer
    ensemble_size: int

    def get_trained(self, *, train_loader: DataLoader, train_augmentations: Optional[Module],
                    validation_loader: DataLoader, log) -> TrainedBayesianEnsemble:
        models = []

        for i in range(self.ensemble_size):
            log[i] = {}
            model = self.model_trainer.get_trained(train_loader=train_loader, train_augmentations=train_augmentations,
                                                   validation_loader=validation_loader, log=log[i])
            models += [model]

        return TrainedBayesianEnsemble(models)

    def get_distilled(self, *, prediction_loader: DataLoader, train_augmentations: Optional[Module],
                      validation_loader: DataLoader, log) -> TrainedBayesianEnsemble:
        models = []
        for i in range(self.ensemble_size):
            log[i] = {}
            model = self.model_trainer.get_distilled(prediction_loader=prediction_loader,
                                                     train_augmentations=train_augmentations,
                                                     validation_loader=validation_loader, log=log[i])
            models += [model]
        return TrainedBayesianEnsemble(models)