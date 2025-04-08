import numpy as np

def constraint():
    lb = np.array([0.01,0.005])
    ub = np.array([1,0.2])
    return lb,ub

def func(x):
    R = x[0]
    t = x[1]
    P = 50*10**3
    L = 5
    E = 210*10**9
    siga = 250*10**6
    e = 0.02*R
    Delta = 0.25
    rho = 7850
    A = 2*np.pi*R*t
    I = np.pi*R**3*t
    c = R + 0.5*t
    k = np.sqrt(I/A)
    sec1 = 1/(np.cos((L/k)*(P/(E*A))**0.5))
    sig = (P/A) * (1 + (e*c/k**2)*sec1)
    Pcr = (np.pi**2 * E * I)/(4*L**2)
    sec2 = 1/(np.cos((P/(E*I))**0.5))
    delta = e*(sec2-1)
    g1 = sig-siga
    g2 = P-Pcr
    g3 = delta-Delta
    g4 = R-50*t
    if (g1 or g2 or g3 or g4)>0:
        z = rho*L*A + (10**8)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4]))
    else:
        z = rho*L*A
    return z