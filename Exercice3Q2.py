import numpy as np
import matplotlib.pyplot as plt
from Exercice1 import *

### Question 2

#ptsX : float[]
ptsX=[10,12,14,11,7,10,16,10,4,11,18]

#ptsY : float[]
ptsY=[10,8,10,14,10,6,8,16,8,3,4]

plt.scatter(ptsX,ptsY,color="blue")

#k : int
k=3

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
for i in np.arange(0, m-k+1.1, 0.1):
	Qy.append(bcurve(i,u,k,ptsY))
	Qx.append(bcurve(i,u,k,ptsX))

plt.plot(Qx,Qy,color="blue")
plt.show()





















