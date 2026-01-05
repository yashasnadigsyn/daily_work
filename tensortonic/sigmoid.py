import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    X_arr = np.asarray(x, dtype=float)
    sigmoid_x = (1) / (1 + np.exp(-X_arr))
    return sigmoid_x
