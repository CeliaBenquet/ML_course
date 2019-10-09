# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

def compute_loss(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    # TODO: compute loss by MSE
    N=y.shape[0]
    e=y-tx.dot(w)
    return 1/(2*N)*np.sum(e**2,axis=0)