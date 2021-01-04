# AUTOGENERATED! DO NOT EDIT! File to edit: 07_black_box_training.ipynb (unless otherwise specified).

__all__ = ['train', 'evaluate', 'create_metrics', 'LOG_INTERVAL', 'get_predictions']

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
from toma import toma
from torch import nn
from tqdm.auto import tqdm

from .consistent_mc_dropout import (
    GeometricMeanPrediction,
    SamplerModel,
    multi_sample_loss,
)
from .restoring_early_stopping import RestoringEarlyStopping

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
    training_log: dict,
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

    training_log["epochs"] = []
    epochs_log = training_log["epochs"]

    # Logging
    @validation_evaluator.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        metrics = dict(engine.state.metrics)
        epochs_log.append(metrics)

    # Add early stopping
    if patience is not None:
        early_stopping = RestoringEarlyStopping(
            patience=patience,
            score_function=lambda: float(-validation_evaluator.state.metrics["crossentropy"]),
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


@torch.no_grad()
def get_predictions(*, model, num_samples, num_classes, loader, device: str):
    model.to(device=device)

    N = len(loader.dataset)
    predictions = torch.empty((N, num_samples, num_classes), dtype=float, device="cpu")

    pbar = tqdm(total=N * num_samples, desc="get_predictions", leave=False)

    @toma.execute.range(0, num_samples, 128)
    def get_prediction_batch(start, end):
        if start == 0:
            pbar.reset()

        model.eval()

        prediction_model = SamplerModel(model, end - start)

        data_start = 0
        for batch_x, _ in loader:
            batch_x = batch_x.to(device=device)

            batch_predictions = prediction_model(batch_x)

            batch_size = len(batch_predictions)
            data_end = data_start + batch_size

            predictions[data_start:data_end, start:end].copy_(batch_predictions.float(), non_blocking=True)

            data_start = data_end

            pbar.update(batch_size * (end - start))

    pbar.close()

    return predictions