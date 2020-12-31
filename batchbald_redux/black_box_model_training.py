# AUTOGENERATED! DO NOT EDIT! File to edit: 07_black_box_training.ipynb (unless otherwise specified).

__all__ = ['train', 'evaluate', 'create_metrics', 'LOG_INTERVAL', 'handler_save_predictions', 'get_predictions']

# Internal Cell

from typing import Optional

import torch
from ignite.contrib.engines.common import (
    add_early_stopping_by_val_score,
    setup_common_training_handlers,
)
from ignite.contrib.handlers import ProgressBar
from ignite.engine import Events, create_supervised_evaluator, create_supervised_trainer
from ignite.metrics import Accuracy, Loss, RunningAverage
from torch import nn

from .consistent_mc_dropout import (
    GeometricMeanPrediction,
    SamplerModel,
    multi_sample_loss,
)

# Cell


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
    epochs_log: list,
    loss=None,
    validation_loss=None,
    optimizer=None
):
    """
    :param model:
    :param train_loader:
    :param val_loader:
    :param metric_loader: We compute metrics for debugging and introspection purposes with this data.
    :param patience: How many epochs to wait for early-stopping.
    :param max_epochs:
    :param tb_log_dir:
    :param device:
    :return: Optimizer that was used for training.
    """
    if loss is None:
        loss = nn.NLLLoss()
    if validation_loss is None:
        validation_loss = loss

    train_model = SamplerModel(model, training_samples)
    validation_model = GeometricMeanPrediction(SamplerModel(model, validation_samples))

    # Move model to device before creating the optimizer
    train_model.to(device)

    if optimizer is None:
        optimizer = torch.optim.Adam(model.parameters(), weight_decay=5e-4)

    trainer = create_supervised_trainer(train_model, optimizer, multi_sample_loss(loss), device=device)

    metrics = create_metrics(validation_loss)

    validation_evaluator = create_supervised_evaluator(validation_model, metrics=metrics, device=device)

    @trainer.on(Events.EPOCH_COMPLETED)
    def compute_metrics(engine):
        validation_evaluator.run(validation_loader)

    # Only to look nicer.
    RunningAverage(output_transform=lambda x: x).attach(trainer, "crossentropy")

    setup_common_training_handlers(trainer, with_gpu_stats=torch.cuda.is_available(), log_every_iters=LOG_INTERVAL)

    ProgressBar(persist=False).attach(
        validation_evaluator,
        metric_names="all",
        event_name=Events.ITERATION_COMPLETED(every=LOG_INTERVAL),
    )

    # Logging
    @validation_evaluator.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        metrics = dict(engine.state.metrics)
        epochs_log.append(metrics)

    # TODO: use my early stopping module (that restores the module!)
    # Add early stopping
    if patience is not None:
        add_early_stopping_by_val_score(patience, validation_evaluator, trainer, "crossentropy")

    # Kick everything off
    trainer.run(train_loader, max_epochs=max_epochs)

    # Return the optimizer in case we want to continue training.
    return optimizer


def evaluate(*, model, num_samples, loader, device, loss=None):
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

# Cell


def handler_save_predictions(engine, target_list):
    @engine.on(Events.ITERATION_COMPLETED)
    def iteration_completed(engine):
        target_list.extend(engine.state.output[0])


# TODO: ought to add support for toma here (and large k)
def get_predictions(*, model, loader, device: str):
    evaluator = create_supervised_evaluator(model, device=device)

    predictions = []
    handler_save_predictions(evaluator, predictions)

    ProgressBar(persist=False).attach(
        evaluator,
        metric_names="all",
        event_name=Events.ITERATION_COMPLETED(every=LOG_INTERVAL),
    )

    evaluator.run(loader)

    predictions = torch.stack(predictions)
    return predictions