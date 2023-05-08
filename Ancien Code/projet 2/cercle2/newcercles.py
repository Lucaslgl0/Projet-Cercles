import numpy as np
from copy import *
import cmath as comp


def au_carre(centre):
    new = np.zeros(2)
    new[0] = centre[0] ** 2 - centre[1] ** 2
    new[1] = 2 * centre[0] * centre[1]
    return new


class Cercles2:
    def __init__(self, centre, rayon_courbure, predecesseur=None):
        self.centre = centre

        self.rayon_de_courbure = rayon_courbure
        self.rayon = 1 / rayon_courbure
        self.predecesseur = predecesseur

    def egal(self, other):
        epsilon = 10 ** (-5)
        nvxcentre = self.centre - other.centre
        if abs(nvxcentre[0]) > epsilon:
            return False

        if abs(nvxcentre[1]) > epsilon:
            return False
        if self.rayon - other.rayon > epsilon:

            return False
        return True

    @staticmethod
    def calul_eq_complex(valeur):

        e2 = comp.polar(valeur)
        module = np.sqrt(e2[0])
        phase = e2[1] / 2
        retour = comp.rect(module, phase)
        return (retour, -retour)

    def calcul_new_cercle(self, cercle2: "Cercles2", cercle3: "Cercles2"):
        "on utilise les 2 relation vue en cour  atention les equations traitent de nombres complexes!"

        a = self.rayon_de_courbure
        b = cercle2.rayon_de_courbure
        c = cercle3.rayon_de_courbure
        val = 2 * np.sqrt(a * b + a * c + b * c)
        rayon_courbure = np.array([val + a + b + c, a + b + c - val])

        e = complex(self.centre[0], self.centre[1])

        f = complex(cercle2.centre[0], cercle2.centre[1])
        g = complex(cercle3.centre[0], cercle3.centre[1])
        a = a * e
        b = b * f
        c = c * g

        B = -2 * (a + b + c)
        C = a**2 + b**2 + c**2 - 2 * (a * b + a * c + b * c)
        determinant = B**2 - 4 * C
        delta = Cercles2.calul_eq_complex(determinant)
        x1 = (-B + delta[0]) / 2
        x2 = (-B + delta[1]) / 2  ##signe OK !

        centre_rayon = np.array(
            [
                ((x1) / rayon_courbure[0], rayon_courbure[0]),

                ((x2) / rayon_courbure[1], rayon_courbure[1]),
            ]
        )
        C = []
        for element in centre_rayon:
            C.append(Cercles2(np.array([element[0].real, element[0].imag]), element[1].real,))
        return C



    


