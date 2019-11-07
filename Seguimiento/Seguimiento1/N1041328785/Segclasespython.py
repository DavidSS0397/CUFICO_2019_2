#!/bin/python

#se hara una simulacion de la cinematica de que corresponde a dos particulas
#cargadas inmersas en un campo magnetico

import numpy as np 
import FUNCIONES as FUN

import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d

#se definen las funciones y variables globales que usaranen la simulacion.

#Variables globales
K=1.0
B=(0,0,10)
i=0
dt=0.01

#Se definen dos particulas con sus condiciones iniciales

particula_1=FUN.Particle(0., 0., 0., 0., 0., 0., 10, 10)
particula_2=FUN.Particle(1., 0., 0., 0., 0., 0., 10, -10)

########################################################################################################################################################

#Ahora almacenamos la informacion de nuestras particulas

posicion_P1 = [[particula_1.X], [particula_1.Y], [particula_1.Z]]
posicion_P2 = [[particula_2.X], [particula_2.Y], [particula_2.Z]]

while(i<=10000):

    particula_1.Cambio_tmp(*FUN.lorenzt(particula_1, particula_2, dt))

    posicion_P1[0].append(particula_1.X)
    posicion_P1[1].append(particula_1.Y)
    posicion_P1[2].append(particula_1.Z)

    par_img = FUN.Particle(*particula_1.Estado_anterior) 
    
    particula_2.Cambio_tmp(*FUN.lorenzt(particula_2, par_img, dt))
    
    posicion_P2[0].append(particula_2.X)
    posicion_P2[1].append(particula_2.Y)
    posicion_P2[2].append(particula_2.Z)
    
    i = i+1

#######################################################################################################################################################

##grafica de la trayectoria

fig=plt.figure()
ax=plt.axes(projection='3d')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.title("Trayectoria de dos particulas\n con carga Q1 =%.1f y Q2 = %.1f"%(particula_1.Carga, particula_2.Carga))

ax.plot3D(posicion_P1[0], posicion_P1[1], posicion_P1[2], label ="Trayectoria de la particula_1")
ax.plot3D(posicion_P2[0], posicion_P2[1], posicion_P2[2], label ="Trayectoria de la particula_2")
plt.legend(loc="lower left")
ax.scatter(0., 0., 0., color= "b")
ax.scatter(1., 0., 0., color= "red")

plt.show()
