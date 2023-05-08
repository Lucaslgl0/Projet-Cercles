from espace_fonctions import *
import numpy as np
import matplotlib.pyplot as plt

cercle3 = Cercles_geo(np.array([1, 1.7320508075688772]) * 100, 100)
cercle1 = Cercles_geo(np.array([0, 0]) * 100, 100)
cercle2 = Cercles_geo(np.array([2, 0]) * 100, 100)

C = [cercle2, cercle1, cercle3]

figure, axes = plt.subplots()

plt.axis([-150, 350, -250, 350])

X = Cercles_geo.creation_cercles(C, 8)
print(X)

for element in X:
    draw_circle = plt.Circle(
        (element.centre[0], element.centre[1]), element.rayon, fill=False, linewidth=0.1
    )
    axes.add_artist(draw_circle)

plt.title("Circle")
plt.savefig("fractale_invertion",dpi=1500)