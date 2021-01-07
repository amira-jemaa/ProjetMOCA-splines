import numpy as np
import matplotlib.pyplot as plt

###Question 1

def B(x,i,k,u):
	#si k est d'ordre 0
	if k==0 :
        #x n'est pas dans l'intervalle
		if ( (x<u[i]) or (x>=u[i+1]) ):
			return 0.0
        #retourne 1 si x est dans l'intervalle ui <=x< ui+1 (d'apres la definition de b spline)
		return 1.0
	#pour k est d'ordre k
	#par convention x/0 = 0
	if (u[i+k] == u[i]) :
		#c1 : float: coefficient spline
		c1 = 0.0
	else :
		#c1 : float (d'apres la definition
		c1 = (x-u[i])/(u[i+k]-u[i])*B(x,i,k-1,u)
		
	#convention x/0 = 0
	if (u[i+k+1] == u[i+1]) :
		#c2 : float
		c2 = 0.0
	else :
		#c2 : float
		c2 = (u[i+k+1]-x)/(u[i+k+1]-u[i+1])*B(x,i+1,k-1,u)
	
	return c1 + c2
	

def bcurve(x,u,k,c):
	 
	#test des cas d'erreur
	if ( (x<u[0]) or (x>u[len(u)-1]) ): #si n'appartient pas a l'intervalle qu'on a donner
		print("Erreur bcurve: x en dehors des bornes")
		return 0.0
		 
	#res : float
	res=0.0
	
	#n : int
	n=len(c)-1
	
	#i : int
	for i in range(n+1):
		#on augmente le resultat
		res+=c[i]*B(x,i,k,u)
	
	#on retourne le resultat
	return res

###Question 2	
#creation des BSplines
def traceBSplines(inf, sup, u, k):
	"""int*int*float[]*int -> void"""
	#tabX : float[]
	tabX = np.arange(inf, sup, 0.1)
	
	#i : int
	#pour chaque B-splines
	for i in range(sup+1):
		#on cree le tableau des f(x)
		#tabY : float[]
		tabY = [ B(x,i,k,u) for x in tabX ]
		
		#on ajoute le graphe a l'image finale
		plt.plot(tabX, tabY)
	
	#on affiche toutes les B-splines
	plt.show()
	
#creation de la courbe bcurve
def traceBCurve(inf, sup, u, k, c):
	"""int*int*float[]*int*float[] -> void"""
	#tabX : float[]
	tabX = np.arange(inf, sup, 0.1)
	
	#i : int
	#pour chaque B-splines
	for i in range(sup+1):
		#on cree le tableau des f(x)
		#tabY : float[]
		tabY = [ B(x,i,k,u) for x in tabX ]
		
		#on ajoute le graphe a l'image finale
		plt.plot(tabX, tabY)
		
	#on cree le tableau des f(x)
	#tabY : float[]
	tabY = [ bcurve(x,u,k,c) for x in tabX ]
		
	#on ajoute le graphe a l'image finale
	plt.plot(tabX, tabY)
	
	#on affiche le graphe
	plt.show()


u=[0,0,0,0,1,2,3,4,5,5,5,5]
c1=[-1/2, 1/2, -1/2, 1, -1/2, 1]
#traceBSplines(0, 5, u, 3)
#traceBCurve(0, 5, u, 3, c1)

	
###Question 3
def I(x,i,k,u):
	 
	#on cherche j
	#j : int
	j=-1
    #si j n'est pas dans l'intervalle [uj,uj+1[
	while (j<len(u)-1 and x>=u[j+1]):
		j+=1
	if (j>=len(u)):
		print("Erreur j n'existe pas")
		return -1
	if (x<u[j]):
		print("Erreur j n'existe pas")
		return -1
	
	#on test les differents cas sur j a partir de la definition
	if (j<i+1):
		return 0
		
	if (j>i+k):
		return 1
		
	#res : float
	res=0
	
	#a : int
	for a in range(i+1, j+1):
		res+=B(x, a, k, u)
	
	return res

def icurve(x,u,k,c):
	"""float*float[]*int*float[] -> float"""
	#test des cas d'erreur
    # on test si x est dans l'intervalle d'apres la definition
	if ( (x<u[0]) or (x>u[len(u)-1]) ):
		print("Erreur icurve: x en dehors des bornes")
		return 0
		 
	#res : float
	res=0
	
	#n : int : avec c coefficient des spline
	n=len(c)
	
	#i : int
	for i in range(n):
		#on augmente le resultat
		res+=c[i]*I(x,i,k,u)
	
	#on retourne le resultat
	return res
	
###Question 4	
#creation des ISplines
def traceISplines(inf, sup, u, k):
	"""int*int*float[]*int -> void"""
	#tabX : float[]
	tabX = np.arange(inf, sup, 0.1)
	
	#i : int
	#pour chaque I-splines
	for i in range(sup+1):
		#on cree le tableau des f(x)
		#tabY : float[]
		tabY = [ I(x,i,k,u) for x in tabX ]
		
		#on ajoute le graphe a l'image finale
		plt.plot(tabX, tabY)
	
	#on affiche toutes les B-splines
	plt.show()
	
#creation de la courbe icurve
def traceICurve(inf, sup, u, k, c):
	"""int*int*float[]*int*float[] -> void"""
	#tabX : float[]
	tabX = np.arange(inf, sup, 0.1)
	
	#i : int
	#pour chaque I-splines
	for i in range(sup+1):
		#on cree le tableau des f(x)
		#tabY : float[]
		tabY = [ I(x,i,k,u) for x in tabX ]
		
		#on ajoute le graphe a l'image finale
		plt.plot(tabX, tabY)
		
	#on cree le tableau des f(x)
	#tabY : float[]
	tabY = [ icurve(x,u,k,c) for x in tabX ]
		
	#on ajoute le graphe a l'image finale
	plt.plot(tabX, tabY)
	
	#on affiche le graphe
	plt.show()

c2=[0.4,0.1,0,0.1,0.4]
traceISplines(0, 5, u, 3)
traceICurve(0, 5, u, 3, c2)

