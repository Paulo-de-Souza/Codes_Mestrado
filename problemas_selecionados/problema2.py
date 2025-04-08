import numpy as np

def func(x):
    h = x[0]; b = x[1]; tf = x[2]; tw = x[3]
    L = 25; E = 210
    sigy = 262; siga = 144.1; taua = 86.46; sigt = 255/2 
    Da = L/800; Pm = 104
    Ps = 155
    A = h*tw+2*b*tf
    I = ((1/12) * tw*h**3) + ((2/3)*b*tf**3) + 0.5*b*tf*h*(h+2*tf)
    w = (19+77*A)
    M = (L/8) * (2*Pm + w*L)
    sig = (M/(1000*I)) * (0.5*h + tf)
    sigf = 72845*((tf/b)**2)
    sigw = 3648276*((tw/h)**2)
    S = 0.5*(Ps + w*L)
    D = ((L**3)/(384*(10**6)*E*I)) * (8*Pm + 5*w*L)
    tau = S/(1000*h*tw)
    g1 = sig-siga
    g2 = sig-sigf
    g3 = sig-sigw
    g4 = tau-taua
    g5 = D-Da
    g6 = sig-sigt
    if g1 > 0 or g2 > 0 or g3 > 0 or g4 > 0 or g5 > 0 or g6 > 0:
        z = A*L + (10**5)*(np.max([0,g1])+np.max([0,g2])+np.max([0,g3])+np.max([0,g4])+np.max([0,g5])+np.max([0,g6]))
    else:
        z = A*L   
    return z

def constraint():
    lb = np.array([0.3,0.3,0.01,0.01])
    ub = np.array([2.5,2.5,0.1,0.1])
    return lb,ub

def restricoes(x):
    h = x[0]; b = x[1]; tf = x[2]; tw = x[3]
    L = 25; E = 210
    sigy = 262; siga = 144.1; taua = 86.46; sigt = 255/2 
    Da = L/800; Pm = 104
    Ps = 155
    A = h*tw+2*b*tf
    I = ((1/12) * tw*h**3) + ((2/3)*b*tf**3) + 0.5*b*tf*h*(h+2*tf)
    w = (19+77*A)
    M = (L/8) * (2*Pm + w*L)
    sig = (M/(1000*I)) * (0.5*h + tf)
    sigf = 72845*((tf/b)**2)
    sigw = 3648276*((tw/h)**2)
    S = 0.5*(Ps + w*L)
    D = ((L**3)/(384*(10**6)*E*I)) * (8*Pm + 5*w*L)
    tau = S/(1000*h*tw)
    g1 = sig-siga
    g2 = sig-sigf
    g3 = sig-sigw
    g4 = tau-taua
    g5 = D-Da
    g6 = sig-sigt
    z = A*L
    G = np.array([g1,g2,g3,g4,g5,g6])
    return z,G