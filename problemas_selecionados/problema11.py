import numpy as np

def constraint():
    # definindo d, D e N
    lb = np.array([0.05,0.25,2])
    ub = np.array([2,1.3,15])
    return lb,ub

def func(x):
    # variaveis do problema
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]

    # restricoes
    g1 = 1 - (x2**3 * x3)/(71785*x1**4)
    g2 = (4*x2**2 - x1*x2)/(12566*(x2*x1**3-x1**4)) + 1/(5108*x1**2) - 1
    #g3 = 1 - ((140.45*x1)/((x2**2)*x3))
    if x3 == 0:
        g3 = float('inf')  # Divisão por zero é evitada, definindo g3 como infinito
    else:
        g3 = 1 - ((140.45 * x1) / ((x2**2) * x3))

    g4 = (x1+x2)/1.5 - 1
    fx = (x3+2)*x2*x1**2
    if  g1 > 0 or g2 > 0 or g3 > 0 or g4 > 0:
        z = fx + (10**1)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4]))
    else:
        z = fx
    return z
