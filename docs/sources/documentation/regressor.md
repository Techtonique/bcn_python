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


Base class for all estimators in scikit-learn.

Notes
-----
All estimators should specify all the parameters that can be set
at the class level in their ``__init__`` as explicit keyword
arguments (no ``*args`` or ``**kwargs``).


----

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNRegressor.py#L75)</span>

### fit


```python
BCNRegressor.fit(X, y, **kwargs)
```


----

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNRegressor.py#L94)</span>

### predict


```python
BCNRegressor.predict(X, **kwargs)
```


----

