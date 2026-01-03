import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x_arr, y_arr = np.asarray(x), np.asarray(y)
    dist = np.sqrt(np.sum(np.square(x_arr - y_arr)))   
    return dist
