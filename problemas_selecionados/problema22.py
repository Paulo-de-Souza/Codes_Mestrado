import numpy as np

def constraint():
    # definindo h, l, t, b
    lb = np.array([2.6,0.7,17,7.3,7.3,2.9,5.0])
    ub = np.array([3.6,0.8,28,8.3,8.3,3.9,5.5])
    return lb,ub

def func(x):
    # variaveis do problema
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    x6 = x[5]
    x7 = x[6]
    # Adicionando uma pequena constante para evitar divisão por zero
    epsilon = 1e-6
    x1+=epsilon
    x2+=epsilon
    x3+=epsilon
    x4+=epsilon
    x5+=epsilon
    x6+=epsilon
    x7+=epsilon
    # criando as restricoes
    g1 = 27/(x1*x2*x3) - 1
    g2 = 397.5/(x1*x2**2*x3**2)-1
    g3 = (1.93*x4**3)/(x2*x3*x6**4) - 1
    g4 = (1.93*x5**3)/(x2*x3*x7**4) - 1
    g5 = (1/(110*x6**3))*np.sqrt(((745*x4)/(x2*x3))**2 + 16.9*10**6) - 1
    g6 = (1/(85*x7**3))*np.sqrt(((745*x4)/(x2*x3))**2 + 157.5*10**6) - 1
    g7 = x2*x3/40 - 1
    g8 = (5*x2/x1) - 1
    g9 = (x1/(12*x2)) - 1
    g10 = (1.5*x6 + 1.9)/x4 - 1
    g11 = (1.1*x7 + 1.9)/x5 - 1
    f = 0.7854*x1*x2**2*(3.3333*x3**2 + 14.9334*x3 - 43.0934) - 1.508*x1*(x6**2 + x7**2) + 7.477*(x6**3 + x7**3) + 0.7854*(x4*x6**2 + x5*x7**2)
    if g1 > 0 or g2 > 0 or g4 > 0 or g3 > 0 or g5 > 0 or g6 > 0 or g7 > 0 or g8>0 or g9>0 or g10>0 or g11>0:
        f1 = (10**7)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4])+np.max([0,g5])+np.max([0,g6]))
        f2 = (10**7)*(np.max([0,g7])+np.max([0,g8])+np.max([0,g9])+np.max([0,g10])+np.max([0,g11]))
        z = f + f1 + f2
    else:
        z = f
    return z

    