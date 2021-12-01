import pickle

# define the path to the pickled model
model_path = 'rf-model.pkl'

# unpickle the random forest model
with open(model_path, 'rb') as file:
    unpickled_rf = pickle.load(file)

# define a single row of X variables to test the prediction
X_example = [[5.0, 2.0, 3.5, 1.0]]

# run the unpickled model and print the answer
y_example = unpickled_rf.predict(X_example)
print(y_example)