import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    y = np.asarray(y)
    split_mask = np.asarray(split_mask, dtype=bool)
    
    y_left = y[split_mask]
    y_right = y[~split_mask]
    
    n = len(y)
    if n == 0:
        return 0.0
    nL = len(y_left)
    nR = len(y_right)
    
    if nL == 0 or nR == 0:
        return 0.0
    
    parent_entropy = _entropy(y)
    left_entropy = _entropy(y_left)
    right_entropy = _entropy(y_right)
    weighted_child_entropy = (nL / n) * left_entropy + (nR / n) * right_entropy
    return parent_entropy - weighted_child_entropy

    
print(information_gain(y=[0,0,1,1], split_mask=[1,1,0,0]))