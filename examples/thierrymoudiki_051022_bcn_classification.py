# -*- coding: utf-8 -*-
"""thierrymoudiki_051022_bcn_classification.ipynb

# 0 - Import packages
"""

!pip install BCN

!pip install the-teller

!pip install scikit-learn numpy

import BCN as bcn # takes a long time to run, ONLY the first it's run
import teller as tr
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer, load_wine, load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from time import time

"""# 1 - Classification examples

# 1 - 1 Wine dataset
"""

dataset = load_wine()
X = dataset.data
y = dataset.target

# split data into training test and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, random_state=13)

start = time()

regr = bcn.BCNClassifier(**{'B': 997, 'nu': 0.41495419042481907,
                            'col_sample': 0.8689119373551017,
                            'lam': 5576.803238697929,
                            'r': 0.8758007308806657,
                            'tol': 1.789513049473953e-08})

regr.fit(X_train, y_train)

print(f"\nElapsed {time() - start}") 

preds = regr.predict(X_test)

# Test set accuracy
print(np.mean(y_test == preds))

print(metrics.classification_report(y_test, preds))

"""# 1 - 2 Breast cancer dataset"""

dataset = load_breast_cancer()
X = dataset.data
y = dataset.target

# split data into training test and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, random_state=13)

start = time()

regr = bcn.BCNClassifier(**{'B': 224, 'nu': 0.6287649668521799, 
                            'col_sample': 0.8472037961052999, 
                            'lam': 0.6900227993008684, 
                            'r': 0.942265267528241, 
                            'tol': 0.0023086390802266204})

regr.fit(X_train, y_train)

print(f"\nElapsed {time() - start}") 

preds = regr.predict(X_test)

# Test set accuracy
print(np.mean(y_test == preds))

print(metrics.classification_report(y_test, preds))

"""# 1 - 3 iris dataset"""

dataset = load_iris()
X = dataset.data
y = dataset.target

# split data into training test and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, random_state=13)

start = time()

regr = bcn.BCNClassifier(**{'B': 246, 'nu': 1.531297749915455, 
                            'col_sample': 0.9111422409364928, 
                            'lam': 3.367488375051336, 
                            'r': 0.8254366770501732, 
                            'tol': 2.2080314922763116e-06})

regr.fit(X_train, y_train)

print(f"\nElapsed {time() - start}") 

preds = regr.predict(X_test)

# Test set accuracy
print(np.mean(y_test == preds))

print(metrics.classification_report(y_test, preds))
