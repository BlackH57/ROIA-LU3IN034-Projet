import gurobipy as gp
from gurobipy import GRB


def solve1(utility_m):
    m = gp.Model("question1")  # create model
    N = len(utility_m)

    # creation des variables
    x = []
    for i in range(0, N):
        x.append([])
        for j in range(0, len(utility_m[i])):
            x[i].append(m.addVar(vtype=GRB.BINARY, name="x_{}_{}".format(i, j)))

    # creation des contraintes
    maxtruc = m.addVar(vtype=GRB.CONTINUOUS, name="max")
    objective = 0
    for i in range(0, N):
        const1 = 0
        const2 = 0
        for j in range(0, N):
            objective += utility_m[i][j] * x[i][j]
            const1 += x[i][j]
            const2 += x[j][i]
        m.addConstr(const1 == 1, name="l".join(str(i))) # Un objet par personne
        m.addConstr(const2 == 1, name="c".join(str(i))) # Une personne par objet


    for i in range(0,N):    # Pour l'agent i
        regret = max([utility_m[i][j] for j in range(0,N)])     # Max pour l'agent i
        for j in range(0,N):
            regret -= utility_m[i][j] * x[i][j]  # On enleve l'utilite de l'objet
        m.addConstr(maxtruc >= regret)

    m.setObjective(objective, GRB.MINIMIZE)

    m.optimize()
    print("MAXXXXXXXXX = " + str(maxtruc))

    return m, x
