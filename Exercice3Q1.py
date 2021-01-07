import numpy as np
import matplotlib.pyplot as plt
from Exercice1 import *

###Question 1

#on definit la foncion pour faciliter les ecritures
def f(x):
	"float -> float"
	return (1/(1+25*x*x))
	
#xi : float[]
xi = np.arange(-1, 1.01, 0.01)

#yi : float[]
yi = [ f(x) for x in xi ]

#on ajoute la fonction en vert
plt.plot(xi,yi, color="green")

#calcul des points Pi
#Px : float[]
Px=[]
#Py : float[]
Py=[]

#on ajoute les differents points dans les tableaux
#i : int
for i in range(11):
	Px.append(-1 + (i/5))
	Py.append(f(-1 + (i/5)))
	
#on ajoute les points noirs 
plt.scatter(Px,Py,color="black")

#interpolation par un polynome de Lagrange
def interLag(yi,xi,x):
	"""float[]*float[]*float -> float"""
	#res : float
	res=0
	
	#i : int
	for i in range(len(yi)):
		
		#calcul du produit l
		#l : float
		l=1
		#j : int
		for j in range(len(xi)):
			if (j!=i):
				l*=((x-xi[j])/(xi[i]-xi[j]))
		
		#on augmente la somme
		res+=(yi[i]*l)
	
	return res

#L : float[]
L = [interLag(Py,Px,x) for x in xi]
#on ajoute l'interpolation par un polynome de Lagrage au graphe
plt.plot(xi,L, color="blue")


#interpolation par une spline cubique
#k : int
k=3

#on rajoute les 2 points artificiels
#Qx : float[]
Qx=[Px[0]]+Px+[Px[len(Px)-1]]
#Qy : float[]
Qy=[Py[0]]+Py+[Py[len(Py)-1]]

#m : int
m=len(Qx)-1

#creation de la matrice Qmat
#Qmat : float[]
Qmat = np.array([Qx,Qy])


#u : float[]
u=[ i for i in range(-k,(m+k+1)+1)]

#creation de la matrice Bmat
#Bmat : float[]
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
	
Px=Pmat[0]
Py=Pmat[1]
Qx=[]
Qy=[]

#i : float
for i in np.arange(0, m-k+1.1, 0.1):
	Qy.append(bcurve(i,u,k,Py))
	Qx.append(bcurve(i,u,k,Px))

plt.plot(Qx,Qy,color="orange")

#on affiche le graphe
plt.show()

