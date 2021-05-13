# AUTOGENERATED! DO NOT EDIT! File to edit: 09d_uniform_target_ood_experiment.ipynb (unless otherwise specified).

__all__ = ['ExperimentData', 'UniformTargetOodExperiment', 'configs']

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
    EvalCandidateBatchComputer,
)
from .active_learning import ActiveLearningData, RandomFixedLengthSampler
from .black_box_model_training import evaluate, train
from .dataset_challenges import (
    AdditiveGaussianNoise,
    AliasDataset,
    NamedDataset,
    get_balanced_sample_indices,
    get_base_dataset_index,
    get_target,
    get_balanced_sample_indices_by_class,
)
from .datasets import train_validation_split
from .di import DependencyInjection
from .fast_mnist import FastFashionMNIST, FastMNIST
from .model_optimizer_factory import ModelOptimizerFactory
from .models import MnistOptimizerFactory
from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
)
from .trained_model import TrainedMCDropoutModel

# Cell


@dataclass
class ExperimentData:
    active_learning: ActiveLearningData
    ood_dataset: NamedDataset
    validation_dataset: Dataset
    test_dataset: Dataset
    evaluation_dataset: Dataset
    initial_training_set_indices: [int]
    evaluation_set_indices: [int]


@dataclass
class UniformTargetOodExperiment:
    seed: int = 1337
    acquisition_size: int = 5
    max_training_set: int = 450
    num_pool_samples: int = 20
    num_validation_samples: int = 20
    num_training_samples: int = 1
    num_patience_epochs: int = 3
    max_training_epochs: int = 30
    training_batch_size: int = 64
    device: str = "cuda"
    validation_set_size: int = 1024
    evaluation_set_size: int = 10 * 10
    validation_split_random_state: int = 0
    initial_training_set_size: int = 20
    samples_per_epoch: int = 5056
    mnist_repetitions: float = 1
    ood_fmnist_repetitions: float = 1
    add_dataset_noise: bool = False
    acquisition_function: Union[
        Type[CandidateBatchComputer], Type[EvalCandidateBatchComputer]
    ] = acquisition_functions.BALD
    train_eval_model: TrainEvalModel = TrainSelfDistillationEvalModel
    model_optimizer_factory: Type[ModelOptimizerFactory] = MnistOptimizerFactory
    acquisition_function_args: dict = None
    temperature: float = 0.0

    def load_experiment_data(self) -> ExperimentData:
        # num_classes = 10, input_size = 28
        full_train_dataset = NamedDataset(
            FastMNIST("data", train=True, download=True, device=self.device), "FastMNIST (train)"
        )

        ood_dataset = FastFashionMNIST("data", train=True, download=True, device=self.device)
        ood_dataset = NamedDataset(ood_dataset, f"OoD Dataset ({len(ood_dataset)} samples)")
        if self.ood_fmnist_repetitions > 1:
            ood_dataset = ood_dataset * self.ood_fmnist_repetitions

        train_dataset, validation_dataset = train_validation_split(
            full_train_dataset=full_train_dataset,
            full_validation_dataset=full_train_dataset,
            train_labels=full_train_dataset.get_targets().cpu(),
            validation_set_size=self.validation_set_size,
            validation_split_random_state=self.validation_split_random_state,
        )

        train_dataset = AliasDataset(train_dataset, f"FastMNIST (train; {len(train_dataset)} samples)")
        validation_dataset = AliasDataset(
            validation_dataset, f"FastMNIST (validation; {len(validation_dataset)} samples)"
        )

        # If we reduce the train set, we need to do so before picking the initial train set.
        if self.mnist_repetitions < 1:
            train_dataset = train_dataset * self.mnist_repetitions

        num_classes = train_dataset.get_num_classes()
        initial_samples_per_class = self.initial_training_set_size / num_classes
        evaluation_set_samples_per_class = self.evaluation_set_size / num_classes
        samples_per_class = initial_samples_per_class + evaluation_set_samples_per_class
        balanced_samples_indices = get_balanced_sample_indices_by_class(
            train_dataset,
            num_classes=num_classes,
            samples_per_class=samples_per_class,
            seed=self.validation_split_random_state,
        )
        initial_training_set_indices = [
            idx for by_class in balanced_samples_indices for idx in by_class[:initial_samples_per_class]
        ]
        evaluation_set_indices = [
            idx for by_class in balanced_samples_indices for idx in by_class[initial_samples_per_class:]
        ]

        # If we over-sample the train set, we do so after picking the initial train set to avoid duplicates.
        if self.mnist_repetitions > 1:
            train_dataset = train_dataset * self.mnist_repetitions

        train_dataset = train_dataset.one_hot(device=self.device) + ood_dataset.uniform_target(device=self.device)

        if self.add_dataset_noise:
            train_dataset = AdditiveGaussianNoise(train_dataset, 0.1)

        test_dataset = FastMNIST("data", train=False, device=None)
        test_dataset = NamedDataset(test_dataset, f"FastMNIST (test, {len(test_dataset)} samples)")

        active_learning_data = ActiveLearningData(train_dataset)

        active_learning_data.acquire_base_indices(initial_training_set_indices)
        evaluation_dataset = active_learning_data.extract_dataset_from_base_indices(evaluation_set_indices)

        return ExperimentData(
            active_learning=active_learning_data,
            ood_dataset=ood_dataset,
            validation_dataset=validation_dataset,
            test_dataset=test_dataset,
            evaluation_dataset=evaluation_dataset,
            initial_training_set_indices=initial_training_set_indices,
            evaluation_set_indices=evaluation_set_indices,
        )

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
        data = self.load_dataset()
        store["dataset_info"] = dict(training=repr(data.active_learning.base_dataset), test=repr(data.test_dataset))
        store["initial_training_set_indices"] = data.initial_training_set_indices
        store["evaluation_set_indices"] = data.evaluation_set_indices

        train_loader = torch.utils.data.DataLoader(
            data.active_learning.training_dataset,
            batch_size=64,
            sampler=RandomFixedLengthSampler(data.active_learning.training_dataset, self.samples_per_epoch),
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

            loss = torch.nn.KLDivLoss(log_target=False, reduction="batchmean")

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
                loss=loss,
                validation_loss=torch.nn.NLLLoss(),
            )

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
                current_max_epochs = iteration_log["training"]["best_epoch"]

                if self.evaluation_set_size:
                    eval_dataset = data.active_learning.evaluation_dataset
                else:
                    eval_dataset = data.active_learning.pool_dataset

                train_eval_model = self.create_train_eval_model(
                    dict(
                        max_epochs=current_max_epochs,
                        training_dataset=data.active_learning.training_dataset,
                        eval_dataset=eval_dataset,
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

            candidate_global_dataset_indices = []
            candidate_labels = []
            for index in candidate_batch.indices:
                base_di = get_base_dataset_index(data.active_learning.pool_dataset, index)
                dataset_type = "ood" if base_di.dataset == data.ood_dataset else "id"
                candidate_global_dataset_indices.append((dataset_type, base_di.index))
                label = get_target(data.active_learning.pool_dataset, index)
                candidate_labels.append(label)

            iteration_log["acquisition"] = dict(
                indices=candidate_global_dataset_indices, labels=candidate_labels, scores=candidate_batch.scores
            )

            data.active_learning.acquire(candidate_batch.indices)

            print(candidate_batch)
            print(candidate_global_dataset_indices)

            ls = ", ".join(f"{label} ({score:.4})" for label, score in zip(candidate_labels, candidate_batch.scores))
            print(f"Acquiring (label, score)s: {ls}")

# Cell

configs = [
    UniformTargetOodExperiment(
        seed=seed,
        acquisition_function=acquisition_functions.TemperedEvalBALD,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        temperature=8,
    )
    for seed in range(5)
    for acquisition_size in [5, 10, 20, 50]
    for num_pool_samples in [100]
] + [
    UniformTargetOodExperiment(
        seed=seed,
        acquisition_function=acquisition_functions.Random,
        acquisition_size=5,
    )
    for seed in range(20)
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