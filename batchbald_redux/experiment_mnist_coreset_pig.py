# AUTOGENERATED! DO NOT EDIT! File to edit: 09b_experiment_mnist_coreset_pig.ipynb (unless otherwise specified).

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
from .train_eval_model import TrainExplicitEvalModel

# Cell

configs = [
    UnifiedExperiment(
        experiment_data_config=StandardExperimentDataConfig(
            id_dataset_name="MNIST",
            id_repetitions=id_repetitions,
            initial_training_set_size=20,
            validation_set_size=4000,
            validation_split_random_state=0,
            evaluation_set_size=4000,
            add_dataset_noise=id_repetitions > 1,
            ood_dataset_config=None,
        ),
        seed=seed + 8945,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=120,
        model_trainer_factory=MnistModelTrainer,
        train_eval_model=TrainExplicitEvalModel
    )
    for seed in range(5)
    for acquisition_size in [1]
    for num_pool_samples in [100]
    for id_repetitions in [1]
    for acquisition_function in [
        acquisition_functions.BALD,
        acquisition_functions.CoreSetPIG,
        acquisition_functions.CoreSetPIGBALD,
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