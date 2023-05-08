import matplotlib.pyplot as plt
from math import *
from cercles import *
from main_cercles import *
from tqdm import tqdm

cercle1_rayon = 1 / (int(input("Quel est le rayon de courbure du cercle 1:")))
cercle2_rayon = 1 / (int(input("Quel est le rayon de courbure du cercle 2:")))
cercle3_rayon = 1 / (int(input("Quel est le rayon de courbure du cercle 3:")))

while cercle3_rayon > cercle2_rayon or cercle2_rayon > cercle1_rayon:
    if cercle3_rayon > cercle2_rayon:
        cercle2_rayon, cercle3_rayon = cercle3_rayon, cercle2_rayon

    if cercle2_rayon > cercle1_rayon:
        cercle1_rayon, cercle2_rayon = cercle2_rayon, cercle1_rayon

cercle1 = plt.Circle((0, 0), cercle1_rayon, color="b", fill=False)
cercle2 = plt.Circle(
    (cercle1_rayon + cercle2_rayon, 0), cercle2_rayon, color="b", fill=False
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


C1 = Cercles(np.array([0, 0]), cercle1_rayon)
C2 = Cercles(np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon)

C1_prime = Cercles(np.array([0, 0]), cercle3_rayon + cercle1_rayon)
C2_prime = Cercles(
    np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon + cercle3_rayon
)

cercle3_centre = C1_prime.calculpoints_intersection_cercles(C2_prime)

a = cercle3_centre[0][0]
h = cercle3_centre[0][1]

cercle3 = plt.Circle((a, h), cercle3_rayon, color="b", fill=False)

C3 = Cercles(np.array([a, h]), cercle3_rayon)

ax = plt.gca()
ax.cla()


ax.set_xlim((-15, 15))
ax.set_ylim((-15, 15))


ax.add_patch(cercle1)
ax.add_patch(cercle2)
ax.add_patch(cercle3)

iterations = int(input("Combien voulez-vous d'itérations ?"))
print("Génération des cercles...")
liste = fractale([C1, C2, C3], iterations)
print("Affichage des cercles...")

i = 0
liste_color = ["b", "g", "r", "m", "y", "c", "k"]
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
            color=liste_color[n % len(liste_color)],
            fill=False,
            linewidth=0.5,
        )
    )
    if cercle.rayon_courbure <= 10:
        plt.text(
            cercle.centre[0] - 1 / ((n + 1) * 10),
            cercle.centre[1] - 1 / ((n + 1) * 5),
            round(cercle.rayon_courbure),
            fontsize=20 * cercle.rayon * (n + 1),
        )

plt.autoscale()
# plt.show()
print("Enregistrement de l'image...")
plt.savefig("fractale n=" + str(iterations) + ".png", dpi=1500)
plt.show()
print("------- Fin du programme -------")