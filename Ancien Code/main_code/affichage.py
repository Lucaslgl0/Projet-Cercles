import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from math import *
from tqdm import tqdm
from random import randint
from Cercle import *


def dessin_pyplot():
    fill = False
    cercle1_rayon = 1 / (int(input("Quel est la courbure du cercle 1:")))
    cercle2_rayon = 1 / (int(input("Quel est la courbure du cercle 2:")))
    cercle3_rayon = 1 / (int(input("Quel est la courbure du cercle 3:")))

    while cercle3_rayon > cercle2_rayon or cercle2_rayon > cercle1_rayon:
        if cercle3_rayon > cercle2_rayon:
            cercle2_rayon, cercle3_rayon = cercle3_rayon, cercle2_rayon

        if cercle2_rayon > cercle1_rayon:
            cercle1_rayon, cercle2_rayon = cercle2_rayon, cercle1_rayon

    cercle1 = plt.Circle((0, 0), cercle1_rayon, color="w", fill=False)
    cercle2 = plt.Circle(
        (cercle1_rayon + cercle2_rayon, 0), cercle2_rayon, color="w", fill=False
    )
    """
    on fait deux cercles:
    -centre (0,0) et rayon r1+r3
    -centre (r1+r2,0) et rayon r2+r3
    d = r1+r2
    a = (r2²-r1²+d²)/2*d
    h = sqrt(r1²-a²)
    on donc point d'intersection :
    -x = a
    -y = h
    """

    C1 = Cercles_complexe(np.array([0, 0]), cercle1_rayon)
    C2 = Cercles_complexe(np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon)

    C1_prime = Cercles_complexe(np.array([0, 0]), cercle3_rayon + cercle1_rayon)
    C2_prime = Cercles_complexe(
        np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon + cercle3_rayon
    )

    cercle3_centre = C1_prime.coordonnees_points_intersection(C2_prime)

    a = cercle3_centre[0][0]
    h = cercle3_centre[0][1]

    cercle3 = plt.Circle((a, h), cercle3_rayon, color="w", fill=False)

    C3 = Cercles_complexe(np.array([a, h]), cercle3_rayon)

    ax = plt.gca()
    ax.cla()

    ax.set_xlim((-15, 15))
    ax.set_ylim((-15, 15))

    ax.add_patch(cercle1)
    ax.add_patch(cercle2)
    ax.add_patch(cercle3)

    iterations = int(input("Combien voulez-vous d'itérations ?"))
    letter = input("Voulez vous coloriser les cercles en fonctions des congruences ? [o/n]")
    if letter == "o" or letter == "O":
        fill = True

    if fill:
        congruence = int(input("Quelle  congruence souhaitez vous tester : "))

        print("Génération des cercles...")
        liste = Cercles_complexe.fractale([C1, C2, C3], iterations)
        print("Affichage des cercles...")

        color = []
        for i in range(congruence):
            color.append('#%06X' % randint(0, 0xFFFFFF))

        i = 0
        new_color = {}
        for cercle in tqdm(liste):
            i += 1
            if (3 / 4) * (i - 4) + 1 > 1:
                n = floor(np.log((3 / 4) * (i - 4) + 1) / np.log(4))
            else:
                n = 0

            ax.add_patch(
                plt.Circle(
                    (cercle.centre[0], cercle.centre[1]),
                    cercle.rayon,
                    color=color[int(cercle.courbure) % congruence],
                    fill=False,
                    linewidth=0.5,
                )
            )
            new_color[int(cercle.courbure) % congruence] = color[int(cercle.courbure) % congruence]

        patches = [mpatches.Patch(color=new_color[i], label=i) for i in new_color.keys()]
        plt.legend(handles=patches, loc='upper right', ncol=2 )
        plt.autoscale()
        # plt.show()
        print("Enregistrement de l'image...")
        plt.savefig("fractale n=" + str(iterations) + ".png", dpi=1500)
        plt.show()
        print("------- Fin du programme -------")

    else:
        print("Génération des cercles...")
        liste = Cercles_complexe.fractale([C1, C2, C3], iterations)
        print("Affichage des cercles...")

        i = 0
        for cercle in tqdm(liste):
            i += 1
            if (3 / 4) * (i - 4) + 1 > 1:
                n = floor(np.log((3 / 4) * (i - 4) + 1) / np.log(4))
            else:
                n = 0

            ax.add_patch(
                plt.Circle(
                    (cercle.centre[0], cercle.centre[1]),
                    cercle.rayon,
                    fill=False,
                    linewidth=0.5,
                )
            )
            if cercle.courbure <= 10:
                plt.text(
                    cercle.centre[0] - 1 / ((n + 1) * 10),
                    cercle.centre[1] - 1 / ((n + 1) * 5),
                    round(cercle.courbure),
                    fontsize=20 * cercle.rayon * (n + 1),
                )

        plt.autoscale()
        # plt.show()
        print("Enregistrement de l'image...")
        plt.savefig("fractale n=" + str(iterations) + ".png", dpi=1500)
        plt.show()
        print("------- Fin du programme -------")
