import numpy as np
import matplotlib.pyplot as plt
from Exercice1 import *

#xi : float[]
xi = [6,2,3,4,5,6,7,8,2]
#yi : float[]
yi = [8,12,9,6,15,10,12,7,13]

###Question 1

#k : int
k=2

#m : int : 9 points donc m=8
m=len(xi)-1

#ajout des k-1 points Pm+1,...,Pm+k-1 = Pm pour interpoler Pm
xi = xi+(k-1)*[xi[m]]
yi = yi+(k-1)*[yi[m]]

#ajout des k-1 points P-k+1,...,P-1 = P0 pour interpoler P0
xi = (k-1)*[xi[0]]+xi
yi = (k-1)*[yi[0]]+yi

#u : float[] : vecteur noeud
u=[ i for i in range(-k,(m+k+1)+1)]

#Qx : float[] :
Qx = []
#Qy : float[] :
Qy = []

#pour la question 3
#indice : int
indice = k #on commence a l'indice k

#couleur : int
couleur = 0

#i : float
for i in np.arange(0, m+1, 0.1):
	Qy.append(bcurve(i,u,k,yi))
	Qx.append(bcurve(i,u,k,xi))
	
	#pour la question 3
	if i>=u[indice] and i<=u[indice+1]:
		if couleur==0:
			plt.plot(Qx,Qy,color="red")
		else:
			plt.plot(Qx,Qy,color="orange")
		Qx=[]
		Qy=[]
		indice+=1
		couleur=(couleur+1)%2 #couleur = 0 ou 1

#on affiche le resultat
plt.plot(xi,yi)
plt.plot(Qx,Qy)
plt.show()


###Question 2

#on modifie juste un point
#yi2 : float[]
yi2 = [8,8,12,9,6,15,8,12,7,13,13]

#on vide les listes 
Qy=[]
Qx=[]

#pour la question 3
#indice : int
indice = k #on commence a l'indice k

#couleur : int
couleur = 0

#i : float
for i in np.arange(0, m+1, 0.1):
	Qy.append(bcurve(i,u,k,yi2))
	Qx.append(bcurve(i,u,k,xi))
	
	#pour la question 3
	if i>=u[indice] and i<=u[indice+1]:
		if couleur==0:
			plt.plot(Qx,Qy,color="red")
		else:
			plt.plot(Qx,Qy,color="orange")
		Qx=[]
		Qy=[]
		indice+=1
		couleur=(couleur+1)%2 #couleur = 0 ou 1

#on affiche le resultat
plt.plot(xi,yi2)
plt.plot(Qx,Qy)
plt.show()
