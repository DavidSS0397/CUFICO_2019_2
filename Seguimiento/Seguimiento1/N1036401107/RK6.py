import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Runge-Kutta 6                                                                                                                                 

x, y = np.loadtxt("datos.txt", usecols = (0,1), unpack = True)  #Cargo los datos del archivo que salió del programa en c++

def ODE(y,x):  #Defino la ecuación diferencial
    return x-y

def Exacta(x):    #Defino la solución exacta de la ecuación
    return x-1+2*np.exp(-x)

NumPuntos = np.array([10,100,1000,10000])
x0 = 0.
xf = 5.
y0 = 1.0
h = (xf-x0)/NumPuntos

TotalXS = []
TotalYS = []
TotalExacta = []
Totaldiffexacta = []
Totaldiffodeint = []

for j in NumPuntos:

    xs = np.linspace(x0,xf,j)   # Espacio muestral
    ys = odeint(ODE,y0,xs)      #Resuelvo la integral de la ecuacion por el método de odeint
    ys = np.array(ys).flatten()

    y_exacta = Exacta(xs)

    TotalExacta.append(y_exacta)
    TotalXS.append(xs)
    TotalYS.append(ys)
    
# Grafica

fig = plt.figure(figsize=(12,4))
ax0 = fig.add_subplot(131)
ax1 = fig.add_subplot(132)
ax2 = fig.add_subplot(133)

ax0.plot(TotalXS[3],TotalYS[3], "k",label='Odeint')
ax1.plot(TotalXS[3],TotalExacta[3],"r", label='Exacta')
ax2.plot(x,y,"b", label = 'RK6')  # Los elementos del archivo de texto que generó c++ estan organizados para graficar

plt.show()
