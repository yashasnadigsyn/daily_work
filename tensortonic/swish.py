import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x_arr = np.asarray(x)
    sigmoid = (1) / (1 + np.exp(-x_arr))
    swish = x_arr * sigmoid
    if swish.ndim == 0:
        return np.atleast_1d(swish)
    return swish

print(swish(0.0))