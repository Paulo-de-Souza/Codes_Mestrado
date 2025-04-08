import numpy as np

def constraint():
    # definindo "d" e "t"
    lb = np.array([2,0.2])
    ub = np.array([14,0.8])
    return lb,ub

    
def func(x):
    gg = 2500/(np.pi*x[0]*x[1])
    g1 = gg - 500
    g2 = gg - ((np.pi**2)*(0.85*10**6)*(x[0]**2+x[1]**2))/(8*(250**2))
    if g1 > 0 or g2 > 0:
        z = 9.82*x[0]*x[1] + 2*x[0] + 3*(np.max([0,g1]) + np.max([0,g2]))
    else:
        z = 9.82*x[0]*x[1] + 2*x[0]
    return z

def restricoes(x):
    gg = 2500/(np.pi*x[0]*x[1])
    g1 = gg - 500
    g2 = gg - ((np.pi**2)*(0.85*10**6)*(x[0]**2+x[1]**2))/(8*(250**2))
    z = 9.82*x[0]*x[1] + 2*x[0]
    G = np.array([g1,g2])
    return z,G