from classe_cercles import *

import matplotlib.pyplot as plt


cercle3 = Cercles(np.array([1, 1.7320508075688772]), 1)
cercle1 = Cercles(np.array([0, 0]) * 1, 1)
cercle2 = Cercles(np.array([2, 0]) * 1, 1)
C = [cercle1, cercle2, cercle3]
cercvert = Cercles((cercle1.coordonée_intersection(cercle2)), 0.5)

figure, axes = plt.subplots()
plt.axis([-5, 5, -5, 5])
cercle_2inversé = cercle3.invertion_non_infini(cercvert)
print(cercvert.centre, cercvert.rayon)
print("ok")
points = cercle3.calculpoints_intersection_cercles(cercvert)


cerclenouveaux = cercle_2inversé.incertions(points, cercvert)


C.append(cerclenouveaux[0].invertion_non_infini(cercvert))

C.append(cerclenouveaux[1].invertion_non_infini(cercvert))

print(cerclenouveaux[1].rayon, "r")


cercvert_new = Cercles(
    (cercle3.coordonée_intersection(cerclenouveaux[0].invertion_non_infini(cercvert))),
    min(cerclenouveaux[0].rayon, cercle3.rayon) / 2,
)


cercle_1inversé = cercle1.invertion_non_infini(cercvert_new)

points = cercle3.calculpoints_intersection_cercles(cercvert_new)

celclenouveaux_new = cercle_1inversé.incertions(points, cercvert_new)
C.append(celclenouveaux_new[0].invertion_non_infini(cercvert_new))

C.append(celclenouveaux_new[1].invertion_non_infini(cercvert_new))
for element in C:
    draw_circle = plt.Circle(
        (element.centre[0], element.centre[1]), element.rayon, fill=False
    )
    axes.add_artist(draw_circle)

plt.title("Circle")
plt.show()
