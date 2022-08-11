"""Top-level package for BCN."""

__author__ = """T. Moudiki"""
__email__ = 'thierry.moudiki@gmail.com'
__version__ = '0.2.2'

from .BCNClassifier import BCNClassifier
from .BCNRegressor import BCNRegressor

__all__ = ["BCNClassifier", "BCNRegressor"]
