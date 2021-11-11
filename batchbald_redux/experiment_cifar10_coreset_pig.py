# AUTOGENERATED! DO NOT EDIT! File to edit: 09b_experiment_cifar10_coreset_pig.ipynb (unless otherwise specified).

__all__ = ['configs']

# Cell

import dataclasses
import traceback

from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .experiment_data import StandardExperimentDataConfig
from .unified_experiment import UnifiedExperiment
from .train_eval_model import TrainExplicitEvalModel
from .resnet_models import Cifar10ModelWorkshopPaperTrainer

# Cell

configs = [
    UnifiedExperiment(
        experiment_data_config=StandardExperimentDataConfig(
            id_dataset_name="CIFAR-10",
            id_repetitions=1,
            initial_training_set_size=0,
            validation_set_size=5000,
            validation_split_random_state=seed + 8945,
            evaluation_set_size=0,
            add_dataset_noise=False,
            ood_dataset_config=None,
        ),
        seed=seed + 8945,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=200,
        train_eval_model=TrainExplicitEvalModel,
        ensemble_size=1,
        disable_training_augmentations=True,
        cache_explicit_eval_model=True,
        model_trainer_factory=Cifar10ModelWorkshopPaperTrainer
    )
    for seed in range(5)
    for acquisition_size in [1]
    for num_pool_samples in [100]
    for acquisition_function in [
        acquisition_functions.CoreSetPIGBALD,
        acquisition_functions.BALD,
        acquisition_functions.CoreSetPIG,
    ]
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