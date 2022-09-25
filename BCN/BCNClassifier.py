import os
import numpy as np
import rpy2.robjects.packages as rpackages

from rpy2.robjects.packages import importr
from rpy2.robjects import IntVector
from rpy2.robjects.vectors import StrVector
from rpy2.robjects import numpy2ri, r

from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin

numpy2ri.activate()

r['options'](warn=-1)

required_packages = ["bcn"]  # list of required R packages

if all(rpackages.isinstalled(x) for x in required_packages):
    check_packages = True  # True if packages are already installed
else:
    check_packages = False  # False if packages are not installed

if check_packages == False:  # Not installed? Then install.

    packages_to_install = [
        x for x in required_packages if not rpackages.isinstalled(x)
    ]

    if len(packages_to_install) > 0:
        base = importr("base")
        utils = importr("utils")
        base.options(
            repos=base.c(
                techtonique="https://techtonique.r-universe.dev",
                CRAN="https://cloud.r-project.org",
            )
        )
        utils.install_packages(StrVector(packages_to_install))
        check_packages = True

base = importr("base")
bcn = importr("bcn")
stats = importr("stats")
utils = importr("utils")

class BCNClassifier(BaseEstimator, ClassifierMixin):
  """BCN (Boosted Configuration Networks) classification model

  Parameters:

      B:  int
          Number of iterations of the algorithm.  
      nu: float
          Learning rate.
      col_sample: float
          Percentage of columns (covariates) adjusted at each iteration of the algorithm.
      lam: float
          Defines lower and upper bounds neural networks weights.
      r: float
          A constant usually > 0.9
      tol: float
          Convergence tolerance for an early stopping
      type_optim: string
          Type of optimization procedure used for finding neural networks weights at each iteration ("nlminb", "nmkb", "hjkb", "bobyqa", "randomsearch")
      activation: string
          Activation function (must be bounded). Currently: "sigmoid", "tanh".
      hidden_layer_bias: boolean
          If there is a bias parameter in neural networks weights. If yes, True (default). 
      verbose: int
          Controls verbosity (for checks). The higher, the more verbose.
      show_progress: boolean
          If True, a progress bar is displayed.
      seed: int
          For reproducibility of results.
  """             
  def __init__(self, B = 10,
                nu = 0.4,
                col_sample = 1,
                lam = 1e-1,
                r = 0.9,
                tol = 0,
                type_optim = "nlminb",
                activation = "sigmoid",
                hidden_layer_bias = True,
                verbose = 0,
                show_progress = True,
                seed = 123):
    self.B = B
    self.nu = nu
    self.col_sample = col_sample
    self.lam = lam
    self.r = r
    self.tol = tol
    self.type_optim = type_optim
    self.activation = activation 
    self.hidden_layer_bias = hidden_layer_bias
    self.verbose = verbose
    self.show_progress = show_progress
    self.seed = seed
    self.obj = None

  def fit(self, X, y, **kwargs):  
    """Fit BCN (Boosted Configuration Networks) classification model

    Parameters:

        X: {ndarray} of shape (n_samples, n_features)
            Training data.

        y: ndarray of shape (n_samples,) 
            Target values.

    """
    X_r = base.matrix(X, nrow=X.shape[0], ncol=X.shape[1])
    y_r = IntVector(y) 
    self.obj = bcn.bcn(x = X_r, y = y_r, 
                       B = self.B, 
                       nu = self.nu,
                       col_sample = self.col_sample,
                       lam = self.lam,
                       r = self.r,
                       tol = self.tol,
                       type_optim = self.type_optim,
                       activation = self.activation,
                       hidden_layer_bias = self.hidden_layer_bias,
                       verbose = self.verbose,
                       show_progress = self.show_progress,
                       seed = self.seed                       
                       )
    return self

  def predict_proba(self, X, **kwargs): 
    """Predict probabilities using BCN (Boosted Configuration Networks) classification model

    Parameters:

        X: array-like, shape (n_samples, n_features)
            Training data.
    """           
    assert self.obj is not None, "you must call `fit` before trying to predict"    
    X_r = base.matrix(X, nrow=X.shape[0], ncol=X.shape[1])
    return bcn.predict_bcn(self.obj, X_r, type="probs")

  def predict(self, X, **kwargs):
    """Predict using BCN (Boosted Configuration Networks) classification model

    Parameters:

        X: array-like, shape (n_samples, n_features)
            Test data.
    """           
    return np.argmax(self.predict_proba(X, **kwargs), axis=1)
