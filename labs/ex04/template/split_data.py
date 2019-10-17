# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


import math

def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    num_row = y.shape[0]
    y_random=np.zeros(num_row)
    x_random=np.zeros(num_row)
    # split the data based on the given ratio
    indices = np.random.permutation(num_row)
    for i in range(len(indices)): 
        y_random[i]=y[indices[i]]
        x_random[i]=x[indices[i]]
    sep_row = math.floor(ratio * num_row)
    y_tr = y_random[:sep_row]
    x_tr = x_random[:sep_row]
    y_te = y_random[sep_row:]
    x_te = x_random[sep_row:]
    
    return y_tr, x_tr, y_te, x_te