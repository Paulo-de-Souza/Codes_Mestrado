import numpy as np
#import scipy as sc

def constraint():
    # definindo d, h e t
    lb = np.array([2.5,2.5,0.1])
    ub = np.array([10,10,1])
    return lb,ub

def func(x):
    # variaveis do problema
    d = x[0]+0.001
    h = x[1]+0.001
    t = x[2]+0.001
    # constantes
    E = 3*10**7
    L = 100
    G = 1.154*10**7
    P = -10000
    siga = 40000
    # equacoes fundamentais
    A = (d-t)*(h-t)
    I = (1/12)*(d*h**3 - (d-2*t)*(h-2*t)**3)
    J = (2 * t * (d-t)**2 * (h-t)**2)/(d+h-2*t)
    k22 = 4*L**2 + ((G*J)/(E*I))*L**2
    k33 = k22
    # matriz de rigidez
    Krig = np.array([[24,-6*L,6*L],
                     [-6*L,k22,0],
                     [6*L,0,k33]])
    K = ((E*I)/L**3)*Krig
    # vetor de carregamento
    vecP = np.array([[P],[0],[0]])
    # vetor deslocamento
    U = np.linalg.inv(K)@vecP
    #U = sc.linalg.inv(K)@vecP
    # deslocamentos
    U1 = float(U[0])
    U2 = float(U[1])
    U3 = float(U[2])

    # equacoes para as restricoes
    T = -G*J/L * U3
    #tau = T/(2*A*t)
    if A*t > 1e-6:  # Verifica se t não é muito próximo de zero
        tau = T / (2 * A * t)
    else:
        tau = 0  # Define tau como zero ou outro valor adequado em caso de t muito pequeno
    
    M1 = ((2*E*I)/L**2) * (-3*U1 + U2*L)
    sig1 = (M1*h)/(2*I)
    M2 = ((2*E*I)/L**2) * (-3*U1 + 2*U2*L)
    sig2 = (M2*h)/(2*I)

    # restricoes
    g1 = ((sig1**2 + 3*tau**2)/(siga**2)) - 1
    g2 = ((sig2**2 + 3*tau**2)/(siga**2)) - 1
    if g1 > 0 or g2 > 0:
        z = 2*L*(2*d*t + 2*h*t - 4*t**2) + (10**5)*(np.max([0,g1])+np.max([0,g2]))
    else:
        z = 2*L*(2*d*t + 2*h*t - 4*t**2)
    return z

