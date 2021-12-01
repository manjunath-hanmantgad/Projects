# imports and definitions
import numpy as np
import pandas as pd
#adding import for pickle
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# for random functions
seed_number = 123

# load the dataset to pandas
# method 1 - import from sklearn
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# # method 2 - read the csv
# data_path = "data/iris.csv"
# df = pd.read_csv(data_path, header=0)
# get train/test splits

test_proportion = 0.3
X_train, X_test, y_train, y_test = train_test_split(
    df[iris.feature_names],
    iris.target,
    test_size=test_proportion,
    stratify=iris.target,
    random_state=seed_number,
)

# define the model
n_trees = 100
rf = RandomForestClassifier(
    n_estimators=n_trees, oob_score=True, random_state=seed_number
)

# train the model
rf.fit(X_train, y_train)

# score our model and print the output
predicted = rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted)

# adding the pickle statements

pickle_save = 'rf-model.pkl'
with open(pickle_save, 'wb') as file:
    pickle.dump(rf, file)

#print(
#    "Out-of-bag score estimate: {0:.3f}\n"
#    "Mean accuracy score: {1:.3f}".format(rf.oob_score_, accuracy
#    )
#)