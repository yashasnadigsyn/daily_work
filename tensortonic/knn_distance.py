import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    
    if X_train.ndim == 1: X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1: X_test = X_test.reshape(-1, 1)
    
    n_train = X_train.shape[0]
    n_test = X_test.shape[0]
    
    diff = X_test[:, np.newaxis, :] - X_train[np.newaxis, :, :]
    dist = np.linalg.norm(diff, axis=2)
    k_limit = min(k, n_train)
    k_nearest = np.argsort(dist, axis=1)[:, :k_limit]
    
    if k > n_train:
        padding = np.full((n_test, k-n_train), -1)
        k_nearest = np.concatenate([k_nearest, padding], axis=1)
        
    return k_nearest.astype(int)
    
X_train=[1,3,5]
X_test=[2]
k=2
print(knn_distance(X_train, X_test, k))

X_train=[[0,0],[1,1],[2,2]]
X_test=[[0.5,0.5]]
k=2
print(knn_distance(X_train, X_test, k))