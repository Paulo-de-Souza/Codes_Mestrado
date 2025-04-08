import numpy as np

def constraint():
    lb = np.array([0.2,0.2])
    ub = np.array([2.5,2.5])
    return lb,ub

def func(x):
    g1 = 8/(16*x[0]+9*x[1]) - 4.5/(9*x[0]+16*x[1]) - 0.1
    if g1 > 0:
        z = x[0] + x[1] + 15**3 * np.max([0,g1])
    else:
        z = x[0] + x[1]
    return z