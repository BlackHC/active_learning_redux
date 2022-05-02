# AUTOGENERATED! DO NOT EDIT! File to edit: 09b_experiment_mnist_missing_classes_coreset_pig.ipynb (unless otherwise specified).

__all__ = ['configs']

# Cell

import dataclasses
import traceback

from blackhc.project import is_run_from_ipython
from blackhc.project.experiment import embedded_experiments

import batchbald_redux.acquisition_functions.bald
import batchbald_redux.acquisition_functions.coreset
from batchbald_redux import acquisition_functions, baseline_acquisition_functions
from .experiment_data import ImbalancedTestDistributionExperimentDataConfig
from .models import MnistModelTrainer
from .unified_experiment import UnifiedExperiment
from .train_eval_model import TrainExplicitEvalModel

# Cell

configs = [
    UnifiedExperiment(
        experiment_data_config=ImbalancedTestDistributionExperimentDataConfig(
            dataset_name="MNIST",
            repetitions=1,
            initial_training_set_size=20,
            validation_set_size=4000,
            validation_split_random_state=0,
            evaluation_set_size=4000,
            add_dataset_noise=False,
            minority_classes={2, 3, 4, 5, 7},
            minority_class_percentage=0.
        ),
        seed=seed + 8945,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=120,
        model_trainer_factory=MnistModelTrainer,
        train_eval_model=TrainExplicitEvalModel
    )
    for seed in range(3)
    for acquisition_size in [1, 10]
    for num_pool_samples in [100]
    for id_repetitions in [1]
    for acquisition_function in [
        batchbald_redux.acquisition_functions.bald.BALD,
        batchbald_redux.acquisition_functions.coreset.CoreSetPIG,
        batchbald_redux.acquisition_functions.coreset.CoreSetPIGBALD,
    ]
 ]
#    + [
#     UnifiedExperiment(
#         experiment_data_config=StandardExperimentDataConfig(
#             id_dataset_name="MNIST",
#             id_repetitions=id_repetitions,
#             initial_training_set_size=20,
#             validation_set_size=4096,
#             validation_split_random_state=0,
#             evaluation_set_size=0,
#             add_dataset_noise=id_repetitions > 1,
#             ood_dataset_config=None,
#         ),
#         seed=seed + 8945,
#         acquisition_function=acquisition_function,
#         acquisition_size=acquisition_size,
#         num_pool_samples=num_pool_samples,
#         max_training_set=120,
#         model_trainer_factory=MnistModelTrainer,
#     )
#     for acquisition_function in [
#         baseline_acquisition_functions.BADGE,
#         acquisition_functions.EPIG,
#         acquisition_functions.EvalBALD,
#         acquisition_functions.BALD,
#     ]
#     for seed in range(5)
#     for acquisition_size in [1]
#     for num_pool_samples in [100]
#     for id_repetitions in [1]
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