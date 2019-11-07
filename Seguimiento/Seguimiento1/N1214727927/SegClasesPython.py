#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style


# In[86]:


class Particulas:
    '''descripcion de las particulas cargadas'''
    cargada1=True
    cargada2=True
    
    def __init__(self, x1, y1, z1, vx1, vy1, vz1, m1, carga1, x2, y2, z2, vx2, vy2, vz2, m2, carga2): #entran como argumentos
        #posicion inicial, velocidad inicial, y cargas de particulas 1 y 2
        self.x1=x1
        self.y1=y1
        self.z1=z1
        self.vx1=vx1
        self.vy1=vy1
        self.vz1=vz1
        self.m1=m1
        self.carga1=carga1
        self.x2=x2
        self.y2=y2
        self.z2=z2
        self.vx2=vx2
        self.vy2=vy2
        self.vz2=vz2
        self.m2=m2
        self.carga2=carga2
    
    def descripcion(self): #Me describe el movimiento de las particulas
        k=8.98*10**9 #constante de coulomb
        Bz=10 #campo magnetico en z
        X1=[] #listas para guardas valores de posicion
        Y1=[]
        Z1=[]
        X2=[]
        Y2=[]
        Z2=[]
        t=np.arange(0,100,0.01) #genero numeros entre 0 y 100 con saltos de 0.01
        t=list(t)
        t0=0
        for j in range(0,10000):
            #campo electrico particulas 1 y 2
            E1x=k*self.carga2*(self.x1-self.x2)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E1y=k*self.carga2*(self.y1-self.y2)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E1z=k*self.carga2*(self.z1-self.z2)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E2x=k*self.carga1*(self.x2-self.x1)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E2y=k*self.carga1*(self.y2-self.y1)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E2z=k*self.carga1*(self.z2-self.z1)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            
            #fuerza de lorentz particulas 1 y 2
            Fx1=self.carga1*(E1x+self.vy1*Bz)
            Fy1=self.carga1*(E1y-self.vx1*Bz)
            Fz1=self.carga1*E1z
            Fx2=self.carga2*(E2x+self.vy2*Bz)
            Fy2=self.carga2*(E2y-self.vx2*Bz)
            Fz2=self.carga2*E2z
            
            #posiciones particula 1 y 2
            self.x1=0.5*(Fx1/self.m1)*(t[j]-t0)**2+self.vx1*(t[j]-t0)+self.x1
            self.y1=0.5*(Fy1/self.m1)*(t[j]-t0)**2+self.vy1*(t[j]-t0)+self.y1
            self.z1=0.5*(Fz1/self.m1)*(t[j]-t0)**2+self.vz1*(t[j]-t0)+self.z1
            self.x2=0.5*(Fx2/self.m2)*(t[j]-t0)**2+self.vx2*(t[j]-t0)+self.x2
            self.y2=0.5*(Fy2/self.m2)*(t[j]-t0)**2+self.vy2*(t[j]-t0)+self.y2
            self.z2=0.5*(Fz2/self.m2)*(t[j]-t0)**2+self.vz2*(t[j]-t0)+self.z2
            X1.append(self.x1)
            Y1.append(self.y1)
            Z1.append(self.z1)           
            X2.append(self.x2)
            Y2.append(self.y2)
            Z2.append(self.z2)  
            
            #velocidades particula 1 y 2
            self.vx1=(Fx1/self.m1)*(t[j]-t0)+self.vx1
            self.vy1=(Fy1/self.m1)*(t[j]-t0)+self.vy1
            self.vz1=(Fz1/self.m1)*(t[j]-t0)+self.vz1
            self.vx2=(Fx2/self.m2)*(t[j]-t0)+self.vx2
            self.vy2=(Fy2/self.m2)*(t[j]-t0)+self.vy2
            self.vz2=(Fz2/self.m2)*(t[j]-t0)+self.vz2
            t0=t[j]
        return X1, Y1, Z1, X2, Y2, Z2


# In[87]:


#help(Particulas)
bo=Particulas(0,0,0,0,0,0,10,10,1,0,0,0,0,0,10,-10) #instancio mi clase


# In[88]:


resul=bo.descripcion() #aplico el metodo a mi objeto


# In[89]:
#Organizamos las matrices para graficar

x1=np.array(resul[0])
#print(x.shape)
x1=x1.reshape(1,10000)
x1=list(x1)
print("x1",x1)
y1=np.array(resul[1])
y1=y1.reshape(1,10000)
y1=list(y1)
print("y1",y1)
z1=np.array(resul[2])
z1=z1.reshape(1,10000)
z1=list(z1)
print("z1",z1)
x2=np.array(resul[3])
#print(x.shape)
x2=x2.reshape(1,10000)
x2=list(x2)
print("x2",x2)
y2=np.array(resul[4])
y2=y2.reshape(1,10000)
y2=list(y2)
print("y2",y2)
z2=np.array(resul[5])
z2=z2.reshape(1,10000)
z2=list(z2)
print("z2",z2)


# In[90]:


# Creamos la figura
fig = plt.figure()
# Creamos el plano 3D
ax1 = fig.add_subplot(111, projection='3d')

# Agregamos los puntos en el plano 3D
ax1.scatter(x1, y1, z1, c='g', marker='o')
ax1.scatter(x2, y2, z2, c='r', marker='o')

# Mostramos el gráfico
plt.show()

