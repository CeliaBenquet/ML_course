# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    
    gram=(tx.T).dot(tx)
    txy = (tx.T).dot(y)
    w = np.linalg.solve(gram,txy)
    N = y.shape[0]
    e = y-tx.dot(w)
    MSE = 1/(2*N) * (e.T).dot(e)
    
    return MSE, w 
    
