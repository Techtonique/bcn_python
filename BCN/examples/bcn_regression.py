import BCN as bcn
import numpy as np 
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from time import time
from sklearn import metrics


diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# split data into training test and test set
np.random.seed(15029)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2)

start = time()
clf = bcn.BCNRegressor(show_progress=True).fit(X_train, y_train)
print(f"\nElapsed {time() - start}") 

print(y_train.dtype)

print(clf.obj.rx2['type_problem'])

preds = clf.predict(X_test)

print(preds)

print(y_test)

print(np.sqrt(np.mean((y_test - preds)**2)))