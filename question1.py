import gurobipy as gp
from gurobipy import GRB


def solve(utility_m):
    m = gp.Model("question1")  # create model
    N = len(utility_m)

    # creation des variables
    x = []
    for i in range(0, N):
        x.append([])
        for j in range(0, len(utility_m[i])):
            x[i].append(m.addVar(vtype=GRB.BINARY, name="x_{}_{}".format(i, j)))

    # creation des contraintes

    objective = 0
    for i in range(0, N):
        const1 = 0
        const2 = 0
        for j in range(0, N):
            objective += utility_m[i][j] * x[i][j]
            const1 += x[i][j]
            const2 += x[j][i]
        m.addConstr(const1 == 1, name="l".join(str(i)))
        m.addConstr(const2 == 1, name="c".join(str(i)))

    m.setObjective(objective, GRB.MAXIMIZE)

    m.optimize()
    return m, x
