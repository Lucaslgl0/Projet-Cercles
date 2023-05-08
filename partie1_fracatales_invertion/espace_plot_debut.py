from espace_fonctions import *
import matplotlib.pyplot as plt
#cette partie permet de bien voir comment nous faisons notre cercle inverseur étape par étape 


cer1= Cercles_geo(np.array([0,0])*100,100)  # on crée un objet cer1 qui représente notre cercle n°1
cer2=Cercles_geo(np.array([2,0])*100,100)  # on crée un objet cer2 qui représente notre cercle n°2
cer3=Cercles_geo(np.array([1, 1.7320508075688772])*100,100)  # on crée un objet cer3 qui représente notre cercle n°3

C=[cer1,cer2,cer3]  # on crée une liste comprennant nos trois cercles


# on crée notre cercle par rapport auquel on va faire l'inversion, il apour centre le point d'intersection de cer1 et cer3 et pour rayon 0.1
cercle_inverseur=Cercles_geo((cer3.coordonnee_intersection(cer1)),0.1)


figure, axes = plt.subplots()  
plt.axis([-500, 500, -500, 500])
cercle_2inversé = cer2.inversion_non_infinie(cercle_inverseur) # on fait l'inversion de cer2 par rapport à cercle_inverseur

points = cer1.coordonnees_points_intersection(cercle_inverseur)  # on calcule les coordonnées des points d'intersections de cer1 et cercle_inverseur

cerclenouveaux = cercle_2inversé.insertion(points,cercle_inverseur)  # avec la fonction insertion on calcule les deux cercles tangeants a cer1, cercle_2inversé et cer3

C.append(cerclenouveaux[0].inversion_non_infinie(cercle_inverseur))  # on fait l'inversion d'un nouveau cercle

C.append(cerclenouveaux[1].inversion_non_infinie(cercle_inverseur))  # on fait l'inversion de l'autre cercle

# on plot les cercles
for element in C:
    draw_circle = plt.Circle((element.centre[0], element.centre[1]), element.rayon,fill=False)
    axes.add_artist(draw_circle)

plt.title('Circle')
plt.show()

