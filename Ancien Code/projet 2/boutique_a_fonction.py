
import numpy as np
from copy import *
"on vas taff avec des cercles tq cercle=(mat np,rayon)"
"question on fait ca en orienté objet ? ca serais pas mal on verrais mieux ce que l'on fait "

def calcul_vecteur_normalisé(point1,point2):
    vecteur_1_2=((point2-point1))
    "attention on vas du vect 1 a 2"
    vectnormalise= vecteur_1_2/np.linalg.norm(vecteur_1_2)
    return(vectnormalise)



def intersection(cercle1,cercle2):
    "on regarde si 2 cercles s'intersecte vraiment "
    vect=calcul_vecteur_normalisé(cercle1[0],cercle2[0])
    if cercle1[0]+vect*cercle1[1]==cercle2[0]-cercle2[1]*vect:
        return True
    return False


def coordonée_intersection(cercle1,cercle2):
    "on calcul la coordonée de l'intersection de 2 cercles"
    assert intersection(cercle1,cercle2)== True 
    vectnormalise=calcul_vecteur_normalisé(cercle1[0], cercle2[0])
    return (vectnormalise*cercle1[1]+cercle1[0])

def invertion_non_infini(cercle1,cercleinverse):
    vect= calcul_vecteur_normalisé(cercle1[0],cercleinverse[0])
    newcenter=(cercle1[1]**2)/np.linalg.norm((cercle1[0]-cercleinverse[0]))*vect + cercle1[0]
    rayon=np.linalg.norm(newcenter-((cercle1[1]**2)/np.linalg.norm((cercle1[0]-(-vect*cercleinverse[1]+cercleinverse[0]))) + cercle1[0]))
    return((newcenter,rayon))
    

def crea_cercles(C,iteration):
    "C est la liste de 3 cercles que l'on a on les sup deja tangeants on vas crée un systéme d'incides pour id les cercles tangeants"
    liste_cercles=deepcopy(C)
    new=[C]
    "vas etre le liste des cercles que l'on vas construire comme ca on ne refait pas plein de fois les memes cercles"
    for i in range (iteration):
        pass 
    



print(np.array([0,0])-np.array([1,0]))


















"""if intersection(cercle1,cercle3) and intersection(cercle2,cercle3):
        point_vert=coordonée_intersection(cercle1,cercle2)
        rayon_vert=min(cercle1[1],cercle2[1])/2
        "on construit mtn nos droites tout d'abord les point pour faire notre droite "
        a1=np.zeros(2,)
        a1[0]=point_vert[0]+(rayon_vert**2)/(2*min(cercle1[1],cercle2[1]))
        a1[1]=point_vert[1]+(rayon_vert**2-rayon_vert**4)/(4*min(cercle1[1],cercle2[1]))
        a2=np.zeros(2,)
        a2[0]=point_vert[0]+(rayon_vert**2)/(2*min(cercle1[1],cercle2[1]))
        a2[1]=point_vert[1]-(rayon_vert**2-rayon_vert**4)/(4*min(cercle1[1],cercle2[1]))
        b1=np.zeros(2,)
        b1[0]=point_vert[0]-(rayon_vert**2)/(2*min(cercle1[1],cercle2[1]))
        b1[1]=point_vert[1]+(rayon_vert**2-rayon_vert**4)/(4*min(cercle1[1],cercle2[1]))
        b2=np.zeros(2,)
        b2[0]=point_vert[0]-(rayon_vert**2)/(2*min(cercle1[1],cercle2[1]))
        b2[1]=point_vert[1]-(rayon_vert**2-rayon_vert**4)/(4*min(cercle1[1],cercle2[1]))
        "puis faire les invertion du cercle 3 et cerreles 2 nouveau et refaire une invertion =)"""

