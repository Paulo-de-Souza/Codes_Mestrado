import numpy as np

def constraint():
    # definindo b e d
    lb = np.array([0.5,0.1])
    ub = np.array([2,2])
    return lb,ub

def func(x):
    # variaveis do problema
    b = x[0]
    d = x[1]
    # constantes do problema
    l = 50
    rho = 0.3
    E = 30*10**6
    Px = 10
    Py = 25
    sig_esc = 30000

    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-9
    b += epsilon
    d += epsilon

    g1 = b - 2*d
    sig = (Py/(b*d)) + (6*Px*l)/(b*d**2)
    g2 = sig - sig_esc 
    g3 = sig - (((np.pi**2)*E*d**2)/(48*l**2)) 
    g4 = 0.5 - b
    f = rho*d*b*l
    if g1 > 0 or g2 > 0 or g3 > 0 or g4 > 0:
        z = f + (10**2)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4]))
    else:
        z = f
    return z

def restricoes(x):
    # variaveis do problema
    b = x[0]
    d = x[1]
    # constantes do problema
    l = 50
    rho = 0.3
    E = 30*10**6
    Px = 10
    Py = 25
    sig_esc = 30000

    g1 = b - 2*d
    sig = (Py/(b*d)) + (6*Px*l)/(b*d**2)
    g2 = sig - sig_esc 
    g3 = sig - (((np.pi**2)*E*d**2)/(48*l**2)) 
    g4 = 0.5 - b
    f = rho*d*b*l
    z = f
    G = np.array([g1,g2,g3,g4])
    return z,G
