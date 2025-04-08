import numpy as np

def constraint():
    lb = np.array([1.1,1.1,0.0,0.0])
    ub = np.array([4,4,1,1])
    return lb,ub


def func(x):
    g1 = 0.610262*(x[0]*x[1]-x[2]*x[3]) + 8.64 - (x[0]*x[1]**3 - x[2]*x[3]**3)
    g2 = 40000 - 1713.481*(x[0]*x[1]**3 - x[2]*x[3]**3)
    g3 = 40000 - 1713.481*(x[1]*x[0]**3 - x[3]*x[2]**3)
    g4 = x[2] - x[0]
    g5 = x[3] - x[1]
    if g1 > 0 or g2 > 0 or g3 > 0 or g4 > 0 or g5 > 0:
        z = 34.08*(x[0]*x[1]-x[2]*x[3]) + 10**9 * (np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4])+np.max([0,g5]))
    else:
        z = 34.08*(x[0]*x[1]-x[2]*x[3])
    return z