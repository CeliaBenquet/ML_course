# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
        """implement ridge regression."""
        # ***************************************************
        # INSERT YOUR CODE HERE
        # ridge regression: TODO
        gram = (tx.T).dot(tx)
        N = tx.shape[0]
        D = tx.shape[1]
        lambda_tilt = lambda_ * 2*N
        I = np.identity(D)

        w = np.linalg.inv(gram + lambda_tilt.dot(I)).dot(tx.T.dot(y))
        return w

