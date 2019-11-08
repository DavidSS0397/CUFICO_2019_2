#!/usr/bin/env python
# coding: utf-8

# In[164]:


import numpy as np 
from random import random
import matplotlib.pyplot as plt


# In[165]:


#INtervalo angular
a=-np.pi
b=np.pi


# In[168]:


#Definicion de la funcion de Distribucion
def P(phi):
    p=(1/(0.1*np.sqrt(2*np.pi)))*np.exp(-(phi)**2/2*(0.1)**2)
    return p


# In[188]:


#Plot funcion de distribucion
X=np.linspace(-50,50,1000)
plt.plot(X,P(X))


# In[175]:


#Funcion Delta de S
def DeltaS(P,phi_p,phi_0):
    DS=-np.log(P(phi_p)/P(phi_0))
    return DS


# In[180]:


#Reglas para la eleccion del Phi(Estado)
S=[]
for i in range (1000):
    phi_p=(b-a)*random()+a
    phi_0=(b-a)*random()+a
    if DeltaS(P,phi_p,phi_0)<0:
        phi=phi_p
        S.append(phi)
    else:
        x=random()
        p=(phi_p)/(phi_0)
        if x < p:
            phi=phi_p
            S.append(phi)
        else:
            pass
    phi_0=phi_p

#S=np.array(S)
        


# In[181]:


H=np.histogram(S)


# In[182]:


X=np.linspace(0,len(H),len(H))


# In[183]:


plt.bar(H[1][:10],H[0],width=0.5)


# In[192]:


#Prueba con otra funcion de Distribucion x**2
def P2(phi):
    p=phi**2
    return p
X=np.linspace(-50,50,1000)
plt.plot(X,P2(X))
plt.show()
S=[]
for i in range (1000):
    phi_p=(b-a)*random()+a
    phi_0=(b-a)*random()+a
    if DeltaS(P2,phi_p,phi_0)<0:
        phi=phi_p
        S.append(phi)
    else:
        x=random()
        p=(phi_p)/(phi_0)
        if x < p:
            phi=phi_p
            S.append(phi)
        else:
            pass
    phi_0=phi_p
H=np.histogram(S)
X=np.linspace(0,len(H),len(H))
plt.bar(H[1][:10],H[0],width=0.5)


# In[ ]:




