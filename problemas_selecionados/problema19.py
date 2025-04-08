import numpy as np

def constraint():
    # definindo x1 e x2
    lb = np.array([0.04,0.06])
    ub = np.array([0.12,0.20])
    return lb,ub

def func(x):
    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-6
    x[0]+=epsilon
    x[1]+=epsilon

    """ g1 = (0.9/(x[0]*x[1]**2)) - 220
    g2 = ((875.604*10**-9)/(x[0]*x[1]**3)) - 0.02
    g3 = x[0] - x[1] """
    g1 = (0.9/(220*x[0]*x[1]**2)) - 1
    g2 = ((875.604*10**-9)/(0.02*x[0]*x[1]**3)) - 1
    g3 = x[0]/x[1] - 1
    if g1 > 0 or g2 > 0 or g3 > 0:
        z = 76500*x[1]*x[0] + 1.5*10**8 * (np.max([0,g1]) + np.max([0,g2]) + np.max([0,g3]))
    else:
        z = 76500*x[1]*x[0]
    return z

def restricoes(x):
    g1 = (0.9/(220*x[0]*x[1]**2)) - 1
    g2 = ((875.604*10**-9)/(0.02*x[0]*x[1]**3)) - 1
    g3 = x[0]/x[1] - 1
    # g1 = (0.9/(x[0]*x[1]**2)) - 220
    # g2 = ((875.604*10**-9)/(x[0]*x[1]**3)) - 0.02
    # g3 = x[0] - x[1]
    z = 76500*x[1]*x[0]
    G = np.array([g1,g2,g3])
    return z,G