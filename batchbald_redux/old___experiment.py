# AUTOGENERATED! DO NOT EDIT! File to edit: 09z_old__experiment.ipynb (unless otherwise specified).

__all__ = ['Experiment', 'configs']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass
from typing import Type, Union

import torch
import torch.utils.data
from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments
from torch import nn
from torch.utils.data import Dataset

import batchbald_redux.acquisition_functions as acquisition_functions
import batchbald_redux.acquisition_functions.bald
from .acquisition_functions import (
    CandidateBatchComputer,
    EvalModelBatchComputer,
)
from .active_learning import ActiveLearningData
from .black_box_model_training import evaluate
from .dataset_challenges import (
    create_repeated_MNIST_dataset,
    get_base_dataset_index,
    get_target,
)
from .di import DependencyInjection
from .models import MnistModelTrainer
from .experiment_data import ExperimentData, StandardExperimentDataConfig

# Cell

from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
)
from .trained_model import ModelTrainer

# Cell


@dataclass
class Experiment:
    seed: int = 1337
    acquisition_size: int = 5
    max_training_set: int = 300
    num_pool_samples: int = 20
    num_validation_samples: int = 20
    num_training_samples: int = 1
    num_patience_epochs: int = 5 * 4
    max_training_epochs: int = 30 * 4
    training_batch_size: int = 64
    device: str = "cuda"
    validation_set_size: int = 2048
    initial_set_size: int = 20
    min_samples_per_epoch: int = 1024
    repeated_mnist_repetitions: int = 1
    add_dataset_noise: bool = False
    acquisition_function: Union[
        Type[CandidateBatchComputer], Type[EvalModelBatchComputer]
    ] = batchbald_redux.acquisition_functions.bald.BALD
    train_eval_model_factory: Type[TrainEvalModel] = TrainSelfDistillationEvalModel
    model_trainer_factory: Type[ModelTrainer] = MnistModelTrainer
    acquisition_function_args: dict = None
    temperature: float = 0.0

    def load_dataset(self) -> (ActiveLearningData, Dataset, Dataset):
        experiment_data_config = StandardExperimentDataConfig(id_dataset_name="MNIST",
                                                              id_repetitions=self.repeated_mnist_repetitions,
                                                              initial_training_set_size=self.initial_set_size,
                                                              evaluation_set_size=0,
                                                              validation_split_random_state=0,
                                                              validation_set_size=self.validation_set_size,
                                                              add_dataset_noise=self.add_dataset_noise, ood_dataset_config=None,
                                                              device=self.device)
        experiment_data = experiment_data_config.load()

        return experiment_data.active_learning, experiment_data.validation_dataset, experiment_data.test_dataset

    # Simple Dependency Injection
    def create_acquisition_function(self):
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.acquisition_function)

    def create_train_eval_model(self, runtime_config) -> TrainEvalModel:
        config = {**vars(self), **runtime_config}
        di = DependencyInjection(config, [])
        return di.create_dataclass_type(self.train_eval_model_factory)

    def create_model_trainer(self) -> ModelTrainer:
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.model_trainer_factory)

    def run(self, store):
        torch.manual_seed(self.seed)

        # Active Learning setup
        active_learning_data, validation_dataset, test_dataset = self.load_dataset()
        store["dataset_info"] = dict(training=repr(active_learning_data.base_dataset), test=repr(test_dataset))

        model_trainer = self.create_model_trainer()

        train_loader = model_trainer.get_train_dataloader(active_learning_data.training_dataset)
        pool_loader = model_trainer.get_evaluation_dataloader(active_learning_data.pool_dataset)
        validation_loader = model_trainer.get_evaluation_dataloader(validation_dataset)
        test_loader = model_trainer.get_evaluation_dataloader(test_dataset)

        store["active_learning_steps"] = []
        active_learning_steps = store["active_learning_steps"]

        acquisition_function = self.create_acquisition_function()

        # Active Training Loop
        while True:
            training_set_size = len(active_learning_data.training_dataset)
            print(f"Training set size {training_set_size}:")

            # iteration_log = dict(training={}, pool_training={}, evaluation_metrics=None, acquisition=None)
            active_learning_steps.append({})
            iteration_log = active_learning_steps[-1]

            iteration_log["training"] = {}
            trained_model = model_trainer.get_trained(train_loader=train_loader, train_augmentations=None,
                                                      validation_loader=validation_loader,
                                                      log=iteration_log["training"])

            evaluation_metrics = evaluate(model=trained_model, num_samples=self.num_validation_samples,
                                          loader=test_loader, device=self.device, storage_device="cpu")

            iteration_log["evaluation_metrics"] = evaluation_metrics
            print(f"Perf after training {evaluation_metrics}")

            if training_set_size >= self.max_training_set:
                print("Done.")
                break

            if isinstance(acquisition_function, CandidateBatchComputer):
                candidate_batch = acquisition_function.compute_candidate_batch(trained_model, pool_loader, self.device)
            elif isinstance(acquisition_function, EvalModelBatchComputer):
                train_eval_model = self.create_train_eval_model(
                    dict(
                        model_trainer=model_trainer,
                        training_dataset=active_learning_data.training_dataset,
                        eval_dataset=active_learning_data.pool_dataset,
                        validation_loader=validation_loader,
                        trained_model=trained_model,
                    )
                )

                iteration_log["eval_training"] = {}
                trained_eval_model = train_eval_model(training_log=iteration_log["eval_training"], device=self.device)

                candidate_batch = acquisition_function.compute_candidate_batch(
                    trained_model, trained_eval_model, pool_loader, device=self.device
                )
            else:
                raise ValueError(f"Unknown acquisition function {acquisition_function}!")

            candidate_global_indices = [
                get_base_dataset_index(active_learning_data.pool_dataset, index).index
                for index in candidate_batch.indices
            ]
            candidate_labels = [
                get_target(active_learning_data.base_dataset, index).item() for index in candidate_global_indices
            ]

            iteration_log["acquisition"] = dict(
                indices=candidate_global_indices, labels=candidate_labels, scores=candidate_batch.scores
            )

            active_learning_data.acquire(candidate_batch.indices)

            ls = ", ".join(f"{label} ({score:.4})" for label, score in zip(candidate_labels, candidate_batch.scores))
            print(f"Acquiring (label, score)s: {ls}")

# Cell

configs = [
    Experiment(
        seed=seed + 315,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        repeated_mnist_repetitions=repeated_mnist_repetitions,
        add_dataset_noise=repeated_mnist_repetitions > 1,
        temperature=temperature,
        max_training_set=150,
    )
    for seed in range(5)
    for acquisition_function in [
        batchbald_redux.acquisition_functions.bald.SoftmaxBALD,
    ]
    for temperature in [1 / 32, 1 / 64, 1 / 128, 1 / 256]
    for acquisition_size in [5]
    for num_pool_samples in [100]
    for repeated_mnist_repetitions in [2]
]

if not is_run_from_ipython() and __name__ == "__main__":
    for job_id, store in embedded_experiments(__file__, len(configs)):
        config = configs[job_id]
        config.seed += job_id
        print(config)
        store["config"] = dataclasses.asdict(config)
        store["log"] = {}

        try:
            config.run(store=store)
        except Exception:
            store["exception"] = traceback.format_exc()
            raise