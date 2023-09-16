# AUTOGENERATED! DO NOT EDIT! File to edit: 09c_experiment_cifar10_missing_classes.ipynb (unless otherwise specified).

__all__ = ['configs']

# Cell

import dataclasses
import traceback

from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

import batchbald_redux.acquisition_functions.bald
import batchbald_redux.acquisition_functions.epig
from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .experiment_data import (
    ImbalancedTestDistributionExperimentDataConfig,
)
from .unified_experiment import UnifiedExperiment

# Cell

# (ID: air, automobile, ship and truck, OOD: bird, cat, deer, dog, frog and horse)
# ood_classes={2, 3, 4, 5, 6, 7}



configs = [
    UnifiedExperiment(
        experiment_data_config=ImbalancedTestDistributionExperimentDataConfig(
            dataset_name="CIFAR-10",
            repetitions=1,
            initial_training_set_size=0,
            validation_set_size=4000,
            validation_split_random_state=0,
            evaluation_set_size=4000,
            add_dataset_noise=False,
            minority_classes={2, 3, 4, 5, 6, 7},
            minority_class_percentage=0.0,
        ),
        seed=seed + 4658,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=450,
        ensemble_size=5,
        disable_training_augmentations=True
    )
    for seed in range(5)
    for acquisition_function in [
        batchbald_redux.acquisition_functions.bald.BALD,
        batchbald_redux.acquisition_functions.epig.EPIG,
        #acquisition_functions.EvalBALD,
        #baseline_acquisition_functions.BADGE,
        #acquisition_functions.Random,
    ]
    for acquisition_size in [10]
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