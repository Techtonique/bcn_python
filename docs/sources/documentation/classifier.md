# Classifier

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNClassifier.py#L47)</span>

### BCNClassifier


```python
BCN.BCNClassifier.BCNClassifier(
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

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNClassifier.py#L75)</span>

### fit


```python
BCNClassifier.fit(X, y, **kwargs)
```


----

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNClassifier.py#L99)</span>

### predict


```python
BCNClassifier.predict(X, **kwargs)
```


----

<span style="float:right;">[[source]](https://github.com/Techtonique/bcn_python/BCN/BCNClassifier.py#L94)</span>

### predict_proba


```python
BCNClassifier.predict_proba(X, **kwargs)
```


----

