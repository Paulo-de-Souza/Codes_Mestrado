import numpy as np

def constraint():
    # definindo x1 e x2
    lb = np.array([6,7])
    ub = np.array([12,20])
    return lb,ub

    
def func(x):
    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-6
    x[0]+=epsilon
    x[1]+=epsilon

    g1 = 0.6/x[0] + 0.3464/x[1] - 0.1
    if g1>0:
        z = 0.1*x[0] + 0.05773*x[1] + 1000*(np.max([0,g1]))
    else:
        z = 0.1*x[0] + 0.05773*x[1]
    return z