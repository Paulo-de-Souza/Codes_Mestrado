import numpy as np

def SCA(N, Max_iteration, lb, ub, fobj):
    #print('SCA is optimizing your problem')
    dim = np.size(lb)
    # Inicializar conjunto de soluções aleatórias
    X = initialization(N, dim, ub, lb)

    Destination_position = np.zeros(dim)
    Destination_fitness = np.inf

    Convergence_curve = np.zeros(Max_iteration)
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

        Convergence_curve[t-1] = Destination_fitness

        # Incrementar o contador de iteração
        t += 1

    return Destination_fitness, Destination_position, Convergence_curve

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