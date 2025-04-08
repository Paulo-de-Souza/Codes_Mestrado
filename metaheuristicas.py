import numpy as np
import random 

def fun_checkpositions(vec_pos,var_no_group,lb,ub):
  Lb = lb
  Ub = ub
  for i in range(var_no_group):
    is_below_lb = vec_pos[i] < Lb;
    is_above_ub = vec_pos[i] > Ub;
    vec_pos[i][is_below_lb] = Lb[is_below_lb]
    vec_pos[i][is_above_ub] = Ub[is_above_ub]
  return vec_pos

def initialization(SearchAgents_no, dim, ub, lb):
    Boundary_no = len(ub)  # número de limites

    # Se os limites de todas as variáveis são iguais
    if Boundary_no == 1:
        X = np.random.rand(SearchAgents_no, dim) * (ub - lb) + lb

    # Se cada variável tem um limite diferente
    if Boundary_no > 1:
        X = np.zeros((SearchAgents_no, dim))
        for i in range(dim):
            ub_i = ub[i]
            lb_i = lb[i]
            X[:, i] = np.random.rand(SearchAgents_no) * (ub_i - lb_i) + lb_i

    return X

def fun_checkpositions2(X, N, lb, ub):
    for i in range(N):
        for j in range(len(lb)):
            if X[i, j] > ub[j]:
                X[i, j] = ub[j]
            elif X[i, j] < lb[j]:
                X[i, j] = lb[j]
    return X


def myDE(Fun,n,F,Cr,lb,ub,N_max):
    N_iter = 0
    d = np.size(lb)
    Convergence_curve = np.zeros((1,N_max))
    Sol = np.zeros((n,d))
    Fitness = np.zeros((n,1))
    
    for i in range(n):
        for j in range(d):
            Sol[i][j] = random.uniform(lb[j],ub[j])
        Fitness[i][0] = Fun(Sol[i,:])

    fmin = np.min(Fitness)
    I = np.argmin(Fitness)
    best = Sol[I]

    while N_iter<N_max:
        # mutacao
        k1 = np.random.permutation(n)
        k1sol = Sol[k1,:]
        k2 = np.random.permutation(n)
        k2sol = Sol[k2,:]
        V = Sol + F*(k1sol-k2sol)
        
        # cruzamento
        K = np.random.rand(n,d)<Cr
        V = np.multiply(Sol,1-K) + np.multiply(V,K)       
        V = fun_checkpositions(V,n,lb,ub)

    ## ESSE FINAL PRECISA SER MODIFICADO
        for i in range(n):
            Fnew = Fun(V[i])
            if Fnew <= Fitness[i]:
                Sol[i] = V[i]
                Fitness[i] = Fnew

            if Fnew<=fmin:
                best=V[i]
                fmin=Fnew
                
        Convergence_curve[0][N_iter]=fmin
        N_iter = N_iter + 1
    return best,fmin,Convergence_curve

def myAOA(f,materials_no,Max_iter,lb,ub,C3,C4):
  C1=2;
  C2=6;
  u=0.9;
  l=0.1;

  dub = np.size(lb)
  X = np.zeros((materials_no,dub))
  acc = np.zeros((materials_no,dub))
  den = np.zeros((materials_no,dub))
  vol = np.zeros((materials_no,dub))
  Y = np.zeros((materials_no,1))
  for j in range(materials_no):
    for k in range(len(lb)):
      X[j][k]   =  random.uniform(lb[k],ub[k])
      acc[j][k] = (random.uniform(lb[k],ub[k]))
      den[j][k] = (random.random())
      vol[j][k] = (random.random())
      Y[j][0] = f(X[j,:])

  Scorebest = np.min(Y)
  Score_index = np.argmin(Y)
  Xbest = X[Score_index]
  den_best=den[Score_index][:];
  vol_best=vol[Score_index];
  acc_best=acc[Score_index];
  acc_norm=acc;
  acc_temp = np.zeros((materials_no, len(den[0])))
  X_new = np.zeros((materials_no, len(den[0])))
  Convergence_curve = np.zeros((1,Max_iter))

  for t in range(Max_iter):
    t = t+1
    TF = np.exp((t-Max_iter)/(Max_iter))
    if TF > 1:
      TF = 1
    d=np.exp((Max_iter-t)/Max_iter)-(t/Max_iter)
    acc=acc_norm
    r=random.random()
    for i in range(materials_no):
      den[i][:] = np.array(den[i][:]) + r*(den_best-np.array(den[i][:]))
      vol[i][:] = np.array(vol[i][:]) + r*(vol_best-np.array(vol[i][:]))
      if TF < 0.45:
        mr = random.randint(0,materials_no-1)
        acc_temp[i][:] = np.divide((np.array(den[mr][:]) + np.multiply(np.array(vol[mr][:]),np.array(acc[mr][:]))), (random.random() * np.multiply(np.array(den[mr][:]), np.array(vol[mr][:]))))  # Eq. (10)
      else:
        acc_temp[i][:] = np.divide((den_best + np.multiply(vol_best, acc_best)),(random.random()*np.multiply(np.array(den[i][:]), np.array(vol[i][:])))) # Eq. (11)
        #print(acc_temp)
    acc_norm = np.divide(u*(acc_temp-np.min(acc_temp)),(np.max(acc_temp)-np.min(acc_temp)))+l
    for i in range(materials_no):
        if TF < 0.4:
            for j in range(len(lb)):
                mrand = random.randint(0,materials_no-1)
                X_new[i][j] = X[i][j]+C1*random.random()*np.multiply(acc_norm[i][j],(X[mrand][j]-X[i][j]))*d;  # Eq. (13)
        else:
            for j in range(len(lb)):
                p = 2*random.random()-C4
                T = C3*TF
                if T > 1:
                    T=1
                if p<.5:
                    X_new[i][j] = np.array(Xbest[j]) + C2*random.random()*np.multiply(np.array(acc_norm[i][j]),T*np.array(Xbest[j])-np.array(X[i][j]))*d
                else:
                    X_new[i][j] = np.array(Xbest[j]) - C2*random.random()*np.multiply(np.array(acc_norm[i][j]),T*np.array(Xbest[j])-np.array(X[i][j]))*d

    X_new = fun_checkpositions(X_new,materials_no,lb,ub)
    for i in range(materials_no):
      v = f(X_new[i])
      if v < Y[i]:
        X[i] = X_new[i]
        Y[i] = v

    var_Ybest = np.min(Y)
    var_index = np.argmin(Y)
    t = t-1
    Convergence_curve[0][t]=var_Ybest;
    if var_Ybest < Scorebest:
      Scorebest = var_Ybest
      Score_index = var_index
      Xbest = X[var_index][:]
      den_best = den[Score_index][:]
      vol_best = vol[Score_index][:]
      acc_best = acc[Score_index][:]
  return Xbest, Scorebest, Convergence_curve

def myPSO(Fun,N,c1,c2,lb,ub,kmax):
    d = np.size(lb)
    k = 0
    ## Inicializacao das particulas e velocidades
    x = np.zeros([N,d])
    v = np.zeros([N,d])
    Evolution = np.zeros((1,kmax))

    for i in range(N):
        for j in range(d):
            x[i][j] = random.random()*(ub[j]-lb[j])+lb[j]

    ## Calculando as particulas iniciais na funcao objetivo
    fx = np.zeros([N,1])
    for i in range(N):
        xi = x[i]
        fx[i] = Fun(xi)

    ## salvando a melhor particula global e a melhor localizacao das particulas
    gfit = np.min(fx)     # menor valor global
    ind = np.argmin(fx)   # indice do menor valor global
    g = x[ind]            # vetor de posicao do menor valor global 
    fp  = fx              # melhor valor por posicao
    p = x                 # melhor posicao

    ## Iniciando o processo iterativo
    for k in range(kmax):
        #k = k + 1
        ## Calculando as novas velocidades para cada particula
        for i in range(N):
            ## Extraindo as particulas
            xi = x[i]
            ## Extraindo a particula local
            pi = p[i]
            ## Determinando a nova velocidade para cada particula vi
            v[i] = v[i] + c1*np.random.rand(1,d)@(pi-xi) + c2*np.random.rand(1,d)@(g-xi)
        
        ## Determinacao de nova posicao de cada particula
        x = x+v
        x = fun_checkpositions(x,N,lb,ub)
        ## Determinando as novas particulas com a funcao objetivo
        for i in range(N):
            xi = x[i]
            fx[i] = Fun(xi)
        
        ## Salvando a melhor particula e a melhor posicao da particula
        gfitkplus1 = np.min(fx)
        ind = np.argmin(fx)
        if gfitkplus1 < gfit:
            gfit = gfitkplus1
            g = x[ind]
        
        for i in range(N):
            # Se alguma particula for melhor que a da solucao anterior, atualizar a melhor posicao local
            if fx[i] < fp[i]:
                fp[i] = fx[i]
                p[i] = x[i]

        Evolution[0][k] = gfit
        Xbest = g
        Fbest = gfit
    return Xbest, Fbest, Evolution

def mySCA(N, Max_iteration, lb, ub, fobj):
    #print('SCA is optimizing your problem')
    dim = np.size(lb)
    # Inicializar conjunto de soluções aleatórias
    X = initialization(N, dim, ub, lb)

    Destination_position = np.zeros(dim)
    Destination_fitness = np.inf

    Convergence_curve = np.zeros((1,Max_iteration))
    Objective_values = np.zeros(N)

    # Calcular a aptidão do primeiro conjunto e encontrar a melhor
    for i in range(N):
        Objective_values[i] = fobj(X[i])
        if i == 0:
            Destination_position = X[i].copy()
            Destination_fitness = Objective_values[i]
        elif Objective_values[i] < Destination_fitness:
            Destination_position = X[i].copy()
            Destination_fitness = Objective_values[i]

    # Loop principal
    t = 1  # Começa da segunda iteração, já que a primeira é dedicada ao cálculo da aptidão
    while t <= Max_iteration:

        # Eq. (3.4)
        a = 2
        r1 = a - t * (a / Max_iteration)  # r1 decresce linearmente de a para 0

        # Atualizar a posição das soluções em relação ao destino
        for i in range(N):
            for j in range(dim):
                r2 = 2 * np.pi * np.random.rand()
                r3 = 2 * np.random.rand()
                r4 = np.random.rand()

                if r4 < 0.5:
                    X[i, j] += r1 * np.sin(r2) * abs(r3 * Destination_position[j] - X[i, j])
                else:
                    X[i, j] += r1 * np.cos(r2) * abs(r3 * Destination_position[j] - X[i, j])

        # Verificar se as soluções estão fora do espaço de busca e trazê-las de volta
        X = fun_checkpositions2(X, N, lb, ub)

        # Calcular os novos valores objetivos
        for i in range(N):
            Objective_values[i] = fobj(X[i])

            # Atualizar o destino se houver uma solução melhor
            if Objective_values[i] < Destination_fitness:
                Destination_position = X[i].copy()
                Destination_fitness = Objective_values[i]

        Convergence_curve[0][t-1] = Destination_fitness

        # Incrementar o contador de iteração
        t += 1

    return Destination_fitness, Destination_position, Convergence_curve

