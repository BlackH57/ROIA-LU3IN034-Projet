import question1
import tools

matrice1 = [
    [12, 20, 6, 5, 8],
    [5, 12, 6, 8, 5],
    [8, 5, 11, 5, 6],
    [6, 8, 6, 11, 5],
    [5, 6, 8, 7, 7]
]


def test_question1():
    m, x = question1.solve(matrice1)
    tools.affiche_sol(matrice1, m, x)


def test_temps_question1(time_allowed):
    lt = tools.time_consumption_solve(question1.solve, time_allowed)
    tools.write_time_func(lt, question1.solve)


if __name__ == "__main__":
    test_temps_question1(0.5)
