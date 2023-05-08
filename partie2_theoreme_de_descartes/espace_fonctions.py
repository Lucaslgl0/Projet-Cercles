import numpy as np
from copy import *
import cmath as comp
import copy
from tqdm import tqdm
from math import floor
from termcolor import colored


class Cercles_complexe:
    ###########################################################################
    # Classe traitant les cercles avec leur centre en complexe et utilise les
    # relations de Descartes
    ###########################################################################
    def __init__(self, centre, rayon, predecesseur=None):
        self.centre = centre
        self.rayon = rayon
        self.courbure = 1 / rayon
        self.predecesseur = predecesseur

    def egal(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : true si self et other sont les même cercles et false sinon
        #######################################################################
        epsilon = 10 ** (-5)  # permet d'éviter les différences d'arrondis de python
        nvxcentre = self.centre - other.centre
        if abs(nvxcentre[0]) > epsilon:
            return False

        if abs(nvxcentre[1]) > epsilon:
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
        vecteur_1_2 = point2 - point1
        vectnormalise = vecteur_1_2 / np.linalg.norm(vecteur_1_2)
        return vectnormalise

    def intersection(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : true si self et other s'intersectent et false sinon
        #######################################################################
        vect = Cercles_complexe.vecteur_normalise(self.centre, other.centre)
        intersection1 = (
            self.centre + vect * self.rayon - (other.centre - other.rayon * vect)
        )
        intersection2 = (
            self.centre - vect * self.rayon - (other.centre - other.rayon * vect)
        )  # si self est dans other
        intersection3 = (
            self.centre + vect * self.rayon - (other.centre + other.rayon * vect)
        )  # si other est dans self
        epsilon = 10 ** (-5)

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
        assert self.intersection(other)
        vectnormalise = Cercles_complexe.vecteur_normalise(self.centre, other.centre)
        return vectnormalise * self.rayon + self.centre

    def cercle_dans_cercle(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : true si self est dans other et false sinon
        #######################################################################
        vect = Cercles_complexe.vecteur_normalise(self.centre, other.centre)
        if (
            np.linalg.norm(self.centre - other.centre) < self.rayon
            and np.linalg.norm(self.centre - other.centre) < other.rayon
        ):
            return True
        return False

    def inversion_non_infinie(self, cercleinverseur):
        #######################################################################
        # input : cercleinverseur un autre cerle
        # output : un nouveau cercle qui est l'inversion de self par
        #          cercleinverseur
        #######################################################################

        # attention le centre de self n'est pas envoyé sur le centre du nouveau cercle
        # attention cas à part si les deux cercles ont le même centre

        diffcentre = cercleinverseur.centre - self.centre

        if abs(diffcentre[0]) < 0.00001 and abs(diffcentre[1]) < 0.00001:
            newrayon = (cercleinverseur.rayon**2) / (self.rayon)
            return Cercles_complexe(cercleinverseur.centre, newrayon)

        vect = Cercles_complexe.vecteur_normalise(
            cercleinverseur.centre, self.centre
        )  # vect va du cercle inverseur au cercle qui va être inversé
        pointA = (
            (cercleinverseur.rayon**2)
            / np.linalg.norm(
                (self.centre + self.rayon * (vect * (-1)) - cercleinverseur.centre)
            )
        ) * vect + cercleinverseur.centre
        pointB = (
            (cercleinverseur.rayon**2)
            / np.linalg.norm((self.centre + self.rayon * vect - cercleinverseur.centre))
        ) * vect + cercleinverseur.centre
        # le pointB est plus proche du centre que du cercle inverseur

        if self.cercle_dans_cercle(cercleinverseur):
            rayon = np.linalg.norm(pointA - pointB) / 2
            newcenter = vect * rayon + pointA
            return Cercles_complexe(newcenter, rayon)

        rayon = np.linalg.norm(pointA - pointB) / 2
        newcenter = (-1) * vect * rayon + pointA
        return Cercles_complexe(newcenter, rayon)

    def coordonnees_points_intersection(self, other):
        #######################################################################
        # input : other un autre cerle
        # output : un tuple de np.array qui sont les deux points
        #          d'intersection de self et other
        #######################################################################
        distance = np.sqrt(
            (self.centre[0] - other.centre[0]) ** 2
            + (self.centre[1] - other.centre[1]) ** 2
        )

        a = abs((self.rayon**2 - (other.rayon**2) + distance**2) / (2 * distance))
        b = abs(
            ((other.rayon**2) - (self.rayon**2) + distance**2) / (2 * distance)
        )

        h = np.sqrt(abs(self.rayon**2 - (a**2)))
        xcentre = self.centre[0] + (a / distance) * (other.centre[0] - self.centre[0])
        ycentre = self.centre[1] + (a / distance) * (other.centre[1] - self.centre[1])
        point1 = np.array(
            [
                xcentre - (h * (other.centre[1] - self.centre[1])) / distance,
                ycentre + (h * (other.centre[0] - self.centre[0])) / distance,
            ]
        )
        point2 = np.array(
            [
                xcentre + (h * (other.centre[1] - self.centre[1])) / distance,
                ycentre - (h * (other.centre[0] - self.centre[0])) / distance,
            ]
        )
        return (point1, point2)

    def insertion(self, droite1, cercle_inverseur):
        #######################################################################
        # input : un tuple de points qui représente une droite et
        #         other un cercle
        # output : liste de deux nouveaux cercles tangents à la droite et à
        #          other
        #######################################################################
        nouveaucentre1 = (
            self.centre
            + 2
            * self.rayon
            * Cercles_complexe.vecteur_normalise(droite1[1], droite1[0])
        )
        nouveaucentre2 = (
            self.centre
            - 2
            * self.rayon
            * Cercles_complexe.vecteur_normalise(droite1[1], droite1[0])
        )
        return [
            Cercles_complexe(
                nouveaucentre1, self.rayon, self.inversion_non_infinie(cercle_inverseur)
            ),
            Cercles_complexe(
                nouveaucentre2, self.rayon, self.inversion_non_infinie(cercle_inverseur)
            ),
        ]

    @staticmethod
    def suprime_memecercles(C):
        #######################################################################
        # input : C une liste de cercles
        # output : new qui est la liste C sans les cercles identiques
        #######################################################################
        new = C.copy()
        for element1 in new:
            for element2 in new:
                if element1.egal(element2):
                    new.remove(element2)
            new.append(element1)
        return new

    @staticmethod
    def calul_eq_complex(valeur):
        #######################################################################
        # input : valeur un nombre complexe sous la forme a + ib
        # output : renvoie la valeur au carré
        #######################################################################
        e2 = comp.polar(valeur)
        module = np.sqrt(e2[0])
        phase = e2[1] / 2
        retour = comp.rect(module, phase)
        return (retour, -retour)

    def calcul_new_cercle(
        self, cercle2: "Cercles_complexe", cercle3: "Cercles_complexe"
    ):
        #######################################################################
        # input : cercle2 et cercle3 des Cercles
        # output : C une liste avec les nouveaux cercles tangents à self,
        #          cercle2 et cercle3
        #######################################################################

        # on utilise les 2 relations vues en cours
        # attention les équations traitent de nombres complexes

        a = self.courbure
        b = cercle2.courbure
        c = cercle3.courbure
        val = 2 * np.sqrt(a * b + a * c + b * c)
        courbure = np.array([val + a + b + c, a + b + c - val])
        epsilon = 10 ** (-10)
        if (a + b + c - val).real == 0:
            return [None, None]

        if (val + a + b + c).real == 0:
            return [None, None]

        e = complex(self.centre[0], self.centre[1])
        f = complex(cercle2.centre[0], cercle2.centre[1])
        g = complex(cercle3.centre[0], cercle3.centre[1])
        a = a * e
        b = b * f
        c = c * g

        B = -2 * (a + b + c)
        C = a**2 + b**2 + c**2 - 2 * (a * b + a * c + b * c)
        determinant = B**2 - 4 * C
        delta = self.calul_eq_complex(determinant)
        x1 = (-B + delta[0]) / 2
        x2 = (-B + delta[1]) / 2

        centre_rayon = np.array(
            [
                ((x1) / courbure[0], courbure[0]),
                ((x2) / courbure[1], courbure[1]),
            ]
        )
        C = []
        for element in centre_rayon:
            C.append(
                Cercles_complexe(
                    np.array([element[0].real, element[0].imag]),
                    1 / element[1].real,
                )
            )
        return C

    @staticmethod
    def creation_cercle(C, iteration):
        #######################################################################
        # input : C une liste de cercles et iteration un entier
        # output : C avec les nouveaux cercles qui sont tangents à 3 cercles
        #          de C, ce qui est répété le nombre d'itérations entré en
        #          paramètre
        #######################################################################
        for i in range(iteration):
            new = []
            for cercle0 in C:
                for cercle in C:
                    if not cercle.egal(cercle0):
                        if cercle0.intersection(
                            cercle
                        ):  # vérifie si cercle est tangent avec cercle0
                            cercle1 = cercle
                            continue
                for other in C:
                    if other.egal(cercle0) or other.egal(cercle1):
                        continue

                    if other.intersection(cercle1) and other.intersection(
                        cercle0
                    ):  # vérifie si other est tangent avec cercle0 et cercle1
                        # on construit le cercle par rapport auquel on va faire l'inversion
                        point_inverseur = cercle0.coordonnee_intersection(other)
                        rayon_inverseur = min(cercle0.rayon, other.rayon) / 2
                        cercle_inverseur = Cercles_complexe(
                            point_inverseur, rayon_inverseur
                        )

                        # on construit la droite permettant l'insertion
                        points = cercle0.coordonnees_points_intersection(
                            cercle_inverseur
                        )
                        cercle2_inverse = cercle1.inversion_non_infinie(
                            cercle_inverseur
                        )
                        points = other.coordonnees_points_intersection(cercle_inverseur)
                        cercles_nouveau = cercle2_inverse.insertion(
                            points, cercle_inverseur
                        )

                        new.append(
                            cercles_nouveau[0].inversion_non_infinie(cercle_inverseur)
                        )
                        new.append(
                            cercles_nouveau[1].inversion_non_infinie(cercle_inverseur)
                        )
            C = new + C
            C = Cercles_complexe.suprime_memecercles(C)
        return C

    @staticmethod
    def crea_quadruple(liste_cercles):
        ###########################################################################
        # input : liste_cercles une liste d'objets de type Cercles
        # output : liste2 une liste d'objets de type Cercles
        ###########################################################################
        liste2 = []
        for i in range(4):
            liste1 = []
            k = (
                2
                * (
                    liste_cercles[(i + 1) % 4].courbure
                    + liste_cercles[(i + 2) % 4].courbure
                    + liste_cercles[(i + 3) % 4].courbure
                )
                - liste_cercles[i].courbure
            )
            x = (
                2
                * (
                    (liste_cercles[(i + 1) % 4].centre[0])
                    * liste_cercles[(i + 1) % 4].courbure
                    + (liste_cercles[(i + 2) % 4].centre[0])
                    * liste_cercles[(i + 2) % 4].courbure
                    + (liste_cercles[(i + 3) % 4].centre[0])
                    * liste_cercles[(i + 3) % 4].courbure
                )
                - (liste_cercles[i].centre[0]) * liste_cercles[i].courbure
            ) / k
            y = (
                2
                * (
                    (liste_cercles[(i + 1) % 4].centre[1])
                    * liste_cercles[(i + 1) % 4].courbure
                    + (liste_cercles[(i + 2) % 4].centre[1])
                    * liste_cercles[(i + 2) % 4].courbure
                    + (liste_cercles[(i + 3) % 4].centre[1])
                    * liste_cercles[(i + 3) % 4].courbure
                )
                - (liste_cercles[i].centre[1]) * liste_cercles[i].courbure
            ) / k
            for j in range(i):
                liste1.append(liste_cercles[j])
            liste1.append(Cercles_complexe(np.array([x, y]), 1 / k))
            for j in range(i + 1, 4):
                liste1.append(liste_cercles[j])
            liste2.append(liste1)
        return liste2

    @staticmethod
    def fractale(liste_cercles, n):
        ###########################################################################
        # input : liste_cercles une liste d'objets de type Cercles et n un entier
        #         qui est le nombre d'itération voulue
        # output : liste1 une liste d'objets de type Cercles avec les nouveaux
        #          cercles tangents à trois cercles de la liste itéré n-fois
        ###########################################################################
        liste1 = []
        liste2 = []
        eps = 10 ** (-5)
        for cercle in liste_cercles:
            liste1.append(cercle)
        cercle4 = (liste1[0].calcul_new_cercle(liste1[1], liste1[2]))[1]
        if cercle4 is None:
            print(colored("Fractale avec cercle infini", "red"))
            return []
        ##mettre un max si on souhaite ne pas avoir des cercles de courbure trés petites 
        liste1.append(cercle4)
        liste_cercles.append(cercle4)
        liste2.append(liste_cercles)
        for i in range(n):
            print("Création de l'itération ", i + 1)
            liste2_prime = []
            for j in tqdm(range(len(liste2))):###mettre tqdm si on veux voir la rapidité de la construction des fractales
                quadruple_cercles = liste2.pop()
                quadruple2_cercles = Cercles_complexe.crea_quadruple(quadruple_cercles)
                cercle1_prime = quadruple2_cercles[0][0]
                test = 0
                for cercle in liste1:
                    if (
                        (
                            cercle1_prime.rayon <= cercle.rayon + eps
                            and cercle1_prime.rayon >= cercle.rayon - eps
                        )
                        and (
                            cercle1_prime.centre[0] <= cercle.centre[0] + eps
                            and cercle1_prime.centre[0] >= cercle.centre[0] - eps
                        )
                        and (
                            cercle1_prime.centre[1] <= cercle.centre[1] + eps
                            and cercle1_prime.centre[1] >= cercle.centre[1] - eps
                        )
                    ):
                        test = 1
                if test == 0:
                    liste1.append(cercle1_prime)
                cercle2_prime = quadruple2_cercles[1][1]
                test = 0
                for cercle in liste1:
                    if (
                        (
                            cercle2_prime.rayon <= cercle.rayon + eps
                            and cercle2_prime.rayon >= cercle.rayon - eps
                        )
                        and (
                            cercle2_prime.centre[0] <= cercle.centre[0] + eps
                            and cercle2_prime.centre[0] >= cercle.centre[0] - eps
                        )
                        and (
                            cercle2_prime.centre[1] <= cercle.centre[1] + eps
                            and cercle2_prime.centre[1] >= cercle.centre[1] - eps
                        )
                    ):
                        test = 1
                if test == 0:
                    liste1.append(cercle2_prime)
                cercle3_prime = quadruple2_cercles[2][2]
                test = 0
                for cercle in liste1:
                    if (
                        (
                            cercle3_prime.rayon <= cercle.rayon + eps
                            and cercle3_prime.rayon >= cercle.rayon - eps
                        )
                        and (
                            cercle3_prime.centre[0] <= cercle.centre[0] + eps
                            and cercle3_prime.centre[0] >= cercle.centre[0] - eps
                        )
                        and (
                            cercle3_prime.centre[1] <= cercle.centre[1] + eps
                            and cercle3_prime.centre[1] >= cercle.centre[1] - eps
                        )
                    ):
                        test = 1
                if test == 0:
                    liste1.append(cercle3_prime)
                cercle4_prime = quadruple2_cercles[3][3]
                test = 0
                for cercle in liste1:
                    if (
                        (
                            cercle4_prime.rayon <= cercle.rayon + eps
                            and cercle4_prime.rayon >= cercle.rayon - eps
                        )
                        and (
                            cercle4_prime.centre[0] <= cercle.centre[0] + eps
                            and cercle4_prime.centre[0] >= cercle.centre[0] - eps
                        )
                        and (
                            cercle4_prime.centre[1] <= cercle.centre[1] + eps
                            and cercle4_prime.centre[1] >= cercle.centre[1] - eps
                        )
                    ):
                        test = 1
                if test == 0:
                    liste1.append(cercle4_prime)
                for quadruple in quadruple2_cercles:
                    liste2_prime.append(quadruple)
            liste2 = copy.deepcopy(liste2_prime)

        return liste1
