import matplotlib.pyplot as plt
import numpy as np
from math import *
from espace_fonctions import *
from tqdm import tqdm


# on demande les courbures des cercles de départ et on fait leur inverse pour avoir les rayons
cercle1_rayon = 1 / (float(input("Quel est la courbure du cercle 1:")))
cercle2_rayon = 1 / (float(input("Quel est la courbure du cercle 2:")))
cercle3_rayon = 1 / (float(input("Quel est la courbure du cercle 3:")))

# on ordonne les cercles dans l'ordre décroissant
while cercle3_rayon > cercle2_rayon or cercle2_rayon > cercle1_rayon:
    if cercle3_rayon > cercle2_rayon:
        cercle2_rayon, cercle3_rayon = cercle3_rayon, cercle2_rayon

    if cercle2_rayon > cercle1_rayon:
        cercle1_rayon, cercle2_rayon = cercle2_rayon, cercle1_rayon

# on plot les deux premiers cercles
cercle1 = plt.Circle(
    (0, 0),
    cercle1_rayon,
    fill=False,
    linewidth=0.01,
)
cercle2 = plt.Circle(
    (cercle1_rayon + cercle2_rayon, 0),
    cercle2_rayon,
    fill=False,
    linewidth=0.01,
)

C1 = Cercles_complexe(np.array([0, 0]), cercle1_rayon)
C2 = Cercles_complexe(np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon)

C1_prime = Cercles_complexe(np.array([0, 0]), cercle3_rayon + cercle1_rayon)
C2_prime = Cercles_complexe(
    np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon + cercle3_rayon
)

# on calcule le centre du troisième cercle pour qu'il soit tangeant aux deux autres
cercle3_centre = C1_prime.coordonnees_points_intersection(C2_prime)

a = cercle3_centre[0][0]
h = cercle3_centre[0][1]

cercle3 = plt.Circle(
    (a, h),
    cercle3_rayon,
    fill=False,
    linewidth=0.01,  # pour le box couting il est essentiel d'avoir un trait fin
)

C3 = Cercles_complexe(np.array([a, h]), cercle3_rayon)

ax = plt.gca()
ax.cla()

ax.add_patch(cercle1)
ax.add_patch(cercle2)
ax.add_patch(cercle3)

# on demande le nombre d'itérations souhaité 
iterations = int(input("Combien voulez-vous d'itérations ?"))

# on calcule les cercles de la fractales
print("Génération des Cercles_complexe...")
liste = Cercles_complexe.fractale([C1, C2, C3], iterations)
print("Affichage des Cercles_complexe...")

# on plot les cercles de la fractale
i = 0
liste_color = ["b", "g", "r", "m", "y", "c", "k"]
for cercle in liste:
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
            linewidth=0.01, # on prend cette largeur de trait pour avoir le moins de pixels colorisé
        )
    )

# on affiche la fractale
plt.autoscale()
plt.grid(False)
plt.axis("off")
ax.set_aspect("equal", adjustable="box")
print("Enregistrement de l'image...")
plt.savefig("essai box counting.png", dpi=1500) 
plt.show()

print("------- Fin du programme -------")
    