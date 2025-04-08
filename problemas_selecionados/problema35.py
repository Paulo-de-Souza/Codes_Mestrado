import numpy as np

def constraint():
    # definindo h, l, t, b
    lb = np.array([0.0,0.0,10,10])
    ub = np.array([100,100,200,200])
    return lb,ub

def func(x):
    # variaveis do problema
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193*x3
    g2 = -x2 + 0.00954*x3
    g3 = -np.pi*(x3**2)*x4 - (4/3)*np.pi*(x3**3) + 1296000
    g4 = x4 - 240
    f = 0.6224*x1*x3*x4 + 1.7781*x2*(x3**2) + 3.1661*(x1**2)*x4 + 19.84*(x1**2)*x3
    if g1 > 0 or g2 > 0 or g3 > 0 or g4 > 0:
        z = f + (10**7)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4]))
    else:
        z = f
    return z
