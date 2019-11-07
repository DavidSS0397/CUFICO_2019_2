#!/etc/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #for making arrays out of csv files

'''
def MyFirstODE(y,x): #The differential equation
    return x-y
'''


def ExactSolution(x): #The exact solution
    return x-1+2*np.exp(-x)


values = pd.read_csv("rk6.csv", sep = ",", header = None) #gets the values out of the file.

xVal, rK6Sol = values[0], values[1] 

exactSol = ExactSolution(xVal)

diffRK6 = np.abs(rK6Sol-exactSol)


fig = plt.figure(figsize = (12,4)) #Makes the "Canvas" for the graphing


ax0 = fig.add_subplot(131)#Makes the first subgraph
ax1 = fig.add_subplot(132)#Makes the second subgraph
ax2 = fig.add_subplot(133)#Makes the third subgraph


ax0.plot(xVal,rK6Sol, 'b--', label ="RungeKutta6")
ax0.plot(xVal, exactSol, 'k', label = "Exact")
ax0.legend()

ax1.semilogy(xVal,diffRK6, 'b--')#Graphs the difference of the RK6 method and the exact solution

#ax2.plot(xVal, np.mean(diffRK6))#CORREGIR; PRIMERO DEBE DE SER EL NUMERO DE PASOS


plt.show()
