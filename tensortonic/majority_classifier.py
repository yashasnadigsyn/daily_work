import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    y_train = np.asarray(y_train)
    values, counts = np.unique(y_train, return_counts=True)
    maxi = values[np.argmax(counts)]
    return np.full(len(X_test), maxi)

print(majority_classifier([0,0,1,1], [10,20]))