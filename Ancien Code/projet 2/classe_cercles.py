

import numpy as np
from copy import *


class Cercles:
    def __init__(self, centre, rayon,predecesseur=None):
        self.centre = centre
        self.rayon= rayon
        self.predecesseur= predecesseur


    def egal(self,other):
        epsilon=10**(-5)
        nvxcentre=self.centre-other.centre
        if abs(nvxcentre[0])>epsilon:
            return False

        if abs(nvxcentre[1])>epsilon:
            return False
        if self.rayon-other.rayon >epsilon:

            return False
        return True

    @staticmethod
    def calcul_vecteur_normalisé(point1,point2):
        vecteur_1_2=((point2-point1))
        "attention on vas du vect 1 a 2"
        vectnormalise= vecteur_1_2/np.linalg.norm(vecteur_1_2)
        return(vectnormalise)
    "non je deconne gil je t'aime"
    
    def intersection(self,other):
        "on regarde si 2 cercles s'intersecte vraiment "
        
        vect = Cercles.calcul_vecteur_normalisé(self.centre,other.centre)
        "if np.array_equal(self.centre+vect*self.rayon,other.centre-other.rayon*vect):"
        intersection1=self.centre+vect*self.rayon-(other.centre-other.rayon*vect)

        intersection2=self.centre-vect*self.rayon-(other.centre-other.rayon*vect)#cas self dedans 
        intersection3=self.centre+vect*self.rayon-(other.centre+other.rayon*vect)#cas self englobe 
        epsilon=10**(-2)

        if abs(intersection1[0])<epsilon and abs(intersection1[1])<epsilon :
            return True
        
        if abs(intersection2[0])<epsilon and abs(intersection2[1])<epsilon:
            return True
        
        if abs(intersection3[0])<epsilon and abs(intersection3[1])<epsilon:
            return True
        """print(self.centre+vect*self.rayon)
        print(other.centre-other.rayon*vect)
        print(self.centre+vect*self.rayon-(other.centre-other.rayon*vect))
        "si on a une interséction pas tjr bon la érreur a 10-16"
        print(np.array_equal(self.centre+vect*self.rayon,other.centre-other.rayon*vect))"""
        return False
    
    def coordonée_intersection(self,other):
        "on calcul la coordonée de l'intersection de 2 cercles"
        assert self.intersection(other)== True 
        vectnormalise=Cercles.calcul_vecteur_normalisé(self.centre, other.centre)
        return (vectnormalise*self.rayon+self.centre)
    

    def cercle_dans_cercle(self,other):
        vect=Cercles.calcul_vecteur_normalisé(self.centre,other.centre)
        if np.linalg.norm(self.centre-other.centre)<self.rayon and np.linalg.norm(self.centre-other.centre)<other.rayon:
            return True
        return False

    
    def invertion_non_infini(self,cercleinverseur):
        """attention le certre de self n'est pas envoyer sur le centre du nouveau cercle !!
        attention cas part si les deux cercles on le meme centre"""
        diffcentre=cercleinverseur.centre-self.centre
        if abs(diffcentre[0])<0.00001 and abs(diffcentre[1])<0.00001:
            newrayon=(cercleinverseur.rayon**2)/(self.rayon)
            return (Cercles(cercleinverseur.centre,newrayon))
        if self.cercle_dans_cercle(cercleinverseur):
            
            vect= Cercles.calcul_vecteur_normalisé(cercleinverseur.centre,self.centre)##vect vas di cercle inverceur au cercle qui vas etre invercé
            pointA=((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*(vect*(-1))-cercleinverseur.centre)))*(-vect) + cercleinverseur.centre
            pointB=((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*vect-cercleinverseur.centre)))*vect + cercleinverseur.centre

            ##pointB est plus proche du centre du cercleinverceur attention on inverce point loin devien point proche
            rayon=np.linalg.norm(pointA-pointB)/2
            newcenteur=(vect*rayon+pointA)
            return(Cercles(newcenteur,rayon))

        vect= Cercles.calcul_vecteur_normalisé(cercleinverseur.centre,self.centre)##vect vas di cercle inverceur au cercle qui vas etre invercé
        pointA=((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*(vect*(-1))-cercleinverseur.centre)))*vect + cercleinverseur.centre
        pointB=((cercleinverseur.rayon**2)/np.linalg.norm((self.centre+self.rayon*vect-cercleinverseur.centre)))*vect + cercleinverseur.centre

        ##pointB est plus proche du centre du cercleinverceur attention on inverce point loin devien point proche
        rayon=np.linalg.norm(pointA-pointB)/2
        newcenteur=((-1)*vect*rayon+pointA)
        return(Cercles(newcenteur,rayon))
    
    def calculpoints_intersection_cercles(self,other):
        distance=np.sqrt((self.centre[0]-other.centre[0])**2+(self.centre[1]-other.centre[1])**2)

        a=(self.rayon**2-(other.rayon**2)+distance**2)/(2*distance)
        b=((other.rayon**2)-(self.rayon**2)+distance**2)/(2*distance)

        h=np.sqrt(self.rayon**2-(a**2))
        xcentre=self.centre[0]+(a/distance)*(other.centre[0]-self.centre[0])
        ycentre=self.centre[1]+(a/distance)*(other.centre[1]-self.centre[1])###voir si on peut pas faire plus efficasse entre les 2 en faisant direct les opé sur les tab
        point1=np.array([xcentre-(h*(other.centre[1]-self.centre[1]))/distance,ycentre+(h*(other.centre[0]-self.centre[0]))/distance])
        point2=np.array([xcentre+(h*(other.centre[1]-self.centre[1]))/distance,ycentre-(h*(other.centre[0]-self.centre[0]))/distance])
        return (point1,point2)

    def incertions(self,droite1,cercle_vert):
        "on suppose que tout c'est bien passé dans l'invertion notre cercle est dans les deux droites"
        "de plus droite une et droite 2 sont des tuple de 1 point et un vect unitaire et elles sont parraléles"
        'on commence par calculer la distance entre les 2 droites pour cela il nous faut les equation de droites sous la forme y=a+mx'
        """m1=(droite1[1][1]-droite1[1][1])/(droite1[0][1]-droite1[0][1])
        a1=droite1[1]-m1*droite1[0]
        m2=(droite2[1][1]-droite2[1][1])/(droite2[0][1]-droite2[0][1])
        a2=droite2[1]-m2*droite2[0]
        assert m1==m2
        'on met la fromule de distance entre deux droites'
        distance=abs(a1-a2)/np.sqrt(m1+1)
        "ainsi on connais les rayons des cercles"""
        "tout ca inutille  !!!"
        distancedroites=2*self.rayon
        nouveaucentre1=self.centre + 2*self.rayon*Cercles.calcul_vecteur_normalisé(droite1[1],droite1[0])
        nouveaucentre2= self.centre -2*self.rayon*Cercles.calcul_vecteur_normalisé(droite1[1],droite1[0])
        return([Cercles(nouveaucentre1,self.rayon,self.invertion_non_infini(cercle_vert)),Cercles(nouveaucentre2,self.rayon,self.invertion_non_infini(cercle_vert))])
    
    @staticmethod
    def suprime_memecercles(C):
        new=C.copy()
        for element1 in new: 
            for element2 in new:
                if element1.egal(element2):
                    new.remove(element2)
            new.append(element1)
        return new
            


        
    

                
            




            
    @staticmethod
    def crea_cercles_nouveaux_et_bien(C,iteration):


        for i in range(iteration):
            new=[]
            for cercle0 in C:
                for cer in C:
                    if not cer.egal(cercle0):
                        if cercle0.intersection(cer):
                            cercle1=cer
                            continue

                for other in C :
                    if other.egal(cercle0) or other.egal(cercle1):
                             
                                continue
                        
                    if other.intersection(cercle1) and other.intersection(cercle0):
                            
                        
                            
                        point_vert=cercle0.coordonée_intersection(other)

                        " c'est avec eu que l'on veux contruire les cercles"
                        rayon_vert=min(cercle0.rayon,other.rayon)/2##ok 

                        cercle_vert=Cercles(point_vert,rayon_vert)
                     
                        "on construit mtn nos droites tout d'abord les point pour faire notre droite "
                        points=cercle0.calculpoints_intersection_cercles(cercle_vert)
                        cercle2_inverse=cercle1.invertion_non_infini(cercle_vert)##l'invertion ne marche pas 
        
                        points=other.calculpoints_intersection_cercles(cercle_vert)
                        cercles_nouveau=cercle2_inverse.incertions(points,cercle_vert)
                    
                        new.append(cercles_nouveau[0].invertion_non_infini(cercle_vert))

                        new.append(cercles_nouveau[1].invertion_non_infini(cercle_vert))
            C=new+C

            C=Cercles.suprime_memecercles(C)
        return(C)
        



                    
                


            

            





""""
a1=np.zeros(2,)
                            a1[0]=point_vert[0]+(rayon_vert**2)/(2*min(cercle0.rayon,other.rayon))
                            a1[1]=point_vert[1]+(rayon_vert**2-rayon_vert**4)/(4*min(cercle0.rayon,other.rayon))
                            a2=np.zeros(2,)
                            a2[0]=point_vert[0]+(rayon_vert**2)/(2*min(cercle0.rayon,other.rayon))
                            a2[1]=point_vert[1]-(rayon_vert**2-rayon_vert**4)/(4*min(cercle0.rayon,other.rayon))b1=np.zeros(2,)
                        b1[0]=point_vert[0]-(rayon_vert**2)/(2*min(cercle0.rayon,other.rayon))
                        b1[1]=point_vert[1]+(rayon_vert**2-rayon_vert**4)/(4*min(cercle0.rayon,other.rayon))
                        b2=np.zeros(2,)
                        b2[0]=point_vert[0]-(rayon_vert**2)/(2*min(cercle0.rayon,other.rayon))
                        b2[1]=point_vert[1]-(rayon_vert**2-rayon_vert**4)/(4*min(cercle0.rayon,other.rayon))"""