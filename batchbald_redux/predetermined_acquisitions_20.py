# AUTOGENERATED! DO NOT EDIT! File to edit: U_predetermined_acquisitions_20.ipynb (unless otherwise specified).

__all__ = ['predetermind_acquisition_base_indices', 'ActiveLearner', 'UnifiedExperiment', 'configs']

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

predetermind_acquisition_base_indices = [
    26919,
    44321,
    12604,
    18494,
    50811,
    52598,
    33588,
    8467,
    33962,
    6502,
    28779,
    12858,
    50958,
    30271,
    23652,
    52324,
    42837,
    24733,
    22071,
    18574,
    46819,
    9563,
    13559,
    53955,
    31962,
    26636,
    13170,
    3317,
    19463,
    8120,
    481,
    53117,
    31558,
    14832,
    21083,
    354,
    31063,
    16817,
    10231,
    19567,
    19118,
    17641,
    12329,
    7069,
    30911,
    3196,
    8051,
    37688,
    14302,
    30494,
    34143,
    45260,
    31056,
    13647,
    12752,
    7238,
    30174,
    43593,
    2025,
    49302,
    50877,
    38453,
    666,
    6382,
    39297,
    22938,
    28324,
    32880,
    28883,
    44904,
    34288,
    2129,
    7324,
    45973,
    36147,
    26508,
    1275,
    955,
    18612,
    22372,
    54800,
    55261,
    974,
    53928,
    14087,
    13276,
    45615,
    29587,
    1355,
    22543,
    44222,
    28479,
    16597,
    41976,
    32058,
    37236,
    37718,
    39817,
    8377,
    34370,
    44848,
    24996,
    31677,
    19090,
    19569,
    23272,
    50317,
    7021,
    32590,
    38665,
    8325,
    22749,
    33247,
    12608,
    14564,
    31500,
    5961,
    43342,
    2043,
    14842,
    39513,
    27211,
    16296,
    27638,
    19736,
    25089,
    41776,
    34984,
    15749,
    1190,
    47320,
    6995,
    6050,
    20300,
    46216,
    293,
    52393,
    29974,
    12033,
    44877,
    36287,
    11797,
    31127,
    51010,
    14711,
    39470,
    6778,
    26240,
    2649,
    36799,
    39714,
    24714,
    11803,
    4497,
    28859,
    18765,
    15544,
    8758,
    18212,
    17841,
    48971,
    28243,
    37043,
    44047,
    46562,
    21933,
    29090,
    12636,
    26512,
    36271,
    22945,
    49077,
    34918,
    29994,
    55020,
    26210,
    53029,
    53553,
    27512,
    7490,
    20898,
    17666,
    30887,
    5059,
    34869,
    31721,
    16628,
    20465,
    53400,
    3049,
    34885,
    22568,
    47915,
    42158,
    52077,
    26458,
    44333,
    50388,
    36837,
    24183,
    34890,
    41217,
    36471,
    7114,
    3559,
    45728,
    1306,
    32627,
    46860,
    9230,
    54921,
    5505,
    46507,
    24474,
    50461,
    23370,
    11472,
    48003,
    43627,
    44532,
    45509,
    43134,
    38829,
    12995,
    48278,
    26167,
    35733,
    22548,
    29346,
    24341,
    6756,
    13021,
    6732,
    47842,
    24974,
    3155,
    33543,
    38326,
    3105,
    11793,
    28897,
    5313,
    12221,
    18992,
    32672,
    22815,
    38098,
    10022,
    4736,
    52133,
    5190,
    7480,
    55130,
    32369,
    32756,
    48768,
    52248,
    241,
    48294,
    55407,
    48642,
    7688,
    54038,
    20243,
    1520,
    11382,
    9257,
    14018,
    6277,
    23889,
    52318,
    26143,
    51188,
    32907,
    15677,
    2349,
    48140,
    31314,
    18055,
    11270,
    40338,
    29173,
    53693,
    44834,
    14684,
    16314,
    54668,
    27606,
    234,
    54791,
    15428,
    51153,
    11254,
    51652,
    41140,
    26610,
    24878,
    38679,
    51566,
    33139,
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