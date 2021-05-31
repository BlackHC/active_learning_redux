# AUTOGENERATED! DO NOT EDIT! File to edit: 09h_experiment_cifar10.ipynb (unless otherwise specified).

__all__ = ['ExperimentData', 'ExperimentDataConfig', 'load_experiment_data', 'Experiment', 'configs']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass, field
from typing import Type, Union

import torch
import torch.utils.data
from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments
from torch.utils.data import Dataset

import batchbald_redux.acquisition_functions as acquisition_functions
from .acquisition_functions import (
    CandidateBatchComputer,
    EvalCandidateBatchComputer,
)
from .active_learning import ActiveLearningData, RandomFixedLengthSampler
from .black_box_model_training import evaluate, train, train_with_schedule
from .dataset_challenges import (
    NamedDataset,
    create_repeated_MNIST_dataset,
    get_balanced_sample_indices,
    get_base_dataset_index,
    get_target, AdditiveGaussianNoise, AliasDataset, get_balanced_sample_indices_by_class,
)
from .datasets import get_dataset
from .datasets import train_validation_split
from .di import DependencyInjection
from .fast_mnist import FastMNIST
from .model_optimizer_factory import ModelOptimizerFactory
from .resnet_models import Cifar10BayesianResnetFactory
from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
    TrainSelfDistillationEvalModelWithSchedule
)
from .trained_model import TrainedMCDropoutModel

# Cell

@dataclass
class ExperimentData:
    active_learning: ActiveLearningData
    augmentation_node: AliasDataset
    unaugmented_train_dataset: Dataset
    augmented_train_dataset: Dataset
    validation_dataset: Dataset
    test_dataset: Dataset
    evaluation_dataset: Dataset
    initial_training_set_indices: [int]
    evaluation_set_indices: [int]

    def toggle_augmentations(self, augment: bool):
        if augment:
            self.augmentation_node.dataset = self.augmented_train_dataset
        else:
            self.augmentation_node.dataset = self.unaugmented_train_dataset


@dataclass
class ExperimentDataConfig:
    id_dataset_name: str
    initial_training_set_size: int
    validation_set_size: int
    evaluation_set_size: int
    id_repetitions: float
    add_dataset_noise: bool
    validation_split_random_state: int

    device: str

    def load(self) -> ExperimentData:
        return load_experiment_data(
            id_dataset_name=self.id_dataset_name,
            initial_training_set_size=self.initial_training_set_size,
            validation_set_size=self.validation_set_size,
            evaluation_set_size=self.evaluation_set_size,
            id_repetitions=self.id_repetitions,
            add_dataset_noise=self.add_dataset_noise,
            validation_split_random_state=self.validation_split_random_state,
            device=self.device,
        )


def load_experiment_data(
    *,
    id_dataset_name: str,
    initial_training_set_size: int,
    validation_set_size: int,
    evaluation_set_size: int,
    id_repetitions: float,
    add_dataset_noise: bool,
    validation_split_random_state: int,
    device: str,
) -> ExperimentData:
    split_dataset = get_dataset(id_dataset_name, root="data", train_augmentation=True, validation_set_size=validation_set_size,
                                validation_split_random_state=validation_split_random_state, normalize_like_cifar10=True)
    unaugmented_split_dataset = get_dataset(id_dataset_name, root="data", train_augmentation=True, validation_set_size=validation_set_size,
                                validation_split_random_state=validation_split_random_state, normalize_like_cifar10=True)

    augmentation_node = AliasDataset(split_dataset.train, "Augmentation Node")
    train_dataset=augmentation_node

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
        augmentation_node=augmentation_node,
        augmented_train_dataset=split_dataset.train,
        unaugmented_train_dataset=unaugmented_split_dataset.train,
        validation_dataset=split_dataset.validation,
        test_dataset=split_dataset.test,
        evaluation_dataset=evaluation_dataset,
        initial_training_set_indices=initial_training_set_indices,
        evaluation_set_indices=evaluation_set_indices,
    )

# Cell

@dataclass
class Experiment:
    seed: int

    id_dataset_name: str = "CIFAR-10"
    initial_training_set_size: int = 1000
    validation_set_size: int = 5000
    evaluation_set_size: int = 0
    id_repetitions: float = 1
    add_dataset_noise: bool = False
    validation_split_random_state: int = 0

    acquisition_size: int = 5
    max_training_set: int = 300
    num_pool_samples: int = 20
    num_validation_samples: int = 20
    num_training_samples: int = 1
    max_training_epochs: int = 60
    training_batch_size: int = 128
    device: str = "cuda"
    min_samples_per_epoch: int = 5056
    patience_schedule: [int] = (3, 3, 3)
    factor_schedule: [int] = (0.1,)
    acquisition_function: Union[
        Type[CandidateBatchComputer], Type[EvalCandidateBatchComputer]
    ] = acquisition_functions.BALD
    train_eval_model: Type[TrainEvalModel] = TrainSelfDistillationEvalModelWithSchedule
    model_optimizer_factory: Type[ModelOptimizerFactory] = Cifar10BayesianResnetFactory
    acquisition_function_args: dict = None
    temperature: float = 0.0
    prefer_accuracy: bool = False

    def load_experiment_data(self) -> ExperimentData:
        di = DependencyInjection(vars(self))
        edc: ExperimentDataConfig = di.create_dataclass_type(ExperimentDataConfig)
        return edc.load()

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

        # Active Learning setup
        data = self.load_experiment_data()
        store["dataset_info"] = dict(training=repr(data.active_learning.base_dataset), test=repr(data.test_dataset))
        store["initial_training_set_indices"] = data.initial_training_set_indices
        store["evaluation_set_indices"] = data.evaluation_set_indices

        train_loader = torch.utils.data.DataLoader(
            data.active_learning.training_dataset,
            batch_size=self.training_batch_size,
            sampler=RandomFixedLengthSampler(data.active_learning.training_dataset, self.min_samples_per_epoch),
            drop_last=True,
        )
        pool_loader = torch.utils.data.DataLoader(
            data.active_learning.pool_dataset, batch_size=128, drop_last=False, shuffle=False
        )

        validation_loader = torch.utils.data.DataLoader(data.validation_dataset, batch_size=512, drop_last=False)
        test_loader = torch.utils.data.DataLoader(data.test_dataset, batch_size=512, drop_last=False)

        store["active_learning_steps"] = []
        active_learning_steps = store["active_learning_steps"]

        acquisition_function = self.create_acquisition_function()

        # Active Training Loop
        while True:
            training_set_size = len(data.active_learning.training_dataset)
            print(f"Training set size {training_set_size}:")

            # iteration_log = dict(training={}, pool_training={}, evaluation_metrics=None, acquisition=None)
            active_learning_steps.append({})
            iteration_log = active_learning_steps[-1]

            iteration_log["training"] = {}

            model_optimizer = self.model_optimizer_factory().create_model_optimizer()

            data.toggle_augmentations(True)

            if training_set_size > 0:
                train_with_schedule(
                    model=model_optimizer.model,
                    optimizer=model_optimizer.optimizer,
                    training_samples=self.num_training_samples,
                    validation_samples=self.num_validation_samples,
                    train_loader=train_loader,
                    validation_loader=validation_loader,
                    patience_schedule = self.patience_schedule,
                    factor_schedule = self.factor_schedule,
                    max_epochs=self.max_training_epochs,
                    device=self.device,
                    training_log=iteration_log["training"],
                    prefer_accuracy=self.prefer_accuracy
                )

            data.toggle_augmentations(False)

            evaluation_metrics = evaluate(
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

            trained_model = TrainedMCDropoutModel(num_samples=self.num_pool_samples, model=model_optimizer.model)

            if isinstance(acquisition_function, CandidateBatchComputer):
                candidate_batch = acquisition_function.compute_candidate_batch(trained_model, pool_loader, self.device)
            elif isinstance(acquisition_function, EvalCandidateBatchComputer):
                current_max_epochs = len(iteration_log["training"]["epochs"])

                if self.evaluation_set_size:
                    eval_dataset = data.evaluation_dataset
                else:
                    eval_dataset = data.active_learning.pool_dataset

                train_eval_model = self.create_train_eval_model(
                    dict(
                        max_epochs=current_max_epochs + 2,
                        training_dataset=data.active_learning.training_dataset,
                        eval_dataset=eval_dataset,
                        validation_loader=validation_loader,
                        trained_model=trained_model,
                        data=data,
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
                get_base_dataset_index(data.active_learning.pool_dataset, index).index
                for index in candidate_batch.indices
            ]
            candidate_labels = [
                get_target(data.active_learning.pool_dataset, index).item() for index in candidate_batch.indices
            ]

            iteration_log["acquisition"] = dict(
                indices=candidate_global_indices, labels=candidate_labels, scores=candidate_batch.scores
            )

            data.active_learning.acquire(candidate_batch.indices)

            ls = ", ".join(f"{label} ({score:.4})" for label, score in zip(candidate_labels, candidate_batch.scores))
            print(f"Acquiring (label, score)s: {ls}")

# Cell

configs = [
    Experiment(
        seed=seed + 7893,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        initial_training_set_size=1000,
        evaluation_set_size=5000,
        max_training_set=30000,
        temperature=8
    )
    for seed in range(5)
    for acquisition_function in [
        acquisition_functions.TemperedBALD,
        acquisition_functions.BALD,
        acquisition_functions.EvalBALD,
        acquisition_functions.TemperedEvalBALD,
        acquisition_functions.Random,
    ]
    for acquisition_size in [250]
    for num_pool_samples in [100]
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