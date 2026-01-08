import numpy as np

def gini_impurity(y_left, y_right):
    y_left, y_right = np.asarray(y_left), np.asarray(y_right)
    NL, NR = len(y_left), len(y_right)
    N = NL + NR
    
    if N == 0: return 0.0 

    def node_gini(y, n):
        if n == 0: return 0.0
        _, counts = np.unique(y, return_counts=True)
        return 1.0 - np.sum(np.square(counts / n))

    gini_split = (NL / N) * node_gini(y_left, NL) + (NR / N) * node_gini(y_right, NR)
    return float(gini_split)

y_left=[]
y_right=[0,1]
print(gini_impurity(y_left, y_right))