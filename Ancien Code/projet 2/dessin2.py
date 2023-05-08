from classe_cercles import * 

import matplotlib.pyplot  as plt 
"""cer1=Cercles(np.array([1, 1.7320508075688772])*100,100)
cer2= Cercles(np.array([0,0])*100,100)
cer3=Cercles(np.array([2,0])*100,100)"""
cer1=Cercles(np.array([11, 10]),3.6099122035539)
cer2= Cercles(np.array([5,12]),2.7242058046958)
cer3=Cercles(np.array([6.9707565895051,9.5199179252111]),0.4478311667875)
C=[cer1,cer2,cer3]
print(cer3.centre,cer1.centre)
print(cer3.coordonée_intersection(cer1))

cercvert=Cercles((cer3.coordonée_intersection(cer1)),0.1)

figure, axes = plt.subplots()
plt.axis([-10, 10, -10, 10])
cercle_2inversé=cer2.invertion_non_infini(cercvert)

points=cer1.calculpoints_intersection_cercles(cercvert)

cerclenouveaux=cercle_2inversé.incertions(points,cercvert)


C.append(cerclenouveaux[0].invertion_non_infini(cercvert))

C.append(cerclenouveaux[1].invertion_non_infini(cercvert))

print(cerclenouveaux[1].rayon,'r')
X=Cercles.crea_cercles_nouveaux_et_bien(C,3)
for element in X:
    draw_circle = plt.Circle((element.centre[0], element.centre[1]), element.rayon,fill=False)
    axes.add_artist(draw_circle)

plt.title('Circle')
plt.show()
