import numpy as np

def constraint():
    lb = np.array([4.5,0.25])
    ub = np.array([9,1.25])
    return lb,ub

Is = 0.816
gama = 386
Sy = 62000
omega = 800
nu = 0.28
ri = 1  
def func(x):
    nu = 0.3
    z = - 0.5*(0.5*(1-2*nu)+(1+nu)*x[0]/((1+x[0]**2)**0.5)-(3/2)*(x[0]**3 / ((1+x[0]**2)**0.5)**3))
    return z