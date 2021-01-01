# AUTOGENERATED! DO NOT EDIT! File to edit: 09a_bald_ical_experiment.ipynb (unless otherwise specified).

__all__ = ['PredictionDataset', 'Experiment']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass

import blackhc.project.script
import torch
import torch.utils.data
from blackhc.project.experiment import embedded_experiments
from torch.utils.data import Dataset

from .active_learning import (
    ActiveLearningData,
    RandomFixedLengthSampler,
    get_balanced_sample_indices,
    get_base_indices,
)
from .batchbald import get_batchbaldical_batch
from .black_box_model_training import evaluate, get_predictions, train
from .consistent_mc_dropout import GeometricMeanPrediction, SamplerModel
from .example_models import BayesianMNISTCNN
from .repeated_mnist import create_repeated_MNIST_dataset

# Cell


class PredictionDataset(torch.utils.data.Dataset):
    dataset: torch.utils.data.Dataset
    predictions: torch.Tensor

    def __init__(self, dataset, predictions):
        assert len(dataset) == predictions.shape[0], f"{len(dataset)} == {predictions.shape[0]}"

        self.dataset = dataset
        self.predictions = predictions

    def __getitem__(self, index):
        x, y = self.dataset[index]
        p = self.predictions[index]
        return x, p

    def __len__(self):
        return len(self.dataset)

# Cell


@dataclass
class Experiment:
    seed: int = 1337
    acquisition_size: int = 5
    max_training_set: int = 300
    num_pool_samples: int = 20
    num_eval_samples: int = 4
    num_training_samples: int = 1
    num_patience_epochs: int = 3
    max_training_epochs: int = 10
    device = "cuda"
    validation_set_size: int = 4096
    initial_set_size: int = 20
    samples_per_epoch: int = 4096 * 6
    repeated_mnist_repetitions: int = 4
    add_dataset_noise: bool = True

    def load_dataset(self) -> (ActiveLearningData, Dataset, Dataset):
        train_dataset, test_dataset = create_repeated_MNIST_dataset(
            num_repetitions=self.repeated_mnist_repetitions, add_noise=self.add_dataset_noise
        )
        active_learning_data = ActiveLearningData(train_dataset)

        validation_dataset = active_learning_data.extract_dataset_from_pool(self.validation_set_size)

        return active_learning_data, validation_dataset, test_dataset

    def new_model(self):
        return BayesianMNISTCNN()

    def new_optimizer(self, model):
        return torch.optim.Adam(model.parameters(), weight_decay=5e-4)

    def get_candidate_batch(self, model, pool_model, pool_loader):
        # Evaluate pool set
        bald_model = SamplerModel(model, self.num_pool_samples)
        normal_log_probs_N_K_C = get_predictions(model=bald_model, loader=pool_loader, device=self.device)

        bald_pool_model = SamplerModel(pool_model, self.num_pool_samples)
        pool_log_probs_N_K_C = get_predictions(model=bald_pool_model, loader=pool_loader, device=self.device)

        # Evaluate BALD scores
        candidate_batch = get_batchbaldical_batch(
            normal_log_probs_N_K_C,
            pool_log_probs_N_K_C,
            batch_size=self.acquisition_size,
            num_samples=100000,
            dtype=torch.double,
            device=self.device,
        )
        return candidate_batch

    def train_pool_model(self, *, model, train_pool_dataset, train_pool_loader, validation_loader, num_epochs, training_log):
        eval_model = GeometricMeanPrediction(SamplerModel(model, self.num_eval_samples))
        log_probs_N_C = get_predictions(model=eval_model, loader=train_pool_loader, device=self.device).cpu()

        train_pool_prediction_dataset = PredictionDataset(train_pool_dataset, log_probs_N_C)
        train_pool_prediction_loader = torch.utils.data.DataLoader(
            train_pool_prediction_dataset, batch_size=64, drop_last=True, shuffle=True
        )

        pool_model = self.new_model()
        pool_optimizer = self.new_optimizer(pool_model)

        loss = torch.nn.KLDivLoss(log_target=True, reduction="batchmean")

        train(
            model=pool_model,
            optimizer=pool_optimizer,
            loss=loss,
            validation_loss=torch.nn.NLLLoss(),
            training_samples=self.num_training_samples,
            validation_samples=self.num_eval_samples,
            train_loader=train_pool_prediction_loader,
            validation_loader=validation_loader,
            patience=self.num_patience_epochs,
            max_epochs=num_epochs,
            device=self.device,
            training_log=training_log,
        )
        # print(training_log)

        return pool_model

    def run(self, store):
        store["hparams"] = dataclasses.asdict(self)

        torch.manual_seed(self.seed)

        # Active Learning setup
        active_learning_data, validation_dataset, test_dataset = self.load_dataset()

        # initial_training_set_indices = active_learning_data.get_random_pool_indices(self.initial_set_size)
        initial_training_set_indices = get_balanced_sample_indices(
            active_learning_data.dataset, 10, self.initial_set_size // 10
        )
        active_learning_data.acquire(initial_training_set_indices)

        store["initial_training_set_indices"] = initial_training_set_indices

        train_loader = torch.utils.data.DataLoader(
            active_learning_data.training_dataset,
            batch_size=64,
            sampler=RandomFixedLengthSampler(active_learning_data.training_dataset, self.samples_per_epoch),
            drop_last=True,
        )
        validation_loader = torch.utils.data.DataLoader(active_learning_data.pool_dataset, batch_size=64, drop_last=False)

        validation_loader = torch.utils.data.DataLoader(validation_dataset, batch_size=64, drop_last=False)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, drop_last=False)

        store["active_learning_steps"] = []
        active_learning_steps = store["active_learning_steps"]

        # Active Training Loop
        while True:
            training_set_size = len(active_learning_data.training_dataset)
            print(f"Training set size {training_set_size}:")

            # iteration_log = dict(training={}, pool_training={}, evalution_metrics=None, acquisition=None)
            active_learning_steps.append({})
            iteration_log = active_learning_steps[-1]

            iteration_log["training"] = {}

            model = self.new_model()
            optimizer = self.new_optimizer(model)
            train(
                model=model,
                optimizer=optimizer,
                training_samples=self.num_training_samples,
                validation_samples=self.num_eval_samples,
                train_loader=train_loader,
                validation_loader=validation_loader,
                patience=self.num_patience_epochs,
                max_epochs=self.max_training_epochs,
                device=self.device,
                training_log=iteration_log["training"],
            )

            evaluation_metrics = evaluate(
                model=model, num_samples=self.num_eval_samples, loader=test_loader, device=self.device
            )
            iteration_log["evalution_metrics"] = evaluation_metrics
            print(f"Perf after training {evaluation_metrics}")

            if training_set_size >= self.max_training_set:
                print("Done.")
                break

            num_epochs = iteration_log["training"]["best_epoch"]

            train_pool_dataset = torch.utils.data.ConcatDataset(
                [active_learning_data.training_dataset, active_learning_data.pool_dataset]
            )
            train_pool_loader = torch.utils.data.DataLoader(train_pool_dataset, batch_size=64, drop_last=False)

            iteration_log["pool_training"] = {}
            pool_model = self.train_pool_model(
                model=model,
                train_pool_dataset=train_pool_dataset,
                train_pool_loader=train_pool_loader,
                validation_loader=validation_loader,
                num_epochs=num_epochs,
                training_log=iteration_log["pool_training"],
            )

            candidate_batch = self.get_candidate_batch(model, pool_model, validation_loader)

            candidate_global_indices = get_base_indices(active_learning_data.pool_dataset, candidate_batch.indices)
            candidate_labels = [
                active_learning_data.dataset[index][1].item() for index in candidate_global_indices
            ]

            iteration_log["acquisition"] = dict(
                indices=candidate_global_indices, labels=candidate_labels, scores=candidate_batch.scores
            )

            active_learning_data.acquire(candidate_batch.indices)

            ls = ", ".join(f"{label} ({score:.4})" for label, score in zip(candidate_labels, candidate_batch.scores))
            print(f"Acquiring (label, score)s: {ls}")

# Cell

if __name__ == "__main__":
    configs = [Experiment(seed=seed) for seed in range(5)]

    for job_id, store in embedded_experiments(__file__, len(configs)):
        config = configs[job_id]
        config.seed += job_id
        print(config)
        store["config"] = dataclasses.asdict(config)
        store["log"] = {}

        try:
            config.run(store=store["log"])
        except Exception:
            store["exception"] = traceback.format_exc()
            raise