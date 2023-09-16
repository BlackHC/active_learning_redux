# AUTOGENERATED! DO NOT EDIT! File to edit: U_predetermined_acquisitions_70.ipynb (unless otherwise specified).

__all__ = ['additional_initial_acquisitions', 'predetermind_acquisition_base_indices', 'ActiveLearner',
           'UnifiedExperiment', 'configs']

# Cell

import dataclasses
import traceback
from dataclasses import dataclass
from typing import Optional, Type, Union

import torch
import torch.utils.data
from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

import batchbald_redux.acquisition_functions.bald
from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .acquisition_functions import (
    CandidateBatchComputer,
    EvalDatasetBatchComputer,
    EvalModelBatchComputer,
)
from .joint_entropy import compute_entropy
from .acquisition_functions.bald import get_bald_scores
from .black_box_model_training import evaluate
from .dataset_operations import get_base_dataset_index, get_target
from .di import DependencyInjection
from .experiment_data import (
    ExperimentData,
    ExperimentDataConfig,
    OoDDatasetConfig,
    StandardExperimentDataConfig,
)
from .models import MnistModelTrainer
from .models import Cifar10ModelTrainer
from .train_eval_model import (
    TrainEvalModel,
    TrainSelfDistillationEvalModel,
)
from .trained_model import BayesianEnsembleModelTrainer, ModelTrainer

# Cell

additional_initial_acquisitions = [
    26919,
    43627,
    1666,
    354,
    23669,
    48412,
    48486,
    18284,
    51745,
    8120,
    41099,
    11397,
    17942,
    38275,
    9674,
    7069,
    2810,
    35239,
    1279,
    11383,
    2271,
    921,
    15619,
    32386,
    17830,
    1385,
    20850,
    16780,
    15765,
    6786,
    18938,
    46468,
    54880,
    14885,
    15543,
    13091,
    39530,
    9241,
    21243,
    48253,
    42363,
    31951,
    6689,
    20219,
    17178,
    26621,
    27534,
    3889,
    48169,
    38735,
]

# Cell

predetermind_acquisition_base_indices = [
    31664,
    42015,
    20215,
    37591,
    34014,
    21701,
    51259,
    12610,
    31518,
    55509,
    16769,
    12950,
    35936,
    5873,
    15528,
    20884,
    41945,
    651,
    45732,
    29320,
    10657,
    15434,
    26053,
    935,
    32432,
    27276,
    33174,
    33543,
    50655,
    25653,
    52587,
    42685,
    33050,
    18699,
    38512,
    2582,
    16538,
    39818,
    47263,
    45455,
    10844,
    40072,
    29155,
    25988,
    20856,
    53605,
    7930,
    34293,
    42634,
    14520,
    54456,
    1921,
    55379,
    34009,
    53071,
    18117,
    16148,
    13289,
    14233,
    8605,
    39777,
    27896,
    18309,
    4650,
    22563,
    44135,
    50973,
    27305,
    8178,
    40552,
    27182,
    37730,
    46980,
    20842,
    43105,
    6755,
    43824,
    18844,
    50980,
    27382,
    52110,
    14680,
    22301,
    19650,
    36590,
    41017,
    4590,
    5672,
    35479,
    48975,
    49077,
    43109,
    42856,
    2273,
    4002,
    18055,
    54055,
    15867,
    54549,
    15192,
    39042,
    1525,
    38120,
    3057,
    20086,
    13057,
    7505,
    11657,
    24569,
    49364,
    30989,
    53456,
    7235,
    23671,
    45814,
    36550,
    53152,
    45304,
    32685,
    33228,
    51475,
    37468,
    44447,
    40218,
    534,
    36252,
    47000,
    34643,
    23067,
    33536,
    23213,
    5126,
    35791,
    23011,
    14709,
    7075,
    54995,
    7308,
    29994,
    37892,
    33361,
    20881,
    33282,
    45639,
    46699,
    35740,
    9412,
    54830,
    44191,
    35802,
    23061,
    44728,
    36421,
    48772,
    1009,
    55089,
    46336,
    5898,
    25672,
    5729,
    35894,
    48649,
    41716,
    46429,
    34903,
    2048,
    15100,
    20657,
    47788,
    36799,
    22143,
    18943,
    3910,
    23770,
    54559,
    47625,
    45886,
    39492,
    13150,
    15517,
    42365,
    15957,
    9998,
    27710,
    44947,
    41223,
    30797,
    34075,
    1746,
    936,
    29242,
    11607,
    1512,
    43561,
    21433,
    40354,
    49182,
    47826,
    48188,
    22556,
    32290,
    22715,
    42134,
    16732,
    46517,
    36151,
    53998,
    22282,
    48719,
    53914,
    12816,
    39033,
    50100,
    22013,
    6394,
    28314,
    46597,
    15518,
    50940,
    5448,
    26062,
    49161,
    51524,
    23881,
    27827,
    37421,
    50338,
    50342,
    15126,
    19795,
    43782,
    5827,
    31717,
    35617,
    5900,
    18764,
    51704,
    2961,
    14787,
    11637,
    15019,
    11895,
    52672,
    40474,
    22860,
    43123,
    31050,
    46590,
    4379,
    11972,
    23576,
    16893,
    12409,
    54716,
    33554,
    55040,
    1601,
    32576,
    30327,
    28526,
    3385,
    37937,
    18950,
    50683,
    43753,
    13339,
    26335,
    41237,
    17421,
    48792,
    35034,
    6553,
    36213,
    13189,
    15055,
    47037,
    14775,
    12995,
    37018,
    9467,
    35404,
    17462,
    25088,
    38942,
    14976,
    602,
    54047,
    15519,
    2598,
    366,
    49210,
    4257,
    351,
    13090,
    51921,
    3034,
    50274,
    50715,
    52259,
    46924,
]

# Cell


@dataclass
class ActiveLearner:
    acquisition_size: int

    num_validation_samples: int
    num_pool_samples: int

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

        data.active_learning.acquire_base_indices(additional_initial_acquisitions)

        # Active Training Loop
        for base_index in predetermind_acquisition_base_indices:
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

            iteration_log["acquisition"] = dict(indices=[base_index])
            acquired_label = get_target(data.active_learning.base_dataset, base_index)

            data.active_learning.acquire_base_indices([base_index])

            print(f"Acquiring base index {base_index} {acquired_label}")


@dataclass
class UnifiedExperiment:
    seed: int

    experiment_data_config: ExperimentDataConfig

    acquisition_size: int = 5

    max_training_epochs: int = 300

    num_pool_samples: int = 100
    num_validation_samples: int = 20
    num_training_samples: int = 1

    device: str = "cuda"
    acquisition_function: Union[Type[CandidateBatchComputer], Type[EvalModelBatchComputer]] = batchbald_redux\
        .acquisition_functions.bald.BALD
    train_eval_model: Type[TrainEvalModel] = TrainSelfDistillationEvalModel
    model_trainer_factory: Type[ModelTrainer] = Cifar10ModelTrainer
    ensemble_size: int = 1

    temperature: float = 0.0
    epig_bootstrap_type: acquisition_functions.BootstrapType = acquisition_functions.BootstrapType.NO_BOOTSTRAP
    epig_bootstrap_factor: float = 1.0
    epig_dtype: torch.dtype = torch.double
    disable_training_augmentations: bool = False
    cache_explicit_eval_model: bool = False

    def load_experiment_data(self) -> ExperimentData:
        print(self.experiment_data_config)
        return self.experiment_data_config.load(self.device)

    # Simple Dependency Injection
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

        model_trainer = self.create_model_trainer()
        if self.ensemble_size > 1:
            model_trainer = BayesianEnsembleModelTrainer(model_trainer=model_trainer, ensemble_size=self.ensemble_size)
        train_eval_model = self.create_train_eval_model()

        active_learner = ActiveLearner(
            acquisition_size=self.acquisition_size,
            num_validation_samples=self.num_validation_samples,
            num_pool_samples=self.num_pool_samples,
            disable_training_augmentations=self.disable_training_augmentations,
            train_eval_model=train_eval_model,
            model_trainer=model_trainer,
            data=data,
            device=self.device,
        )

        active_learner(store)

# Cell

# MNIST experiment (ood_exposure=False)

configs = [
    UnifiedExperiment(
        experiment_data_config=StandardExperimentDataConfig(
            id_dataset_name="MNIST",
            id_repetitions=1,
            initial_training_set_size=20,
            validation_set_size=4096,
            validation_split_random_state=0,
            evaluation_set_size=0,
            add_dataset_noise=False,
            ood_dataset_config=None,
        ),
        seed=trial,
        max_training_epochs=120,
        model_trainer_factory=MnistModelTrainer,
        num_pool_samples=100,
        ensemble_size=2,
        device="cuda",
    )
    for trial in range(5)
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