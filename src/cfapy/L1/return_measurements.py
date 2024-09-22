import numpy as np


# Holding period return (hpr)
def hpr(start, end, dividend):
    return (end + dividend - start) / start

print(hpr(20, 22, 1))  # 0.15