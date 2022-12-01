import random
import time
import matplotlib.pyplot as plt


# Affichage Solution
def affiche_sol(utility_m, model, x):
    print('-------------------')
    print('Solution')
    print()
    taille = len(utility_m)
    v = []
    for i in range(taille):
        for j in range(taille):
            if (x[i][j]).x == 1:
                v.append(utility_m[i][j])

    for i in range(taille):
        print(v[i])

    print()
    print('Valeur de la fonction objectif :', model.objVal)


# Gestion matrice
def generate_matrice(n: int):
    """
    :param n: Taille de la matrice a generer
    :return: Une matrice de taille n
    """
    M = []
    for i in range(0, n):
        M.append([random.randint(0, 21) for j in range(0, n)])
    return M


def print_matrice(matrice: list[list[int]]):
    for ligne in matrice:
        print(ligne)


def func_profil(func, *args, **kwargs):
    """
    :param func: Une fonction
    :param args: Les arguments de la fonction
    :param kwargs: Les arguments de la fonction
    :return: resultat de l'appel, le temps utilise
    """
    start = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start

    return result, elapsed_time


# Enregistrement information
def time_consumption_solve(func, allowed_time: int):
    """
    :param func: Fonction dont on doit tester les performances
    :param allowed_time: temps maximum en minute pour executer une fonction
    :return: Liste du temps utiliser
    """

    # Initialisation des variables
    time_used = 0
    list_n_time = []
    taille_matrice = 5

    while time_used < allowed_time*60:
        start = time.time()     # Debut du chrono
        for _ in range(0, 10):
            utility_matrice = generate_matrice(taille_matrice)
            func(utility_matrice)

        time_used = time.time()-start   # Actualisation du temps utilisé

        list_n_time.append((taille_matrice, time_used/10))
        taille_matrice += 5

    return list_n_time


def write_time_func(lt: list[tuple[int, float]], func):
    """
    Ecrit dans un fichier le temps d'execution en fonction d'un autre argument
    :param lt: Liste contenant les temps d'execution d'une fonction
    :param func: La fonction test
    :return: None
    """
    name = "".join(("time_measurement/", func.__name__, ".txt"))
    fic = open(name, "w")
    for tpl in lt:
        fic.write("{n}\t{t}".format(n=tpl[0], t=tpl[1]))
    fic.close()


def read_info_func(path: str):
    """
    :param path: Emplacement du fichier
    :return: Une liste contenant les temps d'execution d'une fonction
    """
    fic = open(path)
    lines = fic.readlines()
    lt = []
    for line in lines:
        n, t = line.split()
        lt.append((float(n), float(t)))

    return lt


def plot_information_from_fic(path: str, name=""):
    """
    :param name: Nom de la fonction
    :param path: fichier contenant les informations d'une fonction
    :return: None
    """
    lt = read_info_func(path)

    plt.plot([tpl[0] for tpl in lt], [tpl[1] for tpl in lt])

    plt.suptitle("".join((name, " temps ")))
    plt.xlabel("taille de la matrice")
    plt.ylabel("temps (seconde)")

    plt.show()


def plot_information_from_list(lt: list[tuple[int, float]], name=""):
    """
    :param name: Nom de la fonction
    :param lt: liste contenant les informations d'une fonction
    :return: None
    """
    plt.plot([tpl[0] for tpl in lt], [tpl[1] for tpl in lt])

    plt.suptitle("".join((name, " temps ")))
    plt.xlabel("taille de la matrice")
    plt.ylabel("temps (seconde)")

    plt.show()
