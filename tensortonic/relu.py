import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x_arr = np.asarray(x)
    if x_arr.ndim == 0:
        return np.atleast_1d(np.maximum(0.0, x_arr))
    return np.maximum(0.0, x_arr)

print(relu(5.0))