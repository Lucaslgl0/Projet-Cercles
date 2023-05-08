import matplotlib.pyplot as plt
from math import *
from cercles import *
from main_cercles import *
from tqdm import tqdm
from random import randint

nombre_de_repet=int(input("nombre de test"))

iterations = int(input("Combien voulez-vous d'itérations ?"))
print("Génération des cercles...")
for i in tqdm(range(1,nombre_de_repet)):
    ok=True
    cercle1_rayon = 1/i
    for j in range (1,nombre_de_repet):
        cercle2_rayon = 1/j
        for k in range (1,nombre_de_repet):

            cercle3_rayon = 1/k
          
            while cercle3_rayon > cercle2_rayon or cercle2_rayon > cercle1_rayon:
                if cercle3_rayon > cercle2_rayon:
                    cercle2_rayon, cercle3_rayon = cercle3_rayon, cercle2_rayon

                if cercle2_rayon > cercle1_rayon:
                    cercle1_rayon, cercle2_rayon = cercle2_rayon, cercle1_rayon

            """
            on fait deux cercles:
            -centre (0,0) et rayon r1+r3
            -centre (r1+r2,0) et rayon r2+r3
            d = r1+r2
            a = (r2²-r1²+d²)/2*d
            h = sqrt(r1²-a²)
            on donc point d'intersection :
            -x = a
            -y = h
            """


            C1 = Cercles(np.array([0, 0]), cercle1_rayon)
            C2 = Cercles(np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon)

            C1_prime = Cercles(np.array([0, 0]), cercle3_rayon + cercle1_rayon)
            C2_prime = Cercles(
                np.array([cercle1_rayon + cercle2_rayon, 0]), cercle2_rayon + cercle3_rayon
            )

            cercle3_centre = C1_prime.calculpoints_intersection_cercles(C2_prime)

            a = cercle3_centre[0][0]
            h = cercle3_centre[0][1]



            C3 = Cercles(np.array([a, h]), cercle3_rayon)


            liste = fractale([C1, C2, C3], iterations)

            for element in liste: 
                if element.rayon_courbure -floor(element.rayon_courbure )!=0:
                    ok=False
                    
                    break
                    

            if ok==True:
                print("yess")
                print(cercle1_rayon,cercle2_rayon, cercle3_rayon)
                

    
            
