import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    e = y_true - y_pred
    L = np.where(np.abs(e) <= delta, (1/2)*(e)**2, delta*(np.abs(e) - (1/2)*delta))
    return np.mean(L)