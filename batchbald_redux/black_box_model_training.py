# AUTOGENERATED! DO NOT EDIT! File to edit: 07_black_box_training.ipynb (unless otherwise specified).

__all__ = ['train', 'LOG_INTERVAL', 'train_with_schedule', 'ModelOptimizerStateDicts', 'DoubleSnapshots',
           'train_double_snapshots', 'evaluate', 'evaluate_old', 'create_metrics']

# Internal Cell

from dataclasses import dataclass
from typing import Optional
import torch
from blackhc.project import is_run_from_ipython
from blackhc.project.utils.ignite_progress_bar import ignite_progress_bar
from ignite.contrib.engines.common import setup_common_training_handlers
from ignite.contrib.handlers import ProgressBar
from ignite.engine import Events, create_supervised_evaluator, create_supervised_trainer
from ignite.metrics import Accuracy, Loss, RunningAverage
from torch import nn


from .consistent_mc_dropout import (
    GeometricMeanPrediction,
    SamplerModel,
    multi_sample_loss, BayesianModule, get_log_mean_probs,
)
from .restoring_early_stopping import (
    PatienceWithSnapshot,
    ReduceLROnPlateauWithScheduleWrapper,
    RestoringEarlyStopping,
)

# Cell
from .trained_model import TrainedModel

LOG_INTERVAL = 10


def train(
    *,
    model,
    training_samples,
    validation_samples,
    train_loader,
    validation_loader,
    patience: Optional[int],
    max_epochs: int,
    device: str,
    training_log: dict,
    loss=None,
    validation_loss=None,
    optimizer=None,
    prefer_accuracy=True,
    train_augmentations=None,
):
    if loss is None:
        loss = nn.NLLLoss()
    if validation_loss is None:
        validation_loss = loss

    train_model = SamplerModel(model, training_samples)
    if train_augmentations is not None:
        train_model = torch.nn.Sequential(train_augmentations, train_model)

    validation_model = GeometricMeanPrediction(SamplerModel(model, validation_samples))

    # Move model to device before creating the optimizer
    train_model.to(device)

    if optimizer is None:
        optimizer = torch.optim.Adam(model.parameters(), weight_decay=5e-4)

    trainer = create_supervised_trainer(train_model, optimizer, loss_fn=multi_sample_loss(loss), device=device)

    metrics = create_metrics(validation_loss)

    validation_evaluator = create_supervised_evaluator(validation_model, metrics=metrics, device=device)

    @trainer.on(Events.EPOCH_COMPLETED)
    def compute_metrics(engine):
        validation_evaluator.run(validation_loader)

    # Only to look nicer.
    RunningAverage(output_transform=lambda x: x).attach(trainer, "crossentropy")

    enable_tqdm_pbars = is_run_from_ipython()

    setup_common_training_handlers(
        trainer, with_pbars=enable_tqdm_pbars, with_gpu_stats=torch.cuda.is_available(), log_every_iters=LOG_INTERVAL
    )

    if enable_tqdm_pbars:
        ProgressBar(persist=False).attach(
            validation_evaluator,
            metric_names="all",
            event_name=Events.ITERATION_COMPLETED(every=LOG_INTERVAL),
        )
    else:
        ignite_progress_bar(trainer, desc=lambda engine: "Training", log_interval=LOG_INTERVAL)

    training_log["epochs"] = []
    epochs_log = training_log["epochs"]

    # Logging
    @validation_evaluator.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        metrics = dict(engine.state.metrics)
        epochs_log.append(metrics)

        if is_run_from_ipython():
            print(f"Epoch metrics: {metrics}")

    # Add early stopping
    if patience is not None:
        if prefer_accuracy:

            def score_function():
                return float(validation_evaluator.state.metrics["accuracy"])

        else:

            def score_function():
                return float(-validation_evaluator.state.metrics["crossentropy"])

        early_stopping = RestoringEarlyStopping(
            patience=patience,
            score_function=score_function,
            module=model,
            optimizer=optimizer,
            training_engine=trainer,
            validation_engine=validation_evaluator,
        )
    else:
        early_stopping = None

    # Kick everything off
    trainer.run(train_loader, max_epochs=max_epochs)

    if early_stopping:
        training_log["best_epoch"] = early_stopping.best_epoch

    # Return the optimizer in case we want to continue training.
    return optimizer

# Cell


def train_with_schedule(
    *,
    model,
    training_samples,
    validation_samples,
    train_loader,
    validation_loader,
    patience_schedule: [int],
    factor_schedule: [int],
    max_epochs: int,
    device: str,
    training_log: dict,
    loss=None,
    validation_loss=None,
    optimizer=None,
    prefer_accuracy=True,
    train_augmentations=None,
):
    if loss is None:
        loss = nn.NLLLoss()
    if validation_loss is None:
        validation_loss = loss

    train_model = SamplerModel(model, training_samples)
    if train_augmentations is not None:
        train_model = torch.nn.Sequential(train_augmentations, train_model)

    validation_model = GeometricMeanPrediction(SamplerModel(model, validation_samples))

    # Move model to device before creating the optimizer
    train_model.to(device)

    if optimizer is None:
        optimizer = torch.optim.Adam(model.parameters(), weight_decay=5e-4)

    trainer = create_supervised_trainer(train_model, optimizer, loss_fn=multi_sample_loss(loss), device=device)

    metrics = create_metrics(validation_loss)

    validation_evaluator = create_supervised_evaluator(validation_model, metrics=metrics, device=device)

    @trainer.on(Events.EPOCH_COMPLETED)
    def compute_metrics(engine):
        validation_evaluator.run(validation_loader)

    # Only to look nicer.
    RunningAverage(output_transform=lambda x: x).attach(trainer, "crossentropy")

    enable_tqdm_pbars = is_run_from_ipython()

    setup_common_training_handlers(
        trainer, with_pbars=enable_tqdm_pbars, with_gpu_stats=torch.cuda.is_available(), log_every_iters=LOG_INTERVAL
    )

    if enable_tqdm_pbars:
        ProgressBar(persist=False).attach(
            validation_evaluator,
            metric_names="all",
            event_name=Events.ITERATION_COMPLETED(every=LOG_INTERVAL),
        )
    else:
        ignite_progress_bar(trainer, desc=lambda engine: "Training", log_interval=LOG_INTERVAL)

    training_log["epochs"] = []
    epochs_log = training_log["epochs"]

    # Logging
    @validation_evaluator.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        metrics = dict(engine.state.metrics)
        epochs_log.append(metrics)

        if is_run_from_ipython():
            print(f"Epoch metrics: {metrics}")

    if prefer_accuracy:
        def score_function(metrics):
            return float(metrics["accuracy"])

    else:

        def score_function(metrics):
            return float(metrics["crossentropy"])

    training_log["era_epochs"] = []

    def next_era_callback():
        training_log["era_epochs"].append(trainer.state.epoch)

    scheduler = ReduceLROnPlateauWithScheduleWrapper(
        optimizer,
        metrics_transform=score_function,
        factor_schedule=factor_schedule,
        patience_schedule=patience_schedule,
        end_callback=trainer.terminate,
        next_era_callback=next_era_callback,
        mode="max" if prefer_accuracy else "min",
        verbose=True,
    )

    @validation_evaluator.on(Events.EPOCH_COMPLETED)
    def step_scheduler(engine):
        scheduler.step(engine)

    # Kick everything off
    trainer.run(train_loader, max_epochs=max_epochs)

    # Return the optimizer in case we want to continue training.
    return optimizer

# Cell


@dataclass
class ModelOptimizerStateDicts:
    model_state_dict: object
    optimizer_state_dict: object


@dataclass
class DoubleSnapshots:
    high_accuracy: ModelOptimizerStateDicts
    low_cross_entropy: ModelOptimizerStateDicts


def train_double_snapshots(
    *,
    model: BayesianModule,
    training_samples,
    validation_samples,
    train_loader,
    validation_loader,
    patience: int,
    max_epochs: int,
    device: str,
    training_log: dict,
    loss=None,
    validation_loss=None,
    optimizer=None,
    train_augmentations: torch.nn.Module,
) -> DoubleSnapshots:
    if loss is None:
        loss = nn.NLLLoss()
    if validation_loss is None:
        validation_loss = loss

    train_model = SamplerModel(model, training_samples)
    if train_augmentations is not None:
        train_model = torch.nn.Sequential(train_augmentations, train_model)

    validation_model = GeometricMeanPrediction(SamplerModel(model, validation_samples))

    # Move model to device before creating the optimizer
    train_model.to(device)

    if optimizer is None:
        optimizer = torch.optim.Adam(model.parameters(), weight_decay=5e-4)

    trainer = create_supervised_trainer(train_model, optimizer, loss_fn=multi_sample_loss(loss), device=device)

    metrics = create_metrics(validation_loss)

    validation_evaluator = create_supervised_evaluator(validation_model, metrics=metrics, device=device)

    @trainer.on(Events.EPOCH_COMPLETED)
    def compute_metrics(engine):
        validation_evaluator.run(validation_loader)

    # Only to look nicer.
    RunningAverage(output_transform=lambda x: x).attach(trainer, "crossentropy")

    enable_tqdm_pbars = is_run_from_ipython()

    setup_common_training_handlers(
        trainer, with_pbars=enable_tqdm_pbars, with_gpu_stats=torch.cuda.is_available(), log_every_iters=LOG_INTERVAL
    )

    if enable_tqdm_pbars:
        ProgressBar(persist=False).attach(
            validation_evaluator,
            metric_names="all",
            event_name=Events.ITERATION_COMPLETED(every=LOG_INTERVAL),
        )
    else:
        ignite_progress_bar(trainer, desc=lambda engine: "Training", log_interval=LOG_INTERVAL)

    training_log["epochs"] = []
    epochs_log = training_log["epochs"]

    # Logging
    @validation_evaluator.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        metrics = dict(engine.state.metrics)
        epochs_log.append(metrics)

        if is_run_from_ipython():
            print(f"Epoch metrics: {metrics}")

    cross_entropy_state_dicts = None
    accuracy_state_dicts = None

    # Add early stopping
    if patience is not None:

        def cross_entropy_out_of_patience_callback(module_state_dict, optimizer_state_dict):
            nonlocal cross_entropy_state_dicts
            cross_entropy_state_dicts = ModelOptimizerStateDicts(
                model_state_dict=module_state_dict, optimizer_state_dict=optimizer_state_dict
            )
            if cross_entropy_pws.is_out_of_patience() and accuracy_entropy_pws.is_out_of_patience():
                trainer.terminate()

        cross_entropy_pws = PatienceWithSnapshot(
            name="LowCrossEntropy-",
            patience=patience,
            score_function=lambda: float(-validation_evaluator.state.metrics["crossentropy"]),
            module=model,
            optimizer=optimizer,
            training_engine=trainer,
            validation_engine=validation_evaluator,
            out_of_patience_callback=cross_entropy_out_of_patience_callback,
        )

        def accuracy_out_of_patience_callback(module_state_dict, optimizer_state_dict):
            nonlocal accuracy_state_dicts
            accuracy_state_dicts = ModelOptimizerStateDicts(
                model_state_dict=module_state_dict, optimizer_state_dict=optimizer_state_dict
            )
            if cross_entropy_pws.is_out_of_patience() and accuracy_entropy_pws.is_out_of_patience():
                trainer.terminate()

        accuracy_entropy_pws = PatienceWithSnapshot(
            name="Accuracy-",
            patience=patience,
            score_function=lambda: float(validation_evaluator.state.metrics["accuracy"]),
            module=model,
            optimizer=optimizer,
            training_engine=trainer,
            validation_engine=validation_evaluator,
            out_of_patience_callback=accuracy_out_of_patience_callback,
        )

    # Kick everything off
    trainer.run(train_loader, max_epochs=max_epochs)

    if cross_entropy_state_dicts:
        training_log["cross_entropy_best_epoch"] = cross_entropy_pws.best_epoch
    else:
        cross_entropy_state_dicts = ModelOptimizerStateDicts(
            model_state_dict=model.state_dict(), optimizer_state_dict=optimizer.state_dict()
        )

    if accuracy_state_dicts:
        training_log["cross_entropy_best_epoch"] = cross_entropy_pws.best_epoch
    else:
        accuracy_state_dicts = ModelOptimizerStateDicts(
            model_state_dict=model.state_dict(), optimizer_state_dict=optimizer.state_dict()
        )

    return DoubleSnapshots(accuracy_state_dicts, cross_entropy_state_dicts)

# Cell


def evaluate(*, model: TrainedModel, loader, num_samples, device, loss=None):
    log_probs_N_K_C, labels_N = model.get_log_probs_N_K_C_labels_N(loader=loader, num_samples=num_samples, device=device)


    if loss is None:
        loss = nn.NLLLoss()

    log_prob_mean_N_C = get_log_mean_probs(log_probs_N_K_C)
    crossentropy = loss(log_prob_mean_N_C, labels_N)
    accuracy = torch.sum(torch.eq(torch.argmax(log_prob_mean_N_C, dim=1), labels_N)).item() / len(labels_N)

    return dict(accuracy=accuracy, crossentropy=crossentropy)


def evaluate_old(*, model, num_samples, loader, device, loss=None):
    # TODO: rewrite this on top of TrainedModel?
    # Add "get_log_prob_predictions" which returns the mean?
    # Compute accuracy etc based on that?

    # Move model to device
    model.to(device)

    evaluation_model = GeometricMeanPrediction(SamplerModel(model, num_samples))

    if loss is None:
        loss = nn.NLLLoss()

    metrics = create_metrics(loss)

    evaluator = create_supervised_evaluator(evaluation_model, metrics=metrics, device=device)

    ProgressBar(persist=False).attach(
        evaluator,
        metric_names="all",
        event_name=Events.ITERATION_COMPLETED(every=LOG_INTERVAL),
    )

    # Kick everything off
    evaluator.run(loader, max_epochs=1)

    return evaluator.state.metrics


def create_metrics(loss):
    return {"accuracy": Accuracy(), "crossentropy": Loss(loss)}