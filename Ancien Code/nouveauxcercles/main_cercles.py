import numpy as np
from cercles import *
import cmath as comp
import copy
from tqdm import tqdm
from math import floor 


def crea_quadruple(liste_cercles):
    liste2 = []
    for i in range(4):
        liste1 = []
        k = (
            2
            * (
                liste_cercles[(i + 1) % 4].rayon_courbure
                + liste_cercles[(i + 2) % 4].rayon_courbure
                + liste_cercles[(i + 3) % 4].rayon_courbure
            )
            - liste_cercles[i].rayon_courbure
        )
        x = (
            2
            * (
                (liste_cercles[(i + 1) % 4].centre[0])
                * liste_cercles[(i + 1) % 4].rayon_courbure
                + (liste_cercles[(i + 2) % 4].centre[0])
                * liste_cercles[(i + 2) % 4].rayon_courbure
                + (liste_cercles[(i + 3) % 4].centre[0])
                * liste_cercles[(i + 3) % 4].rayon_courbure
            )
            - (liste_cercles[i].centre[0]) * liste_cercles[i].rayon_courbure
        ) / k
        y = (
            2
            * (
                (liste_cercles[(i + 1) % 4].centre[1])
                * liste_cercles[(i + 1) % 4].rayon_courbure
                + (liste_cercles[(i + 2) % 4].centre[1])
                * liste_cercles[(i + 2) % 4].rayon_courbure
                + (liste_cercles[(i + 3) % 4].centre[1])
                * liste_cercles[(i + 3) % 4].rayon_courbure
            )
            - (liste_cercles[i].centre[1]) * liste_cercles[i].rayon_courbure
        ) / k
        for j in range(i):
            liste1.append(liste_cercles[j])
        liste1.append(Cercles(np.array([x, y]), 1 / k))
        for j in range(i + 1, 4):
            liste1.append(liste_cercles[j])
        liste2.append(liste1)
    return liste2


def fractale(liste_cercles, n):
    liste1 = []
    liste2 = []
    eps = 10 ** (-5)
    for cercle in liste_cercles:
        liste1.append(cercle)
    cercle4 = (liste1[0].calcul_new_cercle(liste1[1], liste1[2]))[1]
    if cercle4 == None:
        
        return []
    liste1.append(cercle4)
    liste_cercles.append(cercle4)
    liste2.append(liste_cercles)
    for i in range(n):
        liste2_prime = []
        for j in range(len(liste2)):
            quadruple_cercles = liste2.pop()
            quadruple2_cercles = crea_quadruple(quadruple_cercles)
            cercle1_prime = quadruple2_cercles[0][0]
            test = 0
            for cercle in liste1:
                if (
                    (
                        cercle1_prime.rayon <= cercle.rayon + eps
                        and cercle1_prime.rayon >= cercle.rayon - eps
                    )
                    and (
                        cercle1_prime.centre[0] <= cercle.centre[0] + eps
                        and cercle1_prime.centre[0] >= cercle.centre[0] - eps
                    )
                    and (
                        cercle1_prime.centre[1] <= cercle.centre[1] + eps
                        and cercle1_prime.centre[1] >= cercle.centre[1] - eps
                    )
                ):
                    test = 1
            if test == 0:
                liste1.append(cercle1_prime)
            cercle2_prime = quadruple2_cercles[1][1]
            test = 0
            for cercle in liste1:
                if (
                    (
                        cercle2_prime.rayon <= cercle.rayon + eps
                        and cercle2_prime.rayon >= cercle.rayon - eps
                    )
                    and (
                        cercle2_prime.centre[0] <= cercle.centre[0] + eps
                        and cercle2_prime.centre[0] >= cercle.centre[0] - eps
                    )
                    and (
                        cercle2_prime.centre[1] <= cercle.centre[1] + eps
                        and cercle2_prime.centre[1] >= cercle.centre[1] - eps
                    )
                ):
                    test = 1
            if test == 0:
                liste1.append(cercle2_prime)
            cercle3_prime = quadruple2_cercles[2][2]
            test = 0
            for cercle in liste1:
                if (
                    (
                        cercle3_prime.rayon <= cercle.rayon + eps
                        and cercle3_prime.rayon >= cercle.rayon - eps
                    )
                    and (
                        cercle3_prime.centre[0] <= cercle.centre[0] + eps
                        and cercle3_prime.centre[0] >= cercle.centre[0] - eps
                    )
                    and (
                        cercle3_prime.centre[1] <= cercle.centre[1] + eps
                        and cercle3_prime.centre[1] >= cercle.centre[1] - eps
                    )
                ):
                    test = 1
            if test == 0:
                liste1.append(cercle3_prime)
            cercle4_prime = quadruple2_cercles[3][3]
            test = 0
            for cercle in liste1:
                if (
                    (
                        cercle4_prime.rayon <= cercle.rayon + eps
                        and cercle4_prime.rayon >= cercle.rayon - eps
                    )
                    and (
                        cercle4_prime.centre[0] <= cercle.centre[0] + eps
                        and cercle4_prime.centre[0] >= cercle.centre[0] - eps
                    )
                    and (
                        cercle4_prime.centre[1] <= cercle.centre[1] + eps
                        and cercle4_prime.centre[1] >= cercle.centre[1] - eps
                    )
                ):
                    test = 1
            if test == 0:
                liste1.append(cercle4_prime)
            for quadruple in quadruple2_cercles:
                liste2_prime.append(quadruple)
        liste2 = copy.deepcopy(liste2_prime)

    return liste1
