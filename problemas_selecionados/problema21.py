import numpy as np

def constraint():
    # definindo h, l, t, b
    lb = np.array([0.1,0.1,0.1,0.1])
    ub = np.array([2,10,10,2])
    return lb,ub

def func(x):
    # variaveis do problema
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-9
    x1+=epsilon
    x2+=epsilon
    x3+=epsilon
    x4+=epsilon
    # Dados do problema
    P = 6000
    L = 14
    E = 30*10**6
    G = 12*10**6
    tau_max = 13600
    sig_max = 30000
    delta_max = 0.25
    tau1 = P/(np.sqrt(2)*x1*x2)
    M = P*(L + x2/2)
    R = np.sqrt(x2**2/4 + ((x1+x3)/2)**2)
    J = 2 * ((x1*x2/np.sqrt(2))*(x2**2/12 + ((x1+x3)/2)**2))
    tau2 = M*R/J
    tau = np.sqrt(tau1**2 + tau1*tau2*x2/R + tau2**2)
    sig = (6*P*L)/(x4*x3**2)
    delta = (4*P*L**3)/(E*x4*x3**3)
    Pc = ((4.013*np.sqrt(E*G*x3**2*x4**6*(1/36)))/L**2)*(1-(x3/(2*L))*np.sqrt(E/(4*G)))
    #restricoes
    g1 = tau - tau_max
    g2 = sig - sig_max
    g3 = x1 - x4
    g4 = 0.10471*x1**2 + 0.04811*x3*x4*(14+x2) - 5
    g5 = 0.125 - x1
    g6 = delta - delta_max 
    g7 = P - Pc
    f = 1.10471*x1**2*x2 + 0.04811*x3*x4*(14+x2)
    if g1 > 0 or g2 > 0 or g4 > 0 or g3 > 0 or g5 > 0 or g6 > 0 or g7 > 0:
        z = f + (10**5)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4])+np.max([0,g5])+np.max([0,g6])+np.max([0,g7]))
    else:
        z = f
    return z


