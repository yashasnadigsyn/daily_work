import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    if x.ndim == 2:
        maxi = np.max(x, axis=1, keepdims=True)
        num = np.exp(x - maxi)
        den = np.sum(num, axis=1, keepdims=True)
        return num/den
    else:
        maxi = np.max(x, axis=0, keepdims=True)
        num = np.exp(x - maxi)
        den = np.sum(num, axis=0, keepdims=True)
        return num/den

print(softmax(np.array([1, 2, 3])))