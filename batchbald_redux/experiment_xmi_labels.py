# AUTOGENERATED! DO NOT EDIT! File to edit: 09f_experiment_xmi_labels.ipynb (unless otherwise specified).

__all__ = ['mnist_initial_samples', 'Experiment', 'configs']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass
from typing import Type, Union

import torch
import torch.utils.data
from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments
from torch.utils.data import Dataset

import batchbald_redux.acquisition_functions as acquisition_functions
from .acquisition_functions import (
    CandidateBatchComputer,
    EvalModelBatchComputer,
)
from .active_learning import ActiveLearningData, RandomFixedLengthSampler
from .black_box_model_training import evaluate_old, train
from .dataset_challenges import (
    NamedDataset,
    create_repeated_MNIST_dataset,
    get_base_dataset_index,
    get_target,
)
from .di import DependencyInjection
from .fast_mnist import FastMNIST
from .model_optimizer_factory import ModelOptimizerFactory
from .models import MnistOptimizerFactory

# Cell

# From the BatchBALD Repo
from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
)
from .trained_model import TrainedBayesianModel

mnist_initial_samples = [
    38043,
    40091,
    17418,
    2094,
    39879,
    3133,
    5011,
    40683,
    54379,
    24287,
    9849,
    59305,
    39508,
    39356,
    8758,
    52579,
    13655,
    7636,
    21562,
    41329,
]

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
    validation_set_size: int = 1024
    initial_set_size: int = 20
    min_samples_per_epoch: int = 1024
    repeated_mnist_repetitions: int = 1
    add_dataset_noise: bool = False
    acquisition_function: Union[
        Type[CandidateBatchComputer], Type[EvalModelBatchComputer]
    ] = acquisition_functions.BALD
    train_eval_model: TrainEvalModel = TrainSelfDistillationEvalModel
    model_optimizer_factory: Type[ModelOptimizerFactory] = MnistOptimizerFactory
    acquisition_function_args: dict = None
    temperature: float = 0.0

    def load_dataset(self, initial_training_set_indices) -> (ActiveLearningData, Dataset, Dataset):
        train_dataset = NamedDataset(
            FastMNIST("data", train=True, download=True, device=self.device), "FastMNIST (train)"
        )
        #train_predictions = torch.load("./data/mnist_train_predictions.pt", map_location=self.device)

        # If we over-sample the train set, we do so after picking the initial train set to avoid duplicates.
        if self.repeated_mnist_repetitions > 1:
            train_dataset = train_dataset * self.repeated_mnist_repetitions

        #train_dataset = train_dataset.override_targets(targets=train_predictions.argmax(dim=1))

        if self.add_dataset_noise:
            train_dataset = AdditiveGaussianNoise(train_dataset, 0.1)

        active_learning_data = ActiveLearningData(train_dataset)

        active_learning_data.acquire(initial_training_set_indices)

        validation_dataset = active_learning_data.extract_dataset_from_pool(self.validation_set_size)
        validation_dataset = NamedDataset(
            validation_dataset, f"FastMNIST (validation, {len(validation_dataset)} samples)"
        )

        test_dataset = FastMNIST("data", train=False, device=None)
        test_dataset = NamedDataset(test_dataset, f"FastMNIST (test, {len(test_dataset)} samples)")

        return active_learning_data, validation_dataset, test_dataset

    # Simple Dependency Injection
    def create_acquisition_function(self):
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.acquisition_function)

    def create_train_eval_model(self, runtime_config) -> TrainEvalModel:
        config = {**vars(self), **runtime_config}
        di = DependencyInjection(config, [])
        return di.create_dataclass_type(self.train_eval_model)

    def run(self, store):
        torch.manual_seed(self.seed)

        if self.initial_set_size == len(mnist_initial_samples):
            initial_training_set_indices = mnist_initial_samples
        elif self.initial_set_size == 0:
            initial_training_set_indices = []
        else:
            raise Exception(f"initial_set_size {initial_set_size} not supported here!")

        store["initial_training_set_indices"] = initial_training_set_indices

        # Active Learning setup
        active_learning_data, validation_dataset, test_dataset = self.load_dataset(initial_training_set_indices)
        store["dataset_info"] = dict(training=repr(active_learning_data.base_dataset), test=repr(test_dataset))

        # initial_training_set_indices = active_learning_data.get_random_pool_indices(self.initial_set_size)
        # initial_training_set_indices = get_balanced_sample_indices(
        #     active_learning_data.pool_dataset, 10, self.initial_set_size // 10
        # )

        train_loader = torch.utils.data.DataLoader(
            active_learning_data.training_dataset,
            batch_size=64,
            sampler=RandomFixedLengthSampler(active_learning_data.training_dataset, self.min_samples_per_epoch),
            drop_last=True,
        )
        pool_loader = torch.utils.data.DataLoader(
            active_learning_data.pool_dataset, batch_size=128, drop_last=False, shuffle=False
        )

        validation_loader = torch.utils.data.DataLoader(validation_dataset, batch_size=128, drop_last=False)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=128, drop_last=False)

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

            model_optimizer = self.model_optimizer_factory().create_model_optimizer()

            if training_set_size > 0:
                train(
                    model=model_optimizer.model,
                    optimizer=model_optimizer.optimizer,
                    training_samples=self.num_training_samples,
                    validation_samples=self.num_validation_samples,
                    train_loader=train_loader,
                    validation_loader=validation_loader,
                    patience=self.num_patience_epochs,
                    max_epochs=self.max_training_epochs,
                    device=self.device,
                    training_log=iteration_log["training"],
                )

            evaluation_metrics = evaluate_old(
                model=model_optimizer.model,
                num_samples=self.num_validation_samples,
                loader=test_loader,
                device=self.device,
            )
            iteration_log["evaluation_metrics"] = evaluation_metrics
            print(f"Perf after training {evaluation_metrics}")

            if training_set_size >= self.max_training_set:
                print("Done.")
                break

            trained_model = TrainedBayesianModel(model=model_optimizer.model)

            if isinstance(acquisition_function, CandidateBatchComputer):
                candidate_batch = acquisition_function.compute_candidate_batch(trained_model, pool_loader, self.device)
            elif isinstance(acquisition_function, EvalModelBatchComputer):
                current_max_epochs = iteration_log["training"]["best_epoch"]

                train_eval_model = self.create_train_eval_model(
                    dict(
                        max_epochs=current_max_epochs,
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
        seed=seed,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=200,
        temperature=8,
    )
    for seed in range(5)
    for acquisition_function in [
        acquisition_functions.BALD,
        #acquisition_functions.TemperedBALD,
        acquisition_functions.CoreSetBALD,
        #acquisition_functions.TemperedCoreSetBALD,
    ]
    for acquisition_size in [1]
    for num_pool_samples in [100]
] + [
    Experiment(
        seed=seed,
        acquisition_function=acquisition_functions.Random,
        acquisition_size=10,
        num_pool_samples=1,
        max_training_set=200,
    )
    for seed in range(10)
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