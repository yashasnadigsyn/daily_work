import numpy as np
from scipy.special import erf

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x_arr = np.asarray(x)
    cdf = 0.5 * (1.0 + erf(x_arr / np.sqrt(2.0)))
    return x_arr * cdf

gelu(2)