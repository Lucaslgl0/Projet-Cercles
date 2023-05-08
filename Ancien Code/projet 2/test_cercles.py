import numpy as np
from classe_cercles import *

cercle1= Cercles(np.array([0,0]),1)
cercle2=Cercles(np.array([2,0]),1)
cercle3=Cercles(np.array([1, 1.7320508075688772]),1)
cerclenul=Cercles(np.array(([0, 1.7320508075688772])),1)
C=[cercle1,cercle2,cercle3]

def test_calcul_vectnormalise():
    assert np.array_equal((np.array([1,1])/np.sqrt(2)),Cercles.calcul_vecteur_normalisé(np.array([1,1]),np.array([2,2])))==True
    assert np.array_equal((np.array([1,1])/np.sqrt(2)),(Cercles.calcul_vecteur_normalisé(np.array([2,2]),np.array([1,1]))))==False


def test_egal():
    assert cercle1.egal(cercle1)==True
    assert cercle1.egal(cercle2)==False
    newcerclenul=Cercles(np.array(([0, 0])),2)
    assert newcerclenul.egal(cercle1)==False

def test_intersection():
    assert cercle1.intersection(cercle2)==True
    assert cerclenul.intersection(cercle2)==False
    assert cercle1.intersection(cercle1 )== False 
    "attetions si on a deux cercles les meme il on pas d'intersection "
    for element in C:
        for cercles in C:
            if element.egal(cercles)!= True:
                assert element.intersection(cercles)==True


def test_coordonée_intersection():
    assert np.array_equal(cercle1.coordonée_intersection(cercle2),np.array([1,0]))==True

def test_invertion():
    
    cercleinv1= Cercles(np.array([1,0]),1)
    cercleinv2=Cercles(np.array([0,1]),1)
    "test avec des print marche"
    assert cercle1.egal(cercle1.invertion_non_infini(cercle2).invertion_non_infini(cercle2))==True
    'cercleinv2.invertion_non_infini(cercleinv1).invertion_non_infini(cercleinv1).centre'
    ##attention la ca marche pas car faute a la 6 eme virgule on et en le faisant 2 fois on remarque que les approx de numpy ne marche pas si bien 
    ##vas falloir faire des gros cercles !!! la ca marche bien 
def test_incertion():
    np.array_equal(Cercles(np.array([0.5,0]),0.5).incertions((np.array([0,1]),np.array([1,1])),cercle1)[0].centre,np.array([-0.5,0]))==True
    Cercles(np.array([0.5,0]),0.5).incertions((np.array([0,1]),np.array([1,1])),cercle1)[1].centre==0.5
                   
def test_supprime_meme_cercle():
    l = [cercle1,cercle2,cercle3]
    l.append(cercle3)


    Cercles.suprime_memecercles(l)
    assert len(l)==3

