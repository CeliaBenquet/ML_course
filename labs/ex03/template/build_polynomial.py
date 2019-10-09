# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np

def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data

    matrix=np.ones((len(x),1))
    
    for j in range(1, degree+1):
        matrix = np.c_[matrix, x**(j)]
    
    return matrix 
    # ***************************************************
    #raise NotImplementedError