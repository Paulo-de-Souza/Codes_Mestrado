import numpy as np
import random

lb = np.array([-1,-1,-1])
ub = np.array([2,2,2])
d = np.size(lb)
n = 10
Sol = np.zeros((n,d))

# criando os vetores iniciais
for i in range(n):
    for j in range(d):
        Sol[i][j] = random.uniform(lb[j],ub[j])

# criando as solucoes dos vetores iniciais
def fobj(Sol):
    colunas = np.size(Sol,1)
    linhas = np.size(Sol,0)
    Fitness = np.zeros((linhas,1))
    
    # funcao do problema estudado
    def fun(u):
        z = (1-u[0])**2 + 100*(u[1] - u[0]**2)**2 + 100*(u[2] - u[1]**2)**2
        return z
    
    # gerando a funcao final
    for i in range(linhas):
        Fitness[i] = fun(Sol[i])
    
    return Fitness

funcao = fobj(Sol)
funcao