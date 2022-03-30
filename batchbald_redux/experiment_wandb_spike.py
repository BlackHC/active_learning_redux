# AUTOGENERATED! DO NOT EDIT! File to edit: 09b_experiment_wandb_spike.ipynb (unless otherwise specified).

__all__ = ['asclassdict', 'configs']

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

import wandb

# Cell

import copy

# Helper to add class names to dicts (based on dataclasses.asdict)

def asclassdict(obj, *, dict_factory=dict):
    """Return the fields of a dataclass instance as a new dictionary mapping
    field names to field values.

    Example usage:

      @dataclass
      class C:
          x: int
          y: int

      c = C(1, 2)
      assert asdict(c) == {'x': 1, 'y': 2}

    If given, 'dict_factory' will be used instead of built-in dict.
    The function applies recursively to field values that are
    dataclass instances. This will also look into built-in containers:
    tuples, lists, and dicts.
    """
    if not dataclasses._is_dataclass_instance(obj):
        raise TypeError("asdict() should be called on dataclass instances")
    return _asclassdict_inner(obj, dict_factory)


def _asclassdict_inner(obj, dict_factory):
    if dataclasses._is_dataclass_instance(obj):
        result = []
        result.append(("Dataclass", f"{obj.__class__.__module__}.{obj.__class__.__qualname__}"))
        for f in dataclasses.fields(obj):
            value = _asclassdict_inner(getattr(obj, f.name), dict_factory)
            result.append((f.name, value))
        return dict_factory(result)
    elif isinstance(obj, tuple) and hasattr(obj, '_fields'):
        # obj is a namedtuple.  Recurse into it, but the returned
        # object is another namedtuple of the same type.  This is
        # similar to how other list- or tuple-derived classes are
        # treated (see below), but we just need to create them
        # differently because a namedtuple's __init__ needs to be
        # called differently (see bpo-34363).

        # I'm not using namedtuple's _asdict()
        # method, because:
        # - it does not recurse in to the namedtuple fields and
        #   convert them to dicts (using dict_factory).
        # - I don't actually want to return a dict here.  The main
        #   use case here is json.dumps, and it handles converting
        #   namedtuples to lists.  Admittedly we're losing some
        #   information here when we produce a json list instead of a
        #   dict.  Note that if we returned dicts here instead of
        #   namedtuples, we could no longer call asdict() on a data
        #   structure where a namedtuple was used as a dict key.

        return type(obj)(*[_asclassdict_inner(v, dict_factory) for v in obj])
    elif isinstance(obj, (list, tuple)):
        # Assume we can create an object of this type by passing in a
        # generator (which is not true for namedtuples, handled
        # above).
        return type(obj)(_asclassdict_inner(v, dict_factory) for v in obj)
    elif isinstance(obj, dict):
        return type(obj)((_asclassdict_inner(k, dict_factory),
                          _asclassdict_inner(v, dict_factory))
                         for k, v in obj.items())
    else:
        return copy.deepcopy(obj)

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
        seed=seed + 1765,
        acquisition_function=acquisition_function,
        acquisition_size=acquisition_size,
        num_pool_samples=num_pool_samples,
        max_training_set=300,
        model_trainer_factory=MnistModelTrainer,
        stochastic_mode=stochastic_mode,
        coldness=coldness,
    )
    for acquisition_function in [
        acquisition_functions.StochasticBALD,
    ]
    for seed in range(5)
    for acquisition_size in [20, 40]
    for num_pool_samples in [100]
    for id_repetitions in [1, 2, 4]
    for coldness in [8, 4, 1]
    # Already ran Power
    for stochastic_mode in [
        acquisition_functions.StochasticMode.Power,
        acquisition_functions.StochasticMode.Softmax,
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