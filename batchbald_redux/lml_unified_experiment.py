# AUTOGENERATED! DO NOT EDIT! File to edit: 08d_lml_unified_experiment.ipynb (unless otherwise specified).

__all__ = ['LmlExperimentData', 'LmlExperimentDataConfig', 'load_distribution_experiment_data', 'LmlEstimates',
           'get_lml_estimates', 'LmlActiveLearner', 'LmlUnifiedExperiment', 'configs']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass
from typing import Dict, List, Optional, Type, Union

import numpy as np
import torch
import torch.utils.data
from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments
from torch import nn
from torch.utils.data import Dataset

import batchbald_redux.acquisition_functions.batchbald
import batchbald_redux.acquisition_functions.epig
import wandb
from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .acquisition_functions import (
    CandidateBatchComputer,
    EvalDatasetBatchComputer,
    EvalModelBatchComputer,
)
from .active_learning import ActiveLearningData
from .black_box_model_training import evaluate
from .dataset_operations import (
    NamedDataset,
    get_balanced_sample_indices,
    get_base_dataset_index,
    get_target,
)
from .datasets.factories import get_dataset
from .di import DependencyInjection
from .experiment_data import (
    ExperimentData,
    ExperimentDataConfig,
    OoDDatasetConfig,
    StandardExperimentDataConfig,
)
from .experiment_logging import init_wandb, log2wandb
from .models import MnistModelTrainer
from .models import Cifar10ModelTrainer
from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
)
from .trained_model import BayesianEnsembleModelTrainer, ModelTrainer

# Cell


@dataclass
class LmlExperimentData:
    train_dataset: Dataset
    validation_dataset: Dataset
    test_dataset: Dataset
    train_augmentations: nn.Module
    initial_training_set_indices: List[int]
    device: str


@dataclass
class LmlExperimentDataConfig(ExperimentDataConfig):
    id_dataset_name: str
    initial_training_set_size: int
    validation_set_size: int
    validation_split_random_state: int

    def load(self, device) -> LmlExperimentData:
        return load_distribution_experiment_data(
            id_dataset_name=self.id_dataset_name,
            initial_training_set_size=self.initial_training_set_size,
            validation_set_size=self.validation_set_size,
            validation_split_random_state=self.validation_split_random_state,
            device=device,
        )


def load_distribution_experiment_data(
    *,
    id_dataset_name: str,
    initial_training_set_size: int,
    validation_set_size: int,
    validation_split_random_state: int,
    device: str,
) -> LmlExperimentData:
    split_dataset = get_dataset(
        id_dataset_name,
        root="data",
        validation_set_size=validation_set_size,
        validation_split_random_state=validation_split_random_state,
        normalize_like_cifar10=True,
        device_hint=device,
    )

    train_dataset = split_dataset.train

    targets = train_dataset.get_targets()
    num_classes = train_dataset.get_num_classes()
    initial_samples_per_class = initial_training_set_size // num_classes
    initial_training_set_indices = get_balanced_sample_indices(
        targets=targets,
        num_classes=num_classes,
        samples_per_class=initial_samples_per_class,
        seed=validation_split_random_state,
    )

    return LmlExperimentData(
        train_dataset=train_dataset,
        validation_dataset=split_dataset.validation,
        test_dataset=split_dataset.test,
        train_augmentations=split_dataset.train_augmentations,
        initial_training_set_indices=initial_training_set_indices,
        device=split_dataset.device,
    )

# Cell


@dataclass
class LmlEstimates:
    marginal_log_predictive: float
    joint_log_predictive: float


def get_lml_estimates(log_probs_N_K_C_labels_N):
    log_probs_N_K_C, labels_N = log_probs_N_K_C_labels_N

    true_log_probs_N_K = log_probs_N_K_C[list(range(len(labels_N))), :, labels_N]

    # Compute predictive distribution individually (as average of MC samples) and sum up.
    marginal_log_predictive = (torch.logsumexp(true_log_probs_N_K, dim=1) - np.log(true_log_probs_N_K.shape[1])).sum(
        dim=0
    )

    # Compute joint distribution for each consistent parameter sample and then average.
    joint_log_predictive = torch.logsumexp(true_log_probs_N_K.sum(dim=0), dim=0) - np.log(true_log_probs_N_K.shape[1])

    return LmlEstimates(marginal_log_predictive, joint_log_predictive)


@dataclass
class LmlActiveLearner:
    acquisition_size: int
    max_training_set: int

    num_validation_samples: int
    num_pool_samples: int

    acquisition_function: Union[CandidateBatchComputer, EvalModelBatchComputer]
    model_trainer: ModelTrainer
    data: LmlExperimentData

    device: Optional

    def __call__(self, log):
        log["seed"] = torch.seed()

        # Active Learning setup
        data = self.data

        self.max_training_set = (
            (self.max_training_set + self.acquisition_size - 1) // self.acquisition_size * self.acquisition_size
        )

        active_learning_data = ActiveLearningData(data.train_dataset)
        active_learning_data.acquire_base_indices(data.initial_training_set_indices)

        # Remove most of the remaining pool set
        generator = np.random.default_rng(1137)
        discard_indices = generator.permutation(len(active_learning_data.pool_dataset))[
            : -(self.max_training_set - len(data.initial_training_set_indices))
        ]
        active_learning_data.extract_dataset_from_pool_indices(discard_indices)
        log["pool_indices"] = active_learning_data.pool_dataset.indices

        model_trainer = self.model_trainer

        train_loader = model_trainer.get_train_dataloader(active_learning_data.training_dataset)
        pool_loader = model_trainer.get_evaluation_dataloader(active_learning_data.pool_dataset)
        validation_loader = model_trainer.get_evaluation_dataloader(data.validation_dataset)
        test_loader = model_trainer.get_evaluation_dataloader(data.test_dataset)

        log["active_learning_steps"] = []
        active_learning_steps = log["active_learning_steps"]

        acquisition_function = self.acquisition_function

        num_iterations = 0
        max_iterations = int(
            1.5 * (self.max_training_set - len(active_learning_data.training_dataset)) / self.acquisition_size
        )

        # Active Training Loop
        while True:
            training_set_size = len(active_learning_data.training_dataset)
            print(f"Training set size {training_set_size}:")

            # iteration_log = dict(training={}, pool_training={}, evaluation_metrics=None, acquisition=None)
            active_learning_steps.append({})
            iteration_log = active_learning_steps[-1]

            iteration_log["training"] = {}

            loss = validation_loss = torch.nn.NLLLoss()

            trained_model = model_trainer.get_trained(
                train_loader=train_loader,
                train_augmentations=data.train_augmentations,
                validation_loader=validation_loader,
                log=iteration_log["training"],
                wandb_key_path="model_training",
                loss=loss,
                validation_loss=validation_loss,
            )

            evaluation_metrics = evaluate(
                model=trained_model,
                num_samples=self.num_validation_samples,
                loader=test_loader,
                device=self.device,
                storage_device="cpu",
            )
            iteration_log["evaluation_metrics"] = evaluation_metrics
            log2wandb(evaluation_metrics, commit=False)
            print(f"Perf after training {evaluation_metrics}")

            if training_set_size >= self.max_training_set or num_iterations >= max_iterations:
                log2wandb({}, commit=True)
                print("Done.")
                break

            if isinstance(acquisition_function, CandidateBatchComputer):
                candidate_batch = acquisition_function.compute_candidate_batch(trained_model, pool_loader, self.device)
            else:
                raise ValueError(f"Unknown acquisition function {acquisition_function}!")

            candidate_global_dataset_indices = []
            candidate_labels = []
            candidate_images = []
            for index in candidate_batch.indices:
                base_di = get_base_dataset_index(active_learning_data.pool_dataset, index)
                dataset_type = "id"
                candidate_global_dataset_indices.append((dataset_type, base_di.index))
                if dataset_type == "id":
                    label = get_target(active_learning_data.pool_dataset, index).tolist()
                else:
                    label = None
                candidate_labels.append(label)
                candidate_images.append(wandb.Image(active_learning_data.pool_dataset[index][0]))

            # Lml computation
            lml_batch_dataloader = model_trainer.get_evaluation_dataloader(
                torch.utils.data.Subset(active_learning_data.pool_dataset, candidate_batch.indices)
            )
            lml_log_probs_N_K_C_labels_N = trained_model.get_log_probs_N_K_C_labels_N(
                lml_batch_dataloader, self.num_pool_samples, self.device, "cpu"
            )
            lml_estimate = get_lml_estimates(lml_log_probs_N_K_C_labels_N)

            iteration_log["lml_estimate"] = lml_estimate
            log2wandb(dict(lml_estimate=dataclasses.asdict(lml_estimate)), commit=False)

            acquisition_info = dict(
                indices=candidate_global_dataset_indices, labels=candidate_labels, scores=candidate_batch.scores
            )
            iteration_log["acquisition"] = acquisition_info

            acquistion_batch_table = wandb.Table(
                data=list(
                    zip(
                        *zip(*candidate_global_dataset_indices),
                        candidate_images,
                        candidate_labels,
                        candidate_batch.scores,
                    )
                ),
                columns=["dataset", "index", "sample", "label", "score"],
            )
            log2wandb(dict(acquisition=acquistion_batch_table), commit=False)

            print(candidate_batch)
            print(candidate_global_dataset_indices)

            active_learning_data.acquire(candidate_batch.indices)

            ls = ", ".join(f"{label} ({score:.4})" for label, score in zip(candidate_labels, candidate_batch.scores))
            print(f"Acquiring (label, score)s: {ls}")

            num_iterations += 1
            log2wandb({}, commit=True)


@dataclass
class LmlUnifiedExperiment:
    seed: int

    experiment_data_config: LmlExperimentDataConfig

    acquisition_size: int = 5
    max_training_set: int = 200

    max_training_epochs: int = 300

    num_pool_samples: int = 100
    num_validation_samples: int = 20
    num_training_samples: int = 1

    device: str = "cuda"
    acquisition_function: Union[
        Type[CandidateBatchComputer], Type[EvalModelBatchComputer]
    ] = None  # acquisition_functions.BALD
    model_trainer_factory: Type[ModelTrainer] = None  # Cifar10ModelTrainer
    ensemble_size: int = 1

    temperature: float = 1.0
    coldness: float = 1.0
    stochastic_mode: acquisition_functions.StochasticMode = acquisition_functions.StochasticMode.TopK

    def load_experiment_data(self) -> LmlExperimentData:
        print(self.experiment_data_config)
        return self.experiment_data_config.load(self.device)

    # Simple Dependency Injection
    def create_acquisition_function(self):
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.acquisition_function)

    def create_model_trainer(self) -> ModelTrainer:
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.model_trainer_factory)

    def run(self, store, project=None, entity=None):
        init_wandb(self, project=project, entity=entity)

        torch.manual_seed(self.seed)

        # Active Learning setup
        data = self.load_experiment_data()
        store["dataset_info"] = dict(training=repr(data.train_dataset), test=repr(data.test_dataset))
        store["initial_training_set_indices"] = data.initial_training_set_indices

        print(wandb.config)

        wandb.config.initial_training_set_indices = data.initial_training_set_indices
        wandb.config["dataset_info"] = store["dataset_info"]

        acquisition_function = self.create_acquisition_function()
        model_trainer = self.create_model_trainer()
        if self.ensemble_size > 1:
            model_trainer = BayesianEnsembleModelTrainer(model_trainer=model_trainer, ensemble_size=self.ensemble_size)

        active_learner = LmlActiveLearner(
            acquisition_size=self.acquisition_size,
            max_training_set=self.max_training_set,
            num_validation_samples=self.num_validation_samples,
            num_pool_samples=self.num_pool_samples,
            acquisition_function=acquisition_function,
            model_trainer=model_trainer,
            data=data,
            device=self.device,
        )

        active_learner(store)

        wandb.finish()

# Cell

configs = [
    LmlUnifiedExperiment(
        experiment_data_config=LmlExperimentDataConfig(
            id_dataset_name="MNIST",
            initial_training_set_size=20,
            validation_set_size=4096,
            validation_split_random_state=0,
        ),
        seed=seed + 45682,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=1000,
        model_trainer_factory=MnistModelTrainer,
        stochastic_mode=stochastic_mode,
        coldness=coldness,
    )
    for seed in range(5)
    for acquisition_size in [5]
    for num_pool_samples in [100]
    for coldness in [1]
    for stochastic_mode in [
        acquisition_functions.StochasticMode.Power,
    ]
    for acquisition_function in [acquisition_functions.BALD, acquisition_functions.Random]
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