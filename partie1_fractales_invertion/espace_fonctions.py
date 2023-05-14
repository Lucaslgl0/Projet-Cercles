import numpy as np
from copy import *
from tqdm import tqdm
from math import floor

class Cercles_geo:
    ###########################################################################
    # Classe traitant les cercles avec leur centre dans R2 et utilise les
    # inversions pour créer de nouveaux cercles tangents
    ###########################################################################
    def __init__(self, centre, rayon, predecesseur=None):
        self.centre = centre
        self.rayon = rayon
        self.predecesseur = predecesseur

    def egal(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : true si self et other sont les même cercles et false sinon
        #######################################################################
        epsilon = 10**(-5)  # permet d'éviter les différences d'arrondis de python
        new_center = self.centre-other.centre
        if abs(new_center[0]) > epsilon:
            return False
        if abs(new_center[1]) > epsilon:
            return False
        if self.rayon - other.rayon > epsilon:
            return False
        return True

    @staticmethod
    def vecteur_normalise(point1, point2):
        #######################################################################
        # input : point1 et point2 deux np.array de taille 2
        # output : np.array de taille 2 un vecteur normalisé qui va du point1
        #          au point2
        #######################################################################
        vecteur_1_2 = ((point2-point1))
        "attention on vas du vect 1 a 2"
        vectnormalise = vecteur_1_2/np.linalg.norm(vecteur_1_2)
        return(vectnormalise)

    def intersection(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : true si self et other s'intersectent et false sinon
        #######################################################################
        vect = Cercles_geo.vecteur_normalise(self.centre, other.centre)
        intersection1 = self.centre+vect*self.rayon-(other.centre-other.rayon*vect)
        intersection2 = self.centre-vect*self.rayon-(other.centre-other.rayon*vect)  # si self est dans other
        intersection3 = self.centre+vect*self.rayon-(other.centre+other.rayon*vect)  # si other est dans self

        epsilon = 10**(-2)

        if abs(intersection1[0]) < epsilon and abs(intersection1[1]) < epsilon:
            return True
        if abs(intersection2[0]) < epsilon and abs(intersection2[1]) < epsilon:
            return True
        if abs(intersection3[0]) < epsilon and abs(intersection3[1]) < epsilon:
            return True
        return False

    def coordonnee_intersection(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : un np.array qui est le point d'intersection de self et other
        #######################################################################
        "on calcul la coordonée de l'intersection de 2 cercles"
        
        vectnormalise = Cercles_geo.vecteur_normalise(self.centre, other.centre)
        return (vectnormalise*self.rayon+self.centre)

    def cercle_dans_cercle(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : true si self est dans other et false sinon
        #######################################################################
        vect = Cercles_geo.vecteur_normalise(self.centre, other.centre)
        if np.linalg.norm(self.centre-other.centre) < self.rayon and np.linalg.norm(self.centre-other.centre) < other.rayon:
            return True
        return False

    def inversion_non_infinie(self, cercleinverseur):
        #######################################################################
        # input : cercleinverseur un autre cerle
        # output : un nouveau cercle qui est l'inversion de self par
        #          cercleinverseur
        #######################################################################
        diffcentre = cercleinverseur.centre-self.centre

        if abs(diffcentre[0]) < 0.00001 and abs(diffcentre[1]) < 0.00001:
            newrayon = (cercleinverseur.rayon**2)/(self.rayon)
            return (Cercles_geo(cercleinverseur.centre, newrayon))

        

        if self.cercle_dans_cercle(cercleinverseur):
            vect = Cercles_geo.vecteur_normalise(cercleinverseur.centre, self.centre)  # vect vas du centre du cercle inverseur au centre du cercle qui vas etre inversé
            pointA = ((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*(vect*(-1))-cercleinverseur.centre)))*(-vect) + cercleinverseur.centre
            pointB = ((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*vect-cercleinverseur.centre)))*vect + cercleinverseur.centre  # le pointB est plus proche du centre du cercle inverseur
            
            rayon = np.linalg.norm(pointA-pointB)/2
            newcenteur = (vect*rayon+pointA)
            return(Cercles_geo(newcenteur, rayon))
        
        vect = Cercles_geo.vecteur_normalise(cercleinverseur.centre, self.centre)  # vect vas du centre du cercle inverseur au centre du cercle qui vas etre inversé
        pointA = ((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*(vect*(-1))-cercleinverseur.centre)))*(vect) + cercleinverseur.centre
        pointB = ((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*vect-cercleinverseur.centre)))*vect + cercleinverseur.centre  # le pointB est plus proche du centre du cercle inverseur
        
        rayon = np.linalg.norm(pointA-pointB)/2
        newcenteur = ((-1)*vect*rayon+pointA)
        return(Cercles_geo(newcenteur, rayon))

    def coordonnees_points_intersection(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : un tuple de np.array qui sont les deux points
        #          d'intersection de self et other
        #######################################################################
        distance = np.sqrt((self.centre[0]-other.centre[0])**2+(self.centre[1]-other.centre[1])**2)

        a = (self.rayon**2-(other.rayon**2)+distance**2)/(2*distance)
        b = ((other.rayon**2)-(self.rayon**2)+distance**2)/(2*distance)

        h = np.sqrt(self.rayon**2-(a**2))
        xcentre = self.centre[0]+(a/distance)*(other.centre[0]-self.centre[0])
        ycentre = self.centre[1]+(a/distance)*(other.centre[1]-self.centre[1])
        point1 = np.array([xcentre-(h*(other.centre[1]-self.centre[1]))/distance, ycentre+(h*(other.centre[0]-self.centre[0]))/distance])
        point2 = np.array([xcentre+(h*(other.centre[1]-self.centre[1]))/distance, ycentre-(h*(other.centre[0]-self.centre[0]))/distance])
        return (point1, point2)

    def insertion(self, droite, other):
        #######################################################################
        # input : un tuple de points qui représente une droite et
        #         other un cercle
        # output : liste de deux nouveaux cercles tangeants à la droite et à
        #          other
        #######################################################################
        nouveaucentre1 = self.centre + 2*self.rayon*Cercles_geo.vecteur_normalise(droite[1], droite[0])
        nouveaucentre2 = self.centre - 2*self.rayon*Cercles_geo.vecteur_normalise(droite[1], droite[0])
        return([Cercles_geo(nouveaucentre1, self.rayon, self.inversion_non_infinie(other)), Cercles_geo(nouveaucentre2, self.rayon, self.inversion_non_infinie(other))])

    @staticmethod
    def suprime_memecercles(C):
        #######################################################################
        # input : C une liste de cercles
        # output : new qui est la liste C sans les cercles identiques
        #######################################################################
        new=C.copy()
        for element1 in new: 
            for element2 in new:
                if element1.egal(element2):
                    new.remove(element2)
            new.append(element1)
        return new
            
    @staticmethod
    def creation_cercles(C, iteration):
        #######################################################################
        # input : C une liste de cercles et iteration un entier
        # output : C avec les nouveaux cercles qui sont tangeants à 3 cercles
        #          de C, ce qui est répété le nombre d'itérations entré en
        #          paramètre
        #         la fonction n'est pas finie et ne rend pas une vraie fractale
        #         elle est donc à améliorer, surtout au niveau de
        #         l'organisation pour la création de nouveaux cercles
        #######################################################################
        for i in range(iteration):
            new = []
            for cercle0 in C:
                for cercle in C:
                    if not cercle.egal(cercle0):
                        if cercle0.intersection(cercle):  # vérifie si cercle est tangeant avec cercle0
                            cercle1 = cercle
                            continue
                for other in C:
                    if other.egal(cercle0) or other.egal(cercle1):
                        continue
                    if other.intersection(cercle1) and other.intersection(cercle0):  # vérifie que other est tangeant avec cercle0 et cercle1
                        point_inverseur = cercle0.coordonnee_intersection(other)  # on calcule le centre du cercle par rapport auquel on va inverser
                        rayon_inverseur = min(cercle0.rayon, other.rayon)/2  # on calcule le rayon du cercle par rapport auquel on ve inverser
                        cercle_inverseur = Cercles_geo(point_inverseur, rayon_inverseur)

                        # on construit la droite permettant l'insertion
                        points = cercle0.coordonnees_points_intersection(cercle_inverseur)
                        cercle2_inverse = cercle1.inversion_non_infinie(cercle_inverseur)
                        points = other.coordonnees_points_intersection(cercle_inverseur)
                        cercles_nouveau = cercle2_inverse.insertion(points, cercle_inverseur)

                        # on ajoute à new nos deux nouveaux cercles tangeants à other, cercle0 et cercle1
                        new.append(cercles_nouveau[0].inversion_non_infinie(cercle_inverseur))
                        new.append(cercles_nouveau[1].inversion_non_infinie(cercle_inverseur))
            C = new+C
            C = Cercles_geo.suprime_memecercles(C)
        return(C)
    

