import numpy as np


# Holding period return (hpr)
def hpr(start, end, dividend):
    return (end + dividend - start) / start

def compound_return(hprs):
    return np.prod(hprs + 1) - 1