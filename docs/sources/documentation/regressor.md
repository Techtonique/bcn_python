# Regressor

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNRegressor.py#L47)</span>

### BCNRegressor


```python
BCN.BCNRegressor.BCNRegressor(
    B=10,
    nu=0.4,
    col_sample=1,
    lam=0.1,
    r=0.9,
    tol=1e-10,
    type_optim="nlminb",
    activation="sigmoid",
    hidden_layer_bias=True,
    verbose=0,
    show_progress=True,
    seed=123,
)
```


BCN (Boosted Configuration Networks) regression model

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


----

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNRegressor.py#L104)</span>

### fit


```python
BCNRegressor.fit(X, y, **kwargs)
```


Fit BCN (Boosted Configuration Networks) regression model

Parameters:

    X: {ndarray} of shape (n_samples, n_features)
        Training data.

    y: ndarray of shape (n_samples,) 
        Target values.


----

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNRegressor.py#L134)</span>

### predict


```python
BCNRegressor.predict(X, **kwargs)
```


Predict using BCN (Boosted Configuration Networks) regression model

Parameters:

    X: array-like, shape (n_samples, n_features)
        Test data.


----

