import question1
import question4
import question5
import tools

matrice1 = [
    [12, 20, 6, 5, 8],
    [5, 12, 6, 8, 5],
    [8, 5, 11, 5, 6],
    [6, 8, 6, 11, 5],
    [5, 6, 8, 7, 7]
]


def test_question1(matrice):
    m, x = question1.solve1(matrice)
    tools.affiche_sol(matrice1, m, x)


def test_temps_question1(time_allowed):
    lt = tools.time_consumption_solve(question1.solve1, time_allowed)
    tools.write_time_func(lt, question1.solve1)

def test_question4(matrice, epsilon):
    m, x = question4.solve2(matrice, epsilon)
    tools.affiche_sol(matrice1, m , x)

def test_temps_question4(time_allowed):
    lt = tools.time_consumption_solve(question4.solve2, time_allowed)
    tools.write_time_func(lt, question4.solve2)
    

def test_question5(matrice):
    m, x = question5.solve1(matrice)
    tools.affiche_sol(matrice1, m, x)

if __name__ == "__main__":
    # test_temps_question1(0.5)
    # test_question1(matrice1)
    # test_question4(matrice1, 1)
    # tools.plot_information_from_fic("time_measurement/solve1.txt", "Question 1")
    # test_question4(matrice1, 0.01)
    test_question5(matrice1)
    # test_temps_question4(0.5)
    # tools.plot_information_from_fic("time_measurement/solve2.txt", "Question 2")

