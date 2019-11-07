#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Brayan Alexander Muñoz Barrera
Clase 5 Jueves 22 de Agosto 2019. 
Python y programación orientada a objetos.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.constants import epsilon_0, pi

class Particle:
    #Atributos
    cargada =  True
    
    #Instancias (metodos)
    def __init__(self, posicion , velocidad , m, carga): #Funcion que se aplica sobre la classe misma (self)
        
        self.POS=np.array(posicion)     #La posición es un vector
        self.VEL = np.array(velocidad)  #La velocidad es un vector
        self.M = m                      #Masa
        self.Carga = carga              #Carga
        self.trayectoriax = []          #Aquí guardaré la trayectoria x
        self.trayectoriay = []          #La y y la z
        self.trayectoriaz = []
        
    def Interaccion(paso1):              #Todo lo que respecta a la interacción entre las dos particulas
        B = np.array([0.,0.,10.])       #El campo magnetico en sus componentes
        
        #El campo electrico es E= -nabla(fhi) donde fhi es el potencial. 
        #El potencial fhi = q/4*pi*epsilon_0  1/|r2-r1| funciona bien para el problema
        #donde |r2-r1|=root((x2-x1)**2+(y2-y1)**2 +(z2-z1)**2), que en coordenadas cartesianas queda como pongo a continuación:
        
        #Para la particula 1:
        x1=(p1.POS[0]-p2.POS[0]);y1=(p1.POS[1]-p2.POS[1]);z1=(p1.POS[2]-p2.POS[2]); r1=(((x1**2) - (y1**2) - (z1**2))) #Simplemente defino estas variables para reducir la ecuación del campo electrico
        E1 = np.array([(E_0*p2.Carga*x1)/((r1)**(3/2)),(E_0*p2.Carga*y1)/((r1)**(3/2)),(E_0*p2.Carga*z1)/((r1)**(3/2))])#Campo electrico en sus componentes x,y,z
        #Para la particula 2:
        x2=(p2.POS[0]-p1.POS[0]);y2=(p2.POS[1]-p1.POS[1]);z2=(p2.POS[2]-p1.POS[2]); r2=(((x2**2) - (y2**2) - (z2**2)))
        E2 = np.array([(E_0*p1.Carga*x2)/((r2)**(3/2)),(E_0*p1.Carga*y2)/((r2)**(3/2)),(E_0*p1.Carga*z2)/((r2)**(3/2))])
        
        #Fuerza de Lorentz: F= q(E + VxB):
        f1 = p1.Carga*E1 + p1.Carga*np.cross(p1.VEL,B)
        f2 = p2.Carga*E2 + p2.Carga*np.cross(p2.VEL,B)
        
        #Metodo iterativo de Euler, paso a paso
        acc1 = f1/p1.M        # fuerza = masa*aceleracion => aceleracion = masa/fuerza
        p1.VEL += (acc1*paso1) #La velocidad un t+1 diminuto será así
        p1.POS += p1.VEL*paso1
        p1.trayectoriax.append(p1.POS[0]) #Vamos añadiendo la posición a la trayectoria en cada una de sus componentes para después graficar
        p1.trayectoriay.append(p1.POS[1])
        p1.trayectoriaz.append(p1.POS[2])
       
        #Lo mismo pero para la particula 2
        acc2 = f2/p2.M
        p2.VEL += acc2 * paso1
        p2.POS += p2.VEL*paso1
        p2.trayectoriax.append(p2.POS[0])
        p2.trayectoriay.append(p2.POS[1])
        p2.trayectoriaz.append(p2.POS[2])
        
p1 = Particle([0.1e-20,0.1e-20,0.1e-20],[0.,0.,0.],10.,1.)#Llamamos la clase particula y le definimos las propiedades de particula 1
p2 = Particle([1.,0.1e-20,0.],[0.,0.,0.],10.,-1.)#Particula 2
paso=0.01
paso1=0.00001
E_0= (1.)/(4*pi*epsilon_0)#Constante del potencial
    
for t in np.arange(0,100,paso):#Llamamos la interaccion 10000 veces
    Particle.Interaccion(paso)#Se van añadiendo las trayectorias

#Grafico:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(p1.trayectoriax, p1.trayectoriay,p1.trayectoriaz, label='Particula q+')
ax.plot(p2.trayectoriax,p2.trayectoriay,p2.trayectoriaz, label='Particula q-')

ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

#Gracias.