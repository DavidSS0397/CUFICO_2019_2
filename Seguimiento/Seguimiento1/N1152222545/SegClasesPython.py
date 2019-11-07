# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:30:36 2019

@author: Samuel

"""
import numpy as np
import pylab as plt
import time
from mpl_toolkits.mplot3d import Axes3D





class Particle:
    #Atributos
    cargada =  True
    
    #Instancias (metodos)
    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az, m, carga,): #Funcion que se aplica sobre la classe misma (self)
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.AX=ax
        self.AY=ay
        self.AZ=az
        self.M = m
        self.Carga = carga
    
    def Cinematica(f,teta,phi): #para una fuerza constante a phi del eje z y teta del eje x 
        h=0.01
        n=1000
        for j in range(n):
            
            ax=np.cos(teta)*np.sin(phi)*f/self.M
            ay=np.sin(teta)*np.sin(phi)*f/self.M
            az=np.cos(phi)*f/self.M 
            self.vx=self.vx + ax*h
            self.vy=self.vy + ay*h
            self.vz=self.vz + az*h 
            self.x=self.x +h*self.vx+(0.5*(h**2*f))
            self.x=self.y +h*self.vy+(0.5*(h**2*f))
            self.x=self.z +h*self.vz+(0.5*(h**2*f))
        
        
n=10000 #ITERACIONES
h=0.01      
A=Particle(0,0,0,0,0,0,0,0,0,10,7e-5) 
B=Particle(1,0,0,0,0,0,0,0,0,10,-4e-5)     
e0=8.85e-12
u0=np.pi*4e-7
H=10 
ax1=0
ay1=0  
az1=0
ax2=0
ay2=0
az2=0
x=[]
y=[]
z=[]
x1=[]
y1=[]
z1=[]

def Biot(v1,v2,v3,v4,v5,x1,x2,y1,y2,z1,z2):
    
    return (v1*(v2*(x1-x2)-v3*(y1-y2))-v4*(v5*(y1-y2)-v2*(z1-z2)))*u0*A.Carga*B.Carga/(4*np.pi*R**3)
    
for i in range(n):
    
    R=np.sqrt((A.X-B.X)**2+(A.Y-B.Y)**2+(A.Z-B.Z)**2)
            
    A.AX=A.Carga*B.Carga*(A.X-B.X)/(4*np.pi*e0*R**3)+A.Carga*A.VY*H+(A.VY*(B.VX*(A.Y-B.Y)-B.VY*(A.X-B.X))-A.VZ*(B.VZ*(A.X-B.X)-B.VX*(A.Z-B.Z)))*u0*A.Carga*B.Carga/(4*np.pi*R**3)
    A.AY=A.Carga*B.Carga*(A.Y-B.Y)/(4*np.pi*e0*R**3)+A.Carga*A.VX*H+Biot(A.VZ,B.VY,B.VZ,A.VY,B.VY,A.Z,B.Z,A.Y,B.Y,A.X,B.X)
    A.AZ=A.Carga*B.Carga*(A.Z-B.Z)/(4*np.pi*e0*R**3)+Biot(A.VX,B.VZ,B.VX,A.VY,B.VY,A.X,B.X,A.Z,B.Z,A.Y,B.Y)
    
    
    A.VX=A.VX + 0.5*(ax1+A.AX)*h
    A.VY=A.VY + 0.5*(ay1+A.AY)*h
    A.VZ=A.VZ + 0.5*(az1+A.AZ)*h 
          
    A.X=A.X +h*A.VX+(0.5*(h**2*A.AX))
    A.Y=A.Y +h*A.VY+(0.5*(h**2*A.AY))
    A.Z=A.Z +h*A.VZ+(0.5*(h**2*A.AZ))
    
    ax1=A.AX
    ay1=A.AY
    az1=A.AZ
        
    x.append(A.X)
    y.append(A.Y)
    z.append(A.Z)    
    
        
        
    B.AX=A.Carga*B.Carga*(B.X-A.X)/(4*np.pi*e0*R**3)+B.Carga*B.VY*H+Biot(B.VY,A.VX,A.VY,B.VZ,A.VZ,B.Y,A.Y,B.X,A.X,B.Z,A.Z)  
    B.AY=A.Carga*B.Carga*(B.Y-A.Y)/(4*np.pi*e0*R**3)+B.Carga*B.VX*H+Biot(B.VZ,A.VY,A.VZ,B.VX,A.VX,B.Z,A.Z,B.Y,A.Y,B.X,A.X)
    B.AZ=A.Carga*B.Carga*(B.Z-A.Z)/(4*np.pi*e0*R**3)+Biot(B.VX,A.VZ,A.VX,B.VY,A.VY,B.X,A.X,B.Z,A.Z,B.Y,A.Y)
    
    B.VX=B.VX + 0.5*(ax2+B.AX)*h
    B.VY=B.VY + 0.5*(ay2+B.AY)*h
    B.VZ=B.VZ + 0.5*(az2+B.AZ)*h 
    
    B.X=B.X +h*B.VX+(0.5*(h**2*B.AX))
    B.Y=B.Y +h*B.VY+(0.5*(h**2*B.AY))
    B.Z=B.Z +h*B.VZ+(0.5*(h**2*B.AZ))
    
    ax2=B.AX
    ay2=B.AY
    az2=B.AZ
    
    x1.append(B.X)
    y1.append(B.Y)
    z1.append(B.Z)
    
   
fig=plt.figure()
ax=fig.gca(projection='3d')    
ax.plot(x,y,z, label='particula 1') #
plt.ylabel('eje y')
plt.xlabel('eje x')
ax.plot(x1,y1,z1, label='particula 2')
ax.set_zlabel('eje z')
ax.legend()
plt.show()
