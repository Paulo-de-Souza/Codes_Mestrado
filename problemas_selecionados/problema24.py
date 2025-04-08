import numpy as np

def constraint():
    lb = np.array([5,5,5,5])
    ub = np.array([20,20,20,20])
    return lb,ub

def func(x):
    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-6
    x[0]+=epsilon
    x[1]+=epsilon
    x[2]+=epsilon
    x[3]+=epsilon

    g1 = 1.5625/x[0] + 0.6750/x[1] + 1.5625/x[2] + 1.35/x[3] - 0.5
    if g1 != 10**-7:
        z = x[0] + 1.2*x[1] + x[2] + 0.6*x[3] + 100*(np.max([g1,0]))
    else:
        z = x[0] + 1.2*x[1] + x[2] + 0.6*x[3]
    return z