from newcercles import *

import matplotlib.pyplot as plt

B=-2
C=2
determinant=B**2 - 4*C
delta=Cercles2.calul_eq_complex(determinant)
x1=(-B+delta[0])/2
x2=(-B+delta[1])/2##signe OK !
print(x1,x2)

cercle3 = Cercles2(np.array([1, 1.7320508075688772]), 1)
cercle1 = Cercles2(np.array([0, 0]) * 1, 1)
cercle2 = Cercles2(np.array([2, 0]) * 1, 1)
C = [cercle1, cercle2, cercle3]

figure, axes = plt.subplots()

plt.axis([-5, 5, -5, 5])
for elemtent in cercle2.calcul_new_cercle(cercle1,cercle3):
    C.append(elemtent)
for element in C:
    
    draw_circle = plt.Circle(
        (element.centre[0], element.centre[1]), element.rayon.real, fill=False
    )
    axes.add_artist(draw_circle)

plt.title("Circle")
plt.show()
