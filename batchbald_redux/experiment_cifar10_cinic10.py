# AUTOGENERATED! DO NOT EDIT! File to edit: 09a_experiment_cifar10_cinic10.ipynb (unless otherwise specified).

__all__ = ['shared_configs', 'configs']

# Cell

import dataclasses
import traceback

from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

import batchbald_redux.acquisition_functions.bald
from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .experiment_data import (
    OoDDatasetConfig,
    StandardExperimentDataConfig,
)
from .resnet_models import Cifar10ModelWorkshopPaperTrainer
from .unified_experiment import UnifiedExperiment

# Cell

shared_configs = dict(
    num_validation_samples=1,
    num_pool_samples=1,
    num_training_samples=1,
    resnet18_dropout_head=False,
    ensemble_size=3,
    max_training_epochs=105,
    model_trainer_factory=Cifar10ModelWorkshopPaperTrainer,
    max_training_set=16000,
)

configs = sum(
    [
        [
            UnifiedExperiment(
                experiment_data_config=StandardExperimentDataConfig(
                    id_dataset_name=id_dataset_name,
                    id_repetitions=1,
                    initial_training_set_size=1000,
                    validation_set_size=1024,
                    validation_split_random_state=0,
                    evaluation_set_size=0,
                    add_dataset_noise=False,
                    ood_dataset_config=None,
                ),
                seed=seed + 1456,
                acquisition_function=acquisition_function,
                acquisition_size=acquisition_size,
                **shared_configs
            )
            for acquisition_function in [
            batchbald_redux.acquisition_functions.bald.BALD,
            ]
        ]
        + [
            UnifiedExperiment(
                experiment_data_config=StandardExperimentDataConfig(
                    id_dataset_name=id_dataset_name,
                    id_repetitions=1,
                    initial_training_set_size=1000,
                    validation_set_size=1024,
                    validation_split_random_state=0,
                    evaluation_set_size=0,
                    add_dataset_noise=False,
                    ood_dataset_config=None,
                ),
                seed=seed + 8945,
                acquisition_function=acquisition_function,
                acquisition_size=acquisition_size,
                coldness=coldness,
                stochastic_mode=stochastic_mode,
                **shared_configs
            )
            for stochastic_mode in [
                acquisition_functions.StochasticMode.Power,
                acquisition_functions.StochasticMode.Softmax,
                acquisition_functions.StochasticMode.Softrank,
            ]
            for coldness in ([1/8, 1] if stochastic_mode != acquisition_functions.StochasticMode.Softrank else [1])
            for acquisition_function in [
                batchbald_redux.acquisition_functions.bald.StochasticBALD,
            ]
        ]
        for seed in range(3)
        for id_dataset_name in ["CINIC-10"]
        for acquisition_size in [300]
    ],
    [],
)
# + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name=id_dataset_name,
#             id_repetitions=1,
#             initial_training_set_size=1000,
#             validation_set_size=1024,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=False,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 1456,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_validation_samples=1,
#         num_pool_samples=1,
#         num_training_samples=1,
#         resnet18_dropout_head=False,
#         ensemble_size=1,
#         max_training_epochs=105,
#         model_trainer_factory=Cifar10ModelWorkshopPaperTrainer,
#         max_training_set=16000,
#     )
#     for acquisition_function in [
#         baseline_acquisition_functions.BADGE,
#     ]
#     for seed in range(3)
#     for id_dataset_name in ["CIFAR-10", "CINIC-10"]
#     for acquisition_size in [300, 900]
# ]
#     UnifiedExperiment(
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         initial_training_set_size=1000,
#         evaluation_set_size=0,
#         max_training_set=15000,
#         temperature=temperature,
#         id_dataset_name="CIFAR-10",
#         ood_dataset_name=None,
#         ood_exposure=False,
#         id_repetitions=id_repetitions,
#         add_dataset_noise=True

#     )
#     for seed in range(5)
#     for acquisition_function in [
#         acquisition_functions.SieveBALD,
#     ]
#     for acquisition_size in [3000]
#     for num_pool_samples in [100]
#     for temperature in [1/64]
#     for id_repetitions in [1,5,10,20]
# ]
# +
#     UnifiedExperiment(
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         initial_training_set_size=1000,
#         evaluation_set_size=0,
#         max_training_set=15000,
#         temperature=temperature,
#         id_dataset_name="CIFAR-10",
#         ood_dataset_name=None,
#         ood_exposure=False,
#         id_repetitions=id_repetitions,
#         add_dataset_noise=True

#     )
#     for seed in range(5)
#     for acquisition_function in [
#         acquisition_functions.SoftmaxBALD,
#     ]
#     for acquisition_size in [3000]
#     for num_pool_samples in [100]
#     for temperature in [1/64]
#     for id_repetitions in [1,5,10,20]
# ] + [
#     UnifiedExperiment(
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         initial_training_set_size=1000,
#         evaluation_set_size=0,
#         max_training_set=15000,
#         temperature=temperature,
#         id_repetitions=id_repetitions,
#         add_dataset_noise=True,
#         id_dataset_name="CIFAR-10",
#         ood_dataset_name=None,
#         ood_exposure=False,
#     )
#     for seed in range(5)
#     for acquisition_function in [
#         acquisition_functions.BALD,
#     ]
#     for acquisition_size in [3000]
#     for num_pool_samples in [100]
#     for temperature in [0]
#     for id_repetitions in [1,5,10,20]
# ]

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