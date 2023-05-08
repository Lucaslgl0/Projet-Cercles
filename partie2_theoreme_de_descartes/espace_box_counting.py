from PIL import Image
from numpy import asarray
import numpy as np
from tqdm import tqdm


img = Image.open("essai box counting convolution.png")
numpydata = asarray(img)

liste_i = []
liste_j = []
compteur = 0
for i in tqdm(range(len(numpydata))):
    for j in range(len(numpydata[i])):

        if numpydata[i][j][0] >=255-220:##inverser l'iniégalité(la convolution change les couleur)
                                          ## si convoltution et mettre 255-220(equivalentce ces valeurs) au lieu de 220

            liste_i.append(i)
            liste_j.append(j)
            compteur += 1

print(max(liste_i) - min(liste_i))
print(compteur)
print(np.log(compteur) / np.log(max(liste_i) - min(liste_i)))
