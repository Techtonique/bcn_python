=======
History
=======

0.7.1 (2024-02-06)
------------------

* Add `classes_` attribute to `fit` method in BCNClassifier

0.6.2 (2024-01-25)
------------------

* Add `n_clusters` parameter to `fit` method, to allow for a different number of clusters (for now, only k-means)
* Avoid division by zero when scaling the data

0.5.3 (2023-08-10)
------------------

* Manage dependencies
* Return actual numpy arrays


0.4.0 (2022-08-16)
------------------

* Remove 'direct' method for now
* Improve `verbose` (now an integer in (0, 1, 2, 3))


0.3.1 (2022-08-13)
------------------

* Mirror the R package (remove some dependencies of R package).


0.3.0 (2022-08-12)
------------------

* First release on PyPI.
