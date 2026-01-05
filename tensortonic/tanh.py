import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x_arr = np.asarray(x)
    if x_arr.ndim == 0:
        return np.atleast_1d((np.exp(x_arr) - np.exp(-x_arr))/(np.exp(x_arr) + np.exp(-x_arr)))
    return (np.exp(x_arr) - np.exp(-x_arr))/(np.exp(x_arr) + np.exp(-x_arr))

print(tanh(0.0))