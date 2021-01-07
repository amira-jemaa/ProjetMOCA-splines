import numpy as np
import matplotlib.pyplot as plt
from Exercice1 import *

### Question 1

#ptsX : float[]
ptsX=[2,4,8,10,14,16,16,12,6,4]

#ptsY : float[]
ptsY=[5,2.5,2.5,7.5,10,12.5,17.5,20,17.5,10]


#creation de la figure par interpolation
plt.scatter(ptsX,ptsY,color="blue")

#k : int
k=3

#ajout des k points 
#i : int
for i in range(k):
	ptsX.append(ptsX[i])
	ptsY.append(ptsY[i])


#on rajoute les 2 points artificiels
#Qx : float[]
Qx=[ptsX[0]]+ptsX+[ptsX[len(ptsX)-1]]
#Qy : float[]
Qy=[ptsY[0]]+ptsY+[ptsY[len(ptsY)-1]]

#m : int
m=len(Qx)-1

#creation de la matrice Qmat
#Qmat : float[][]
Qmat = np.array([Qx,Qy])


#u : float[]
u=[ i for i in range(-k,(m+k+1)+1)]

#creation de la matrice Bmat
#Bmat : float[][]
Bmat=[]

#i : int
for i in range(2,m+2+1):
	#Btmp : float[]
	Btmp=[]
	#j : int
	for j in range(m+1):
		Btmp.append(B(u[i],j,k,u))
	Bmat.append(Btmp)
Bmat=np.array(Bmat)

#creation de la matrice Pmat
Pmat = np.linalg.inv(Bmat).dot(Qmat.transpose()).transpose()
	
ptsX=Pmat[0]
ptsY=Pmat[1]
Qx=[]
Qy=[]

#i : float
for i in np.arange(0, m-k-1+.1, 0.1):
	Qy.append(bcurve(i,u,k,ptsY))
	Qx.append(bcurve(i,u,k,ptsX))

plt.plot(Qx,Qy,color="blue")



###Calcul de la surface
#sur : float
sur = 0

#on cherche les points d'abscisse maximale et minimale de Qx

#indiceMax : int
indiceMax = 0

#indiceMin : int
indiceMin = 0

#i : int
for i in range(len(Qx)):
	if Qx[i] < Qx[indiceMin]:
		indiceMin=i
	if Qx[i] > Qx[indiceMax]:
		indiceMax=i
	
#on trace la droite entr le point d'abscisse minimale et celui d'abscisse maximale de Q
def f(x):
	"""
	float->float
	renvoie l'abscisse du point x dans la droite egendree par les points d'abscisse maxial et minimal de Q
	"""
	#a : float
	a = (Qy[indiceMax]-Qy[indiceMin])/(Qx[indiceMax]-Qx[indiceMin])
	#b : float
	b = Qy[indiceMin] - a*Qx[indiceMin]
	return a*x+b
	
#dx : float[]
dx = np.arange(0,18,0.1)
#dy : float[]
dy = [f(x) for x in dx]
plt.plot(dx,dy,color="black")

#on additionne la somme des ordonnees des points se trouvant au dessus de cette droite et on sustrait le ordonnees des points en dessous de cette droite
#i : int
for i in range(len(Qx)):
	#si le point est en dessous de la droite
	if Qy[i] < f(Qx[i]):
		sur -= Qy[i]
	#si le point est au dessus de la droite
	else:
		sur += Qy[i]
		
print("La surface est de",sur,"km carre")
plt.show()
