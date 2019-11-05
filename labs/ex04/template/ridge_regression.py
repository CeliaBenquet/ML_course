# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np

def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""

    """implement ridge regression."""
    aI = 2 * tx.shape[0] * lambda_ * np.identity(tx.shape[1])
    a = tx.T.dot(tx) + aI
    b = tx.T.dot(y)
    w_ridge = np.linalg.solve(a, b)
    
    return w_ridge #only return the optimal w : no chosen loss 
