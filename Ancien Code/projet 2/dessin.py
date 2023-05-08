from classe_cercles import * 
cercle3=Cercles(np.array([1, 1.7320508075688772])*100,100)
cercle1= Cercles(np.array([0,0])*100,100)
cercle2=Cercles(np.array([2,0])*100,100)

C=[cercle1,cercle2,cercle3]

import matplotlib.pyplot as plt
"on vas tester on vas tout d'abord contruire le cercle vert"

cercvert=Cercles((cercle2.coordonée_intersection(cercle3)),50)

figure, axes = plt.subplots()

plt.axis([-500, 500, -500, 500])
cercle_2inversé=cercle1.invertion_non_infini(cercvert)

points=cercle3.calculpoints_intersection_cercles(cercvert)

celclenouveaux=cercle_2inversé.incertions(points,cercvert)


"""C.append(celclenouveaux[0].invertion_non_infini(cercvert))

C.append(celclenouveaux[1].invertion_non_infini(cercvert))"""

X=Cercles.crea_cercles_nouveaux_et_bien(C,7)
print(X)

for element in X:
    
    ##mes element n'ont pas de centre ni de rayon 
    draw_circle = plt.Circle((element.centre[0], element.centre[1]), element.rayon,fill=False)
    axes.add_artist(draw_circle)

plt.title('Circle')
plt.show()

"""a1=np.zeros(2,)
a1[0]=cercvert.centre[0]+(cercvert.rayon**2)/(2*min(cercle1.rayon,cercle3.rayon))
a1[1]=cercvert.centre[1]+(cercvert.rayon**2-cercvert.rayon**4)/(4*min(cercle1.rayon,cercle3.rayon))
a2=np.zeros(2,)
a2[0]=cercvert.centre[0]+(cercvert.rayon**2)/(2*min(cercle1.rayon,cercle3.rayon))
a2[1]=cercvert.centre[1]-(cercvert.rayon**2-cercvert.rayon**4)/(4*min(cercle1.rayon,cercle3.rayon))
b1=np.zeros(2,)
b1[0]=cercvert.centre[0]-(cercvert.rayon**2)/(2*min(cercle1.rayon,cercle3.rayon))
b1[1]=cercvert.centre[1]+(cercvert.rayon**2-cercvert.rayon**4)/(4*min(cercle3.rayon,cercle1.rayon))
b2=np.zeros(2,)
b2[0]=cercvert.centre[0]-(cercvert.rayon**2)/(2*min(cercle1.rayon,cercle3.rayon))
b2[1]=cercvert.centre[1]-(cercvert.rayon**2-cercvert.rayon**4)/(4*min(cercle3.rayon,cercle1.rayon))"""