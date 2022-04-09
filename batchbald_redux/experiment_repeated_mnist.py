# AUTOGENERATED! DO NOT EDIT! File to edit: 09b_experiment_repeated_mnist_bald.ipynb (unless otherwise specified).

__all__ = ['configs']

# Cell

import dataclasses
import traceback

from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .experiment_data import StandardExperimentDataConfig
from .models import MnistModelTrainer
from .unified_experiment import UnifiedExperiment

# Cell

configs = [
    UnifiedExperiment(
        experiment_data_config=StandardExperimentDataConfig(
            id_dataset_name="MNIST",
            id_repetitions=id_repetitions,
            initial_training_set_size=20,
            validation_set_size=4096,
            validation_split_random_state=0,
            evaluation_set_size=0,
            add_dataset_noise=True,
            ood_dataset_config=None,
        ),
        seed=seed + 45682,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=300,
        model_trainer_factory=MnistModelTrainer,
        stochastic_mode=stochastic_mode,
        coldness=coldness,
    )
    for seed in range(5)
    for acquisition_size in [10]
    for num_pool_samples in [100]
    for id_repetitions in [4]
    for coldness in [1.]
    # Already ran Power
    for stochastic_mode in [
        acquisition_functions.StochasticMode.TopK,
        acquisition_functions.StochasticMode.Softrank,
        acquisition_functions.StochasticMode.Power,
        acquisition_functions.StochasticMode.Softmax,
    ]
    for acquisition_function in [
        baseline_acquisition_functions.VariationRatios,
        baseline_acquisition_functions.Margin,
        baseline_acquisition_functions.StdDev,
    ]
]
# [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 1765,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#         stochastic_mode=stochastic_mode,
#         coldness=coldness,
#     )
#     for acquisition_function in [
#         acquisition_functions.StochasticBALD,
#     ]
#     for seed in range(5)
#     for acquisition_size in [20, 40]
#     for num_pool_samples in [100]
#     for id_repetitions in [1, 2, 4]
#     for coldness in [8, 4, 1]
#     # Already ran Power
#     for stochastic_mode in [
#         acquisition_functions.StochasticMode.Power,
#         acquisition_functions.StochasticMode.Softmax,
#     ]
# ] + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 1765,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#         stochastic_mode=stochastic_mode,
#         coldness=coldness,
#     )
#     for acquisition_function in [
#         acquisition_functions.StochasticBALD,
#     ]
#     for seed in range(5)
#     for acquisition_size in [20, 40]
#     for num_pool_samples in [100]
#     for id_repetitions in [1, 2, 4]
#     for coldness in [1.]
#     # Already ran Power
#     for stochastic_mode in [
#         acquisition_functions.StochasticMode.Softrank,
#     ]
# ] + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 1765,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#     )
#     for acquisition_function in [
#         acquisition_functions.BALD,
#     ]
#     for seed in range(5)
#     for acquisition_size in [20, 40]
#     for num_pool_samples in [100]
#     for id_repetitions in [1,2,4]
# ]
# [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#     )
#     for acquisition_function in [
#         acquisition_functions.BatchBALD,
#     ]
#     for seed in range(5)
#     for acquisition_size in [5]
#     for num_pool_samples in [100]
#     for id_repetitions in [1,2,4]
# ] + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#         stochastic_mode = stochastic_mode,
#         coldness = 8.0
#     )
#     for acquisition_function in [
#         acquisition_functions.StochasticBALD,
#     ]
#     for seed in range(5)
#     for acquisition_size in [10]
#     for num_pool_samples in [100]
#     for id_repetitions in [1,2,4]
#     # Already ran Power
#     for stochastic_mode in [acquisition_functions.StochasticMode.Softmax, acquisition_functions.StochasticMode.Softrank]
# ] + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#     )
#     for acquisition_function in [
#         acquisition_functions.BALD,
#         acquisition_functions.Random,
#         baseline_acquisition_functions.BADGE
#     ]
#     for seed in range(5)
#     for acquisition_size in [10]
#     for num_pool_samples in [100]
#     for id_repetitions in [1,2,4]
# ] + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=True,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=300,
#         model_trainer_factory=MnistModelTrainer,
#     )
#     for acquisition_function in [
#         baseline_acquisition_functions.BADGE
#     ]
#     for seed in range(5)
#     for acquisition_size in [20, 40]
#     for num_pool_samples in [100]
#     for id_repetitions in [1,2,4]
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