===
BCN
===


.. image:: https://img.shields.io/pypi/v/BCN.svg
        :target: https://pypi.python.org/pypi/BCN

.. image:: https://img.shields.io/pypi/l/BCN
        :target: https://github.com/Techtonique/bcn_python/blob/main/LICENSE

.. image:: https://pepy.tech/badge/BCN
        :target: https://pepy.tech/project/BCN

.. image:: https://img.shields.io/badge/documentation-is_here-green
        :target: https://techtonique.github.io/bcn_python/   


This package contains an implementation of **Boosted Configuration (*neural*) Networks** 
(BCNs). How do BCNs work? By creating ensembles (boosting in a supervised way) of single-layered 
feedforward (*neural*) Networks.

It's worth mentioning that this Python package is built on top of the `R package`_, thanks 
to ``rpy2``.

Installing BCN
--------

* the **development** version: ``pip install -U git+https://github.com/Techtonique/bcn_python.git``

* the **stable** version: ``pip install BCN``


Using BCN 
--------

As of 08/12/2022, the package's interface contains two classes: ``BCNClassifier`` 
and ``BCNRegressor``. If you're familiar with scikit-learn, then using the package 
will be straightforward (you can use ``fit``, ``predict``, ``cross_val_score``, 
``GridSearchCV``, etc.), as demo'ed in the following example. Otherwise, it's 
relatively easy to grasp.


* BCN for Classification::

        import BCN as bcn # this line takes a long time to run, ONLY the first time it's run
        import numpy as np
        from sklearn.datasets import load_breast_cancer
        from sklearn.model_selection import train_test_split
        from sklearn import metrics


        dataset = load_breast_cancer()
        X = dataset.data
        y = dataset.target

        # split data into training test and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, random_state=123)

        clf = bcn.BCNClassifier(**{'B': 237,
        'activation': 'sigmoid',
        'col_sample': 0.9628819950928769,
        'lam': 0.6163764764960539,
        'nu': 0.6683372199442862,
        'r': 0.9199609524470921,
        'tol': 4.8550370180201114e-06})

        clf.fit(X_train, y_train)

        preds = clf.predict(X_test)

        print(np.mean(y_test == preds))

        print(metrics.classification_report(preds, y_test))

* BCN for Regression

        BCN for Regression works exactly the same way as BCN for Classification. You just need to 
        use a **continuous response** ``y`` as input (no integers in the response).

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`R package`: https://techtonique.r-universe.dev/ui#package:bcn
