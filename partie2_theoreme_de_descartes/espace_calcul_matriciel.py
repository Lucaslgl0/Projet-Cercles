import numpy as np
from numpy.linalg import eig

###espace uniquement utile pour les différents caluculs que nous devons faire avec les matrices 

A = np.array([[-1, 2, 2, 2], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
B = np.array([[1, 0, 0, 0], [2, -1, 2, 2], [0, 0, 1, 0], [0, 0, 0, 1]])
C = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [2, 2, -1, 2], [0, 0, 0, 1]])
D = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [2, 2, 2, -1]])
liste=[A,B,C,D]
valeur =[]
"""for a in liste:
    for b in liste:
        for c in liste:
            for d in liste:
                for e in liste:
                    for f in liste:
                        for g in liste:
                            for h in liste:
                                valeur.append(eig(np.matmul( np.matmul( np.matmul(a,b),np.matmul(c,d)),np.matmul( np.matmul(e,f),np.matmul(g,h))))[0])
                                if max(eig(np.matmul( np.matmul( np.matmul(a,b),np.matmul(c,d)),np.matmul( np.matmul(e,f),np.matmul(g,h))))[0])==(4866.841754047718+0j):
                                    print(a,"a")
                                    print(b,"b")
                                    print(c,"c")
                                    print(d,'d')
                                    print(e)
                                    print(f)
                                    print(g)
                                    print(h)"""
maxi=0
for a in liste:
    for b in liste:
        for c in liste:
            for d in liste:
            
                valeur.append(eig( np.matmul( np.matmul(a,b),np.matmul(c,d)))[0])
                if max(eig( np.matmul( np.matmul(a,b),np.matmul(c,d)))[0])>69:
                    print(a)
                    print(b)
                    print(c)
                    print(d)
                    print(max(eig( np.matmul( np.matmul(a,b),np.matmul(c,d)))[0]))
compteur=0                               
for element in valeur:
    if max(element)>69:
        compteur+=1

        maxi=max(element)
print(maxi,compteur)