import numpy as np

def constraint():
    lb = np.array([0.01,0.01,0.01,0.01,0.01])
    ub = np.array([100,100,100,100,100])
    return lb,ub

def func(x):
    C1 = 0.0624
    C2 = 1
    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-6
    x[0]+=epsilon
    x[1]+=epsilon
    x[2]+=epsilon
    x[3]+=epsilon
    x[4]+=epsilon

    g1 = 61/x[0]**3 + 37/x[1]**3 + 19/x[2]**3 + 7/x[3]**3 + 1/x[4]**3 - C2
    if g1 > 0:
        z = C1*(x[0]+x[1]+x[2]+x[3]+x[4]) + 10**3 * np.max([0,g1])
    else:
        z = C1*(x[0]+x[1]+x[2]+x[3]+x[4])
    return z

def restricoes(x):
    C1 = 0.0624
    C2 = 1
    g1 = 61/x[0]**3 + 37/x[1]**3 + 19/x[2]**3 + 7/x[3]**3 + 1/x[4]**3 - C2
    z = C1*(x[0]+x[1]+x[2]+x[3]+x[4])
    G = np.array([g1])
    return z,G