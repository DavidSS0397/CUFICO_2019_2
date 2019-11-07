"""
! ===========================================================================
! RK6.py
! ===========================================================================
! Este programa grafica la solucion a la ecuacion diferencial y'=x-y que ha 
! ha sido solucionada en C++ usando el metodo de RK6. Ademas compara para 
! diferente numero de puntos.
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co

! Up to date: 19 septiembre 2019			
"""
import numpy as np
import matplotlib.pyplot as plt

#Función con la solución exacta a la ODE
def ExactSolution(x):
    return x-1+2*np.exp(-x)

#Lectura de datos del calculo de RK6 desde C++
x,y = np.loadtxt('dat.txt',unpack = True, delimiter = ',')


NumPuntos = np.array([10,100,1000,10000]) #Numeros de puntos
x0 = 0 #Posicion inicial
xf = 5 #Posicion final
h = (xf-x0)/NumPuntos #Pasos para diferentes numeros de puntos
colors = ['r','b','g','m','k']

#Soluciones para diferentes numeros de puntos en RK6
pos = np.where(x==0)
X = []
Y = []
YExacta = []
yRK6_difference = []

for i in range(0,4,1):
	if i+1==4:
		X.append(x[pos[0][i]:])
		Y.append(y[pos[0][i]:])
	else :
		X.append(x[pos[0][i]:pos[0][i+1]])
		Y.append(y[pos[0][i]:pos[0][i+1]])
	YExacta.append(ExactSolution(X[-1])) #Solucion Exacta 
	yRK6_difference.append(np.mean(np.abs(Y[-1]-YExacta[-1]))) #Calculo de la dovergencia

#Graficas
plt.figure(figsize=(21,7))

plt.subplot(131)
for i in range(0,4,1):
	plt.plot(X[i],Y[i], colors[i],label='%d puntos'%NumPuntos[i])
plt.plot(X[-1],YExacta[-1],'k--',label = 'Solucion exacta')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solucion con RK6 para diferentes numeros de puntos')
plt.legend()
plt.grid()

plt.subplot(132)
for i in range(0,4,1):
	plt.semilogy(X[i],np.abs(Y[i]-YExacta[i]), colors[i],label='%d puntos'%NumPuntos[i])
plt.title('Error')
plt.xlabel('x')
plt.legend()
plt.grid()

plt.subplot(133)
plt.plot(h,yRK6_difference,'orange')
plt.title('Divergencia RK6')
plt.xlabel('h[Paso]')
plt.grid()

plt.show()