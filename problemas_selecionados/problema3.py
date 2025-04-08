import numpy as np

def constraint():
    lb = np.array([0])
    ub = np.array([5])
    return lb,ub

def func(x):
    nu = 0.3
    z = - 0.5*(0.5*(1-2*nu)+(1+nu)*x[0]/((1+x[0]**2)**0.5)-(3/2)*(x[0]**3 / ((1+x[0]**2)**0.5)**3))
    return z   