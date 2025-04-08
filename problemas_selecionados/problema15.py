import numpy as np

def constraint():
    # definindo x1 e x2
    lb = np.array([0.1,0.1])
    ub = np.array([2,2.5])
    return lb,ub

# constantes do problema
E = 30*10**6
rho = 0.283
P = 10000
sig0 = 20000
h = 100
Aref = 1

def funcA(x):
    x1 = x[0]
    x2 = x[1]
    g1 = (P*(1+x1)*np.sqrt(1+x1**2))/(2*np.sqrt(2)*x1*x2*Aref) - sig0
    g2 = (P*(-1+x1)*np.sqrt(1+x1**2))/(2*np.sqrt(2)*x1*x2*Aref) - sig0
    f1 = 2*rho*h*x2*np.sqrt(1+x1**2) * Aref
    if (g1 or g2) > 0:
        z = f1 + (10**5)*(np.max([0,g1])+np.max([0,g2]))
    else:
        z = f1
    return z

def funcB(x):
    x1 = x[0]
    x2 = x[1]
    g1 = (P*(1+x1)*np.sqrt(1+x1**2))/(2*np.sqrt(2)*x1*x2*Aref) - sig0
    g2 = (P*(-1+x1)*np.sqrt(1+x1**2))/(2*np.sqrt(2)*x1*x2*Aref) - sig0
    f2 = (P*h*(1+x1**2)**1.5 * np.sqrt(1+x1**4))/(2*np.sqrt(2)*E*(x1**2)*x2*Aref)
    if (g1 or g2) > 0:
        z = f2 + (10**5)*(np.max([0,g1])+np.max([0,g2]))
    else:
        z = f2
    return z

def funcD(x):
    x1 = x[0]
    x2 = x[1]
    g1 = (P*(1+x1)*np.sqrt(1+x1**2))/(2*np.sqrt(2)*x1*x2*Aref) - sig0
    g2 = (P*(-1+x1)*np.sqrt(1+x1**2))/(2*np.sqrt(2)*x1*x2*Aref) - sig0
    f1 = 2*rho*h*x2*np.sqrt(1+x1**2) * Aref
    f2 = (P*h*(1+x1**2)**1.5 * np.sqrt(1+x1**4))/(2*np.sqrt(2)*E*(x1**2)*x2*Aref)
    if (g1 or g2) > 0:
        z = f1+f2 + (10**5)*(np.max([0,g1])+np.max([0,g2]))
    else:
        z = f1+f2
    return z
