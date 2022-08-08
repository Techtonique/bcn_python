import BCN as bcn
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from time import time


dataset = load_breast_cancer()
X = dataset.data
y = dataset.target

# split data into training test and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, random_state=13)

start = time()
clf = bcn.BCNClassifier(**{'B': 132, 'nu': 0.9009239889175154, 
'col_sample': 0.9272101327262355, 'lam': 0.3634893134414783, 
'r': 0.9447863038069327, 'tol': 2.1760423499366634e-09, 
'type_optim': 'nlminb', 'activation': 'sigmoid'}, show_progress=True).fit(X_train, y_train)
print(f"\nElapsed {time() - start}") 

print(y_train.dtype)

print(clf.obj.rx2["type_problem"])

preds = clf.predict(X_test)

print(preds)

print(y_test)

print(np.mean(y_test == preds))

print(metrics.classification_report(preds, y_test))