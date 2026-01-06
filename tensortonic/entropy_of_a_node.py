import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y_arr = np.asarray(y)
    counts = np.unique(y_arr, return_counts=True)
    N = len(y_arr)
    HS = (counts[1]/N) * (np.log2(counts[1]/N))
    HS_sum = -1 * np.sum(HS)
    return HS_sum
    
print(entropy_node([1,1,1,1]))