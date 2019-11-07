#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style


# In[34]:


class Particulas:
    cargada1=True
    cargada2=True
    
    def __init__(self, x1, y1, z1, vx1, vy1, vz1, m1, carga1, x2, y2, z2, vx2, vy2, vz2, m2, carga2):
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
    
    def movimiento(self):
        k=8.98*10**9
        Bz=10
        X1=[]
        Y1=[]
        Z1=[]
        X2=[]
        Y2=[]
        Z2=[]
        t=np.linspace(0,100,10000)
        t=list(t)
        t0=0
        j=0
        while j < 10000:
            #Componentes del campo electrico
            E1x=k*self.carga2*(self.x1-self.x2)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E1y=k*self.carga2*(self.y1-self.y2)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E1z=k*self.carga2*(self.z1-self.z2)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E2x=k*self.carga1*(self.x2-self.x1)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E2y=k*self.carga1*(self.y2-self.y1)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            E2z=k*self.carga1*(self.z2-self.z1)/((((self.x1-self.x2)**2+(self.y1-self.y2)**2+(self.z1-self.z2)**2))**(3/2))
            
            #Fuerza de lorentz
            Fx1=self.carga1*(E1x+self.vy1*Bz)
            Fy1=self.carga1*(E1y-self.vx1*Bz)
            Fz1=self.carga1*E1z
            Fx2=self.carga2*(E2x+self.vy2*Bz)
            Fy2=self.carga2*(E2y-self.vx2*Bz)
            Fz2=self.carga2*E2z
            
            #Posiciones
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
            
            #Velocidades
            self.vx1=(Fx1/self.m1)*(t[j]-t0)+self.vx1
            self.vy1=(Fy1/self.m1)*(t[j]-t0)+self.vy1
            self.vz1=(Fz1/self.m1)*(t[j]-t0)+self.vz1
            self.vx2=(Fx2/self.m2)*(t[j]-t0)+self.vx2
            self.vy2=(Fy2/self.m2)*(t[j]-t0)+self.vy2
            self.vz2=(Fz2/self.m2)*(t[j]-t0)+self.vz2
            t0=t[j]
            j=j+1
        return X1, Y1, Z1, X2, Y2, Z2


# In[35]:


#help(Particulas)
particula=Particulas(0,0,0,0,0,0,5,1,1,0,0,0,0,0,5,-1)


# In[36]:


resultado=particula.movimiento()


# In[ ]:





# In[37]:


# Creamos la figura
fig = plt.figure()
# Creamos el plano 3D
ax1 = fig.add_subplot(111, projection='3d')

# Agregamos los puntos en el plano 3D
ax1.scatter(x1, y1, z1, c='b', marker='o')
ax1.scatter(x2, y2, z2, c='y', marker='o')

# Mostramos el gráfico
plt.show()


# In[ ]:




