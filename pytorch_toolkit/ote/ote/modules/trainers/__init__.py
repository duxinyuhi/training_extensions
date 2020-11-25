from .base import BaseTrainer
from .mmaction import MMActionTrainer
from .mmdetection import MMDetectionTrainer
from .reid import ReidTrainer

__all__ = [
    'BaseTrainer',
    'MMActionTrainer',
    'MMDetectionTrainer',
    'ReidTrainer',
]
