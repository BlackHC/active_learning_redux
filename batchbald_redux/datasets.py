# AUTOGENERATED! DO NOT EDIT! File to edit: 05c_more_datasets.ipynb (unless otherwise specified).

__all__ = ['SplitDataset', 'SplitDataLoader', 'train_validation_split', 'get_SVHN', 'get_CIFAR10', 'get_CIFAR100',
           'CIFAR10_NORMALIZE', 'get_dataset', 'get_dataloaders', 'get_dataloaders_by_name', 'dataset_factories']

# Cell

from dataclasses import dataclass

import kornia.augmentation as K
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from torch import nn
from torch.utils import data
from torchvision import datasets, transforms

from .fast_mnist import FastMNIST

from .dataset_challenges import NamedDataset

# Cell


@dataclass
class SplitDataset:
    input_size: int
    num_classes: int
    options: dict

    train: data.Dataset
    validation: data.Dataset
    test: data.Dataset

    train_augmentations: nn.Sequential


@dataclass
class SplitDataLoader:
    input_size: int
    num_class: int
    options: dict

    train: data.DataLoader
    validation: data.DataLoader
    test: data.DataLoader

    train_augmentations: nn.Sequential

# Cell


def train_validation_split(
    *, full_train_dataset, full_validation_dataset, train_labels, validation_set_size, validation_split_random_state
):
    # Split off validation set
    if validation_set_size > 0:
        cv = StratifiedShuffleSplit(
            n_splits=1, test_size=validation_set_size, random_state=validation_split_random_state
        )
        for train_indices, validation_indices in cv.split(
            X=np.zeros(len(full_train_dataset)), y=np.asarray(train_labels)
        ):
            pass
    else:
        # Always wrap the dataset in a subset so there
        train_indices = list(range(len(full_train_dataset)))
        validation_indices = []

    train_dataset = data.Subset(full_train_dataset, train_indices)
    validation_dataset = data.Subset(full_validation_dataset, validation_indices)

    return train_dataset, validation_dataset

# Cell

CIFAR10_NORMALIZE = transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))


def get_SVHN(root, validation_set_size, validation_split_random_state, normalize_like_cifar10):
    input_size = 32
    num_classes = 10

    # NOTE: these are not correct mean and std for SVHN, but are commonly used
    normalize = CIFAR10_NORMALIZE if normalize_like_cifar10 else transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    transform = transforms.Compose([transforms.ToTensor(), normalize])

    full_train_dataset = datasets.SVHN(root + "/SVHN", split="train", transform=transform, download=True)
    full_validation_dataset = datasets.SVHN(root + "/SVHN", split="train", transform=transform, download=True)

    train_dataset, validation_dataset = train_validation_split(
        full_train_dataset=full_train_dataset,
        full_validation_dataset=full_validation_dataset,
        train_labels=full_train_dataset.labels,
        validation_set_size=validation_set_size,
        validation_split_random_state=validation_split_random_state,
    )

    test_dataset = datasets.SVHN(root + "/SVHN", split="test", transform=transform, download=True)
    return SplitDataset(
        input_size,
        num_classes,
        dict(
            validation_split_random_state=validation_split_random_state,
            normalize_like_cifar10=normalize_like_cifar10,
        ),
        NamedDataset(
            train_dataset, f"SVHN (Train, seed={validation_split_random_state}, {len(train_dataset)} samples)"
        ),
        NamedDataset(
            validation_dataset,
            f"SVHN (Validation, seed={validation_split_random_state}, {len(validation_dataset)} samples)",
        ),
        NamedDataset(test_dataset, "SVHN (Test)"),
        nn.Sequential()
    )


def get_CIFAR10(root, validation_set_size, validation_split_random_state, normalize_like_cifar10):
    input_size = 32
    num_classes = 10

    dataset_transform = transforms.Compose(
        [
            transforms.ToTensor(),
            CIFAR10_NORMALIZE,
        ]
    )

    train_augmentations = nn.Sequential(
        K.RandomCrop((32, 32), padding=4),
        K.RandomHorizontalFlip(),
    )

    full_train_dataset = datasets.CIFAR10(root + "/CIFAR10", train=True, transform=dataset_transform, download=True)
    full_validation_dataset = datasets.CIFAR10(
        root + "/CIFAR10", train=True, transform=dataset_transform, download=True
    )

    train_dataset, validation_dataset = train_validation_split(
        full_train_dataset=full_train_dataset,
        full_validation_dataset=full_validation_dataset,
        train_labels=full_train_dataset.targets,
        validation_set_size=validation_set_size,
        validation_split_random_state=validation_split_random_state,
    )

    test_dataset = datasets.CIFAR10(root + "/CIFAR10", train=False, transform=dataset_transform, download=True)

    return SplitDataset(
        input_size,
        num_classes,
        dict(
            validation_split_random_state=validation_split_random_state,
            normalize_like_cifar10=True,
        ),
        NamedDataset(
            train_dataset, f"CIFAR-10 (Train, seed={validation_split_random_state}, {len(train_dataset)} samples)"
        ),
        NamedDataset(
            validation_dataset,
            f"CIFAR-10 (Validation, seed={validation_split_random_state}, {len(validation_dataset)} samples)",
        ),
        NamedDataset(test_dataset, "CIFAR-10 (Test)"),
        train_augmentations
    )


def get_CIFAR100(root, validation_set_size, validation_split_random_state, normalize_like_cifar10):
    input_size = 32
    num_classes = 100

    normalize = (
        CIFAR10_NORMALIZE
        if normalize_like_cifar10
        else transforms.Normalize((0.5071, 0.4866, 0.4409), (0.2673, 0.2564, 0.2762))
    )

    dataset_transform = transforms.Compose(
        [
            transforms.ToTensor(),
            normalize,
        ]
    )

    train_augmentations = nn.Sequential(
        K.RandomCrop((32, 32), padding=4),
        K.RandomHorizontalFlip(),
    )

    full_train_dataset = datasets.CIFAR100(root + "/CIFAR100", train=True, transform=dataset_transform, download=True)
    full_validation_dataset = datasets.CIFAR100(
        root + "/CIFAR100", train=True, transform=dataset_transform, download=False
    )

    train_dataset, validation_dataset = train_validation_split(
        full_train_dataset=full_train_dataset,
        full_validation_dataset=full_validation_dataset,
        train_labels=full_train_dataset.targets,
        validation_set_size=validation_set_size,
        validation_split_random_state=validation_split_random_state,
    )

    test_dataset = datasets.CIFAR100(root + "/CIFAR100", train=False, transform=dataset_transform, download=False)

    return SplitDataset(
        input_size,
        num_classes,
        dict(
            validation_split_random_state=validation_split_random_state,
            normalize_like_cifar10=normalize_like_cifar10,
        ),
        NamedDataset(
            train_dataset, f"CIFAR-100 (Train, seed={validation_split_random_state}, {len(train_dataset)} samples)"
        ),
        NamedDataset(
            validation_dataset,
            f"CIFAR-100 (Validation, seed={validation_split_random_state}, {len(validation_dataset)} samples)",
        ),
        NamedDataset(test_dataset, "CIFAR-100 (Test)"),
        train_augmentations
    )

# Cell

dataset_factories = {
    "SVHN": get_SVHN,
    "CIFAR-10": get_CIFAR10,
    "CIFAR-100": get_CIFAR100,
}


def get_dataset(
    name: str,
    *,
    root=None,
    validation_set_size=0,
    validation_split_random_state=0,
    normalize_like_cifar10=False,
):
    root = root if root is not None else "./"
    validation_set_size = validation_set_size if validation_set_size is not None else 0
    validation_split_random_state = validation_split_random_state if validation_split_random_state is not None else 0
    normalize_like_cifar10 = normalize_like_cifar10 if normalize_like_cifar10 is not None else False

    split_dataset = dataset_factories[name](
        root, validation_set_size, validation_split_random_state, normalize_like_cifar10
    )
    return split_dataset


def get_dataloaders(split_dataset: SplitDataset, *, train_batch_size=128, eval_batch_size=512, train_shuffle=True):
    kwargs = {"num_workers": 4, "pin_memory": True}

    train_loader = data.DataLoader(split_dataset.train, batch_size=train_batch_size, shuffle=train_shuffle, **kwargs)

    validation_loader = data.DataLoader(split_dataset.validation, batch_size=eval_batch_size, shuffle=False, **kwargs)
    test_loader = data.DataLoader(split_dataset.test, batch_size=eval_batch_size, shuffle=False, **kwargs)

    return SplitDataLoader(
        split_dataset.input_size,
        split_dataset.num_classes,
        split_dataset.options,
        train_loader,
        validation_loader,
        test_loader,
        split_dataset.train_augmentations
    )


def get_dataloaders_by_name(
    name: str,
    *,
    normalize_like_cifar10,
    root=None,
    validation_set_size=None,
    validation_split_random_state=None,
    train_batch_size=128,
    eval_batch_size=512,
    train_shuffle=True,
):
    split_dataset = get_dataset(
        name,
        root=root,
        validation_set_size=validation_set_size,
        validation_split_random_state=validation_split_random_state,
        normalize_like_cifar10=normalize_like_cifar10,
    )

    split_dataloaders = get_dataloaders(
        split_dataset, train_batch_size=train_batch_size, eval_batch_size=eval_batch_size, train_shuffle=train_shuffle
    )

    return split_dataloaders