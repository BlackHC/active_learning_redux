# AUTOGENERATED! DO NOT EDIT! File to edit: 08c_unified_experiment.ipynb (unless otherwise specified).

__all__ = ['ActiveLearner', 'UnifiedExperiment', 'configs']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass
from typing import Optional, Type, Union

import torch
import torch.utils.data
from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

from batchbald_redux import acquisition_functions
from batchbald_redux import baseline_acquisition_functions
from .acquisition_functions import (
    CandidateBatchComputer,
    EvalDatasetBatchComputer,
    EvalModelBatchComputer,
)
from .black_box_model_training import evaluate
from .dataset_challenges import get_base_dataset_index, get_target
from .di import DependencyInjection
from .experiment_data import (
    ExperimentData,
    ExperimentDataConfig,
    OoDDatasetConfig,
    StandardExperimentDataConfig,
)
from .models import MnistModelTrainer
from .resnet_models import Cifar10ModelTrainer
from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
)
from .trained_model import ModelTrainer, BayesianEnsembleModelTrainer

# Cell


@dataclass
class ActiveLearner:
    acquisition_size: int
    max_training_set: int

    num_validation_samples: int

    acquisition_function: Union[CandidateBatchComputer, EvalModelBatchComputer]
    train_eval_model: TrainEvalModel
    model_trainer: ModelTrainer
    data: ExperimentData

    disable_training_augmentations: bool

    device: Optional

    def __call__(self, log):
        log["seed"] = torch.seed()

        # Active Learning setup
        data = self.data

        train_augmentations = data.train_augmentations if not self.disable_training_augmentations else None

        model_trainer = self.model_trainer
        train_eval_model = self.train_eval_model

        train_loader = model_trainer.get_train_dataloader(data.active_learning.training_dataset)
        pool_loader = model_trainer.get_evaluation_dataloader(data.active_learning.pool_dataset)
        validation_loader = model_trainer.get_evaluation_dataloader(data.validation_dataset)
        test_loader = model_trainer.get_evaluation_dataloader(data.test_dataset)

        log["active_learning_steps"] = []
        active_learning_steps = log["active_learning_steps"]

        acquisition_function = self.acquisition_function

        num_iterations = 0
        max_iterations = int(
            1.5 * (self.max_training_set - len(data.active_learning.training_dataset)) / self.acquisition_size
        )

        # Active Training Loop
        while True:
            training_set_size = len(data.active_learning.training_dataset)
            print(f"Training set size {training_set_size}:")

            # iteration_log = dict(training={}, pool_training={}, evaluation_metrics=None, acquisition=None)
            active_learning_steps.append({})
            iteration_log = active_learning_steps[-1]

            iteration_log["training"] = {}

            # TODO: this is a hack! :(
            if data.ood_dataset is None:
                loss = validation_loss = torch.nn.NLLLoss()
            elif data.ood_exposure:
                loss = torch.nn.KLDivLoss(log_target=False, reduction="batchmean")
                validation_loss = torch.nn.NLLLoss()
            else:
                loss = validation_loss = torch.nn.NLLLoss()

            trained_model = model_trainer.get_trained(
                train_loader=train_loader,
                train_augmentations=train_augmentations,
                validation_loader=validation_loader,
                log=iteration_log["training"],
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
            print(f"Perf after training {evaluation_metrics}")

            if training_set_size >= self.max_training_set or num_iterations >= max_iterations:
                print("Done.")
                break

            if isinstance(acquisition_function, CandidateBatchComputer):
                candidate_batch = acquisition_function.compute_candidate_batch(trained_model, pool_loader, self.device)
            elif isinstance(acquisition_function, EvalDatasetBatchComputer):
                if len(data.evaluation_dataset) > 0:
                    eval_loader = model_trainer.get_evaluation_dataloader(data.evaluation_dataset)
                else:
                    eval_loader = pool_loader

                candidate_batch = acquisition_function.compute_candidate_batch(
                    model=trained_model, pool_loader=pool_loader, eval_loader=eval_loader, device=self.device
                )
            elif isinstance(acquisition_function, EvalModelBatchComputer):
                if len(data.evaluation_dataset) > 0:
                    eval_dataset = data.evaluation_dataset
                else:
                    eval_dataset = data.active_learning.pool_dataset

                iteration_log["eval_training"] = {}
                trained_eval_model = train_eval_model(
                    model_trainer=model_trainer,
                    training_dataset=data.active_learning.training_dataset,
                    train_augmentations=train_augmentations,
                    eval_dataset=eval_dataset,
                    validation_loader=validation_loader,
                    trained_model=trained_model,
                    storage_device=data.device,
                    device=self.device,
                    training_log=iteration_log["eval_training"],
                )

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
                label = get_target(data.active_learning.pool_dataset, index).tolist()
                candidate_labels.append(label)

            iteration_log["acquisition"] = dict(
                indices=candidate_global_dataset_indices, labels=candidate_labels, scores=candidate_batch.scores
            )

            print(candidate_batch)
            print(candidate_global_dataset_indices)

            if data.ood_dataset is None:
                data.active_learning.acquire(candidate_batch.indices)
            elif data.ood_exposure:
                data.active_learning.acquire(candidate_batch.indices)
            else:
                data.active_learning.acquire(
                    [index for index, label in zip(candidate_batch.indices, candidate_labels) if label != -1]
                )

            ls = ", ".join(f"{label} ({score:.4})" for label, score in zip(candidate_labels, candidate_batch.scores))
            print(f"Acquiring (label, score)s: {ls}")

            num_iterations += 1


@dataclass
class UnifiedExperiment:
    seed: int

    experiment_data_config: ExperimentDataConfig

    acquisition_size: int = 5
    max_training_set: int = 200

    max_training_epochs: int = 300

    num_pool_samples: int = 100
    num_validation_samples: int = 20
    num_training_samples: int = 1

    device: str = "cuda"
    acquisition_function: Union[Type[CandidateBatchComputer], Type[EvalModelBatchComputer]] = acquisition_functions.BALD
    train_eval_model: Type[TrainEvalModel] = TrainSelfDistillationEvalModel
    model_trainer_factory: Type[ModelTrainer] = Cifar10ModelTrainer
    ensemble_size: int = 1

    temperature: float = 0.0
    coldness: float = 0.0
    stochastic_mode: acquisition_functions.StochasticMode = None
    epig_bootstrap_type: acquisition_functions.BootstrapType = acquisition_functions.BootstrapType.NO_BOOTSTRAP
    epig_bootstrap_factor: float = 1.
    epig_dtype: torch.dtype = torch.double
    disable_training_augmentations: bool = False
    cache_explicit_eval_model: bool = False

    def load_experiment_data(self) -> ExperimentData:
        print(self.experiment_data_config)
        return self.experiment_data_config.load(self.device)

    # Simple Dependency Injection
    def create_acquisition_function(self):
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.acquisition_function)

    def create_train_eval_model(self) -> TrainEvalModel:
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.train_eval_model)

    def create_model_trainer(self) -> ModelTrainer:
        di = DependencyInjection(vars(self))
        return di.create_dataclass_type(self.model_trainer_factory)

    def run(self, store):
        torch.manual_seed(self.seed)

        # Active Learning setup
        data = self.load_experiment_data()
        store["dataset_info"] = dict(training=repr(data.active_learning.base_dataset), test=repr(data.test_dataset))
        store["initial_training_set_indices"] = data.initial_training_set_indices
        store["evaluation_set_indices"] = data.evaluation_set_indices

        acquisition_function = self.create_acquisition_function()
        model_trainer = self.create_model_trainer()
        if self.ensemble_size > 1:
            model_trainer = BayesianEnsembleModelTrainer(model_trainer=model_trainer, ensemble_size=self.ensemble_size)
        train_eval_model = self.create_train_eval_model()

        active_learner = ActiveLearner(
            acquisition_size=self.acquisition_size,
            max_training_set=self.max_training_set,
            num_validation_samples=self.num_validation_samples,
            disable_training_augmentations=self.disable_training_augmentations,
            acquisition_function=acquisition_function,
            train_eval_model=train_eval_model,
            model_trainer=model_trainer,
            data=data,
            device=self.device,
        )

        active_learner(store)

# Cell

configs = [
    UnifiedExperiment(
        seed=seed + 1234,
        experiment_data_config=StandardExperimentDataConfig(
            id_dataset_name=id_dataset_name,
            id_repetitions=1,
            initial_training_set_size=20,
            validation_set_size=4096,
            validation_split_random_state=0,
            evaluation_set_size=evaluation_set_size,
            add_dataset_noise=False,
            ood_dataset_config=OoDDatasetConfig(
                ood_dataset_name=ood_dataset_name, ood_repetitions=1, ood_exposure=ood_exposure
            ),
        ),
        acquisition_function=acquisition_function,
        acquisition_size=5,
        num_pool_samples=num_pool_samples,
    )
    for seed in range(3)
    for acquisition_function in [acquisition_functions.BatchEvalBALD, acquisition_functions.BatchBALD]
    for evaluation_set_size in [1024]
    for num_pool_samples in [100]
    for ood_exposure in [True, False]
    for id_dataset_name, ood_dataset_name in [("CIFAR-10", "SVHN"), ("SVHN", "CIFAR-10")]
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