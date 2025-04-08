import numpy as np

def constraint():
    lb = np.array([0,0])
    ub = np.array([0.04,0.04])
    return lb,ub

def func(x):
    A1 = 10**-5
    A2 = A1
    h = 1
    s = 1.5
    L = (h**2+0.25*s**2)**0.5
    W = 10**4
    tt = 30*np.pi/180
    E = 207*10**9
    z = (E*A1/L)*(s/(2*L))**2 * x[0]**2 + (E*A2/L)*(h/L)**2 * x[1]**2 - W*(x[0]*np.cos(tt)+x[1]*np.sin(tt))
    return z