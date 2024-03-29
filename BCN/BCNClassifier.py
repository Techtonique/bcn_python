import numpy as np
import rpy2.robjects.packages as rpackages
import subprocess

from rpy2.robjects.packages import importr
from rpy2.robjects import ListVector
from rpy2.robjects.vectors import StrVector
from rpy2.robjects import numpy2ri, default_converter, r
from rpy2.robjects.conversion import localconverter
from rpy2.robjects import NULL as rNULL

from sklearn.base import BaseEstimator
from sklearn.base import ClassifierMixin


r['options'](warn=-1)

# Install R packages
commands1_lm = 'base::system.file(package = "bcn")' # check is installed 
commands2_lm = 'base::system.file("bcn_r", package = "bcn")' # check is installed locally 
exec_commands1_lm = subprocess.run(['Rscript', '-e', commands1_lm], capture_output=True, text=True)
exec_commands2_lm = subprocess.run(['Rscript', '-e', commands2_lm], capture_output=True, text=True)

if (len(exec_commands1_lm.stdout) == 7 and len(exec_commands2_lm.stdout) == 7): # kind of convoluted, but works    

    required_packages = ["Rcpp", "dfoptim", "bcn"]  # list of required R packages

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
                    CRAN="https://cran.rstudio.com/",
                )
            )
            try: 
                utils.install_packages(StrVector(packages_to_install))
            except Exception as e1:
                try: 
                    subprocess.run(['mkdir', '-p', 'bcn_r'])
                    utils.install_packages(StrVector(packages_to_install), lib_loc = StrVector(['bcn_r']))
                except Exception as e2:
                    subprocess.run(["mkdir", "-p", "bcn_r"], check=True)
                    command1 = "Rscript -e \"try(utils::install.packages(c('Rcpp', 'dfoptim'), lib='bcn_r', repos='https://cran.rstudio.com', dependencies = TRUE), silent=TRUE)\""
                    subprocess.run(command1, shell=True, check=True)
                    command2 = "Rscript -e \"try(utils::install.packages('bcn', lib='bcn_r', repos='https://techtonique.r-universe.dev', dependencies = TRUE), silent=TRUE)\""
                    subprocess.run(command2, shell=True, check=True)

            check_packages = True

base = importr("base")
try: 
    bcn = importr("bcn")
except Exception as e:
    bcn = importr("bcn", lib_loc = 'bcn_r')
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
          With 0 < r < 1. Controls the convergence rate of residuals.
      tol: float
          Convergence tolerance for an early stopping
      n_clusters: int
            Number of clusters (k-means for now).
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
                n_clusters = None,
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
    self.n_clusters = n_clusters
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
    self.classes_ = np.unique(y)
    self.n_classes_ = len(self.classes_)
    # cf. https://rpy2.github.io/doc/latest/html/numpy.html
    # Create a converter that starts with rpy2's default converter
    # to which the numpy conversion rules are added.
    np_cv_rules = localconverter(default_converter + numpy2ri.converter)

    with np_cv_rules:
        # Anything here and until the `with` block is exited
        # will use our numpy converter whenever objects are
        # passed to R or are returned by R while calling
        # rpy2.robjects functions.
        self.obj = bcn.bcn(x = X, y = y, 
                       B = self.B, 
                       nu = self.nu,
                       col_sample = self.col_sample,
                       lam = self.lam,
                       r = self.r,
                       tol = self.tol,
                       n_clusters = rNULL if self.n_clusters is None else int(self.n_clusters),
                       type_optim = self.type_optim,
                       activation = self.activation,
                       hidden_layer_bias = self.hidden_layer_bias,
                       verbose = self.verbose,
                       show_progress = self.show_progress,
                       seed = self.seed                       
                       )    
    return self

  def predict_proba(self, X): 
    """Predict probabilities using BCN (Boosted Configuration Networks) classification model

    Parameters:

        X: array-like, shape (n_samples, n_features)
            Training data.
    """           
    assert self.obj is not None, "you must call `fit` before trying to predict"    

    # cf. https://rpy2.github.io/doc/latest/html/numpy.html
    # Create a converter that starts with rpy2's default converter
    # to which the numpy conversion rules are added.
    np_cv_rules = localconverter(default_converter + numpy2ri.converter)

    with np_cv_rules:
        # Anything here and until the `with` block is exited
        # will use our numpy converter whenever objects are
        # passed to R or are returned by R while calling
        # rpy2.robjects functions.
        r_obj = ListVector(self.obj)
        r_obj.do_slot_assign("class", StrVector(["bcn"]))
        return np.asarray(bcn.predict_bcn(r_obj, X, type="probs"))

  def predict(self, X):
    """Predict using BCN (Boosted Configuration Networks) classification model

    Parameters:

        X: array-like, shape (n_samples, n_features)
            Test data.
    """           
    return np.asarray(np.argmax(self.predict_proba(X), axis=1))
