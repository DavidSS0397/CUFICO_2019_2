#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

########solucion analitica#########################
def exact_solution(xe):
	return x-1+2*np.exp(-xe)

##########lectura de datos############################ 
x,y = np.loadtxt('RKtt6.txt', unpack=True)
ye=exact_solution(x)

##########Errores#####################################
Error=(np.abs(y-ye))/ye
print (Error)
#########graficas solucion exacta vs RK6################
plt.figure()
plt.semilogy(x,Error)
plt.title("Error relativo")
plt.xlabel('x')
plt.ylabel('y')

plt.figure()
plt.plot(x,y, label='Solucion RKtt6', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solucion exacta y RKtt6')
plt.plot(x,ye, label= 'Solucion exacta', color='blue')
plt.legend()
plt.grid()
plt.show()
