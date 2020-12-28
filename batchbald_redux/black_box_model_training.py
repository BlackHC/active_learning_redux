# AUTOGENERATED! DO NOT EDIT! File to edit: 07_black_box_training.ipynb (unless otherwise specified).

__all__ = ['train', 'create_metrics', 'LOG_INTERVAL', 'handler_save_predictions', 'get_predictions']

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

# Cell


LOG_INTERVAL = 10


def train(
    *,
    model,
    val_model,
    train_loader,
    val_loader,
    test_loader,
    patience: Optional[int],
    max_epochs: int,
    device: str,
    epochs_log: list,
    loss=None,
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
        loss = nn.CrossEntropyLoss()

    # Move model to device before creating the optimizer
    model.to(device)

    if optimizer is None:
        optimizer = torch.optim.Adam(model.parameters(), weight_decay=5e-4)

    trainer = create_supervised_trainer(model, optimizer, loss, device=device)

    metrics = create_metrics(loss)

    validation_evaluator = create_supervised_evaluator(val_model, metrics=metrics, device=device)

    @trainer.on(Events.EPOCH_COMPLETED)
    def compute_metrics(engine):
        validation_evaluator.run(val_loader)

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

    # Add early stopping
    if patience is not None:
        add_early_stopping_by_val_score(patience, validation_evaluator, trainer, "crossentropy")

    # Kick everything off
    trainer.run(train_loader, max_epochs=max_epochs)

    # Return the optimizer in case we want to continue training.
    return optimizer


def create_metrics(loss):
    return {"accuracy": Accuracy(), "crossentropy": Loss(loss)}

# Cell


def handler_save_predictions(engine, target_list):
    @engine.on(Events.ITERATION_COMPLETED)
    def iteration_completed(engine):
        target_list.extend(engine.state.output[0])


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