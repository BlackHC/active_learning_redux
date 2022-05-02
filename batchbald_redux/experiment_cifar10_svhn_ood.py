# AUTOGENERATED! DO NOT EDIT! File to edit: 09c_experiment_cifar10_svhn_ood.ipynb (unless otherwise specified).

__all__ = ['configs']

# Cell

import dataclasses
import traceback

from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

import batchbald_redux.acquisition_functions.bald
import batchbald_redux.acquisition_functions.epig
from batchbald_redux import acquisition_functions
from batchbald_redux import baseline_acquisition_functions
from .experiment_data import StandardExperimentDataConfig, OoDDatasetConfig
from .unified_experiment import UnifiedExperiment

# Cell

configs = [
    UnifiedExperiment(
        experiment_data_config=StandardExperimentDataConfig(id_dataset_name=id_dataset, id_repetitions=1,
                                                                          initial_training_set_size=20,
                                                                          validation_set_size=4000,
                                                                          validation_split_random_state=0,
                                                                          evaluation_set_size=4000,
                                                                          add_dataset_noise=False,
                                                                          ood_dataset_config=OoDDatasetConfig(ood_dataset_name=ood_dataset, ood_repetitions=1, ood_exposure=ood_exposure)
                                                                          ),
        seed=seed + 4658,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=450 #15000,
    )
    for seed in range(5)
    for acquisition_function in [
        batchbald_redux.acquisition_functions.bald.BALD,
        batchbald_redux.acquisition_functions.epig.EPIG,
        #acquisition_functions.EvalBALD,
    ]
    for acquisition_size in [10]
    for num_pool_samples in [100]
    for ood_exposure in [False, True]
    for id_dataset, ood_dataset in [("CIFAR-10", "SVHN"), ("SVHN", "CIFAR-10")]
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