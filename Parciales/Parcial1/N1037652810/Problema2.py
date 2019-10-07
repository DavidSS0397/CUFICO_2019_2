# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:21:40 2019

@author: ubuntu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#sistema acoplado de las poblaciones de dos gases
#para odeint
def DifEqu(sols,tn):
    #print(sols)    
    y=sols[0]
    x=sols[1]
    c=1.
    d=1.
    a=1.
    b=1.
    DifEq=[0]*(2)
    DifEq[0]=-y*(c-d*x) #n2
    DifEq[1]=x*(a-b*y) #n1
    return DifEq

#para rk4
def DifEque(tn,sols):
    #print(sols)    
    y=sols[0]
    x=sols[1]
    c=1.
    d=1.
    a=1.
    b=1.
    DifEq=[0]*(2)
    DifEq[0] = -y*(c-d*x) #n2
    DifEq[1] = x*(a-b*y) #n1
    return DifEq  
    
def Euler(tn, xn, yn, h): #metodo de euler para 2 ecuaciones acopladas
    sols=[yn,xn]
    Difeq=DifEqu(sols,tn)
    yn= yn+(h*Difeq[0])
    xn= xn+h*Difeq[1]
    return yn, xn

def RK4(t,h,y,n): # Runge-Kutta 4 de dimension n, parametro t,step h , vector y con las soluciones de x y y
    
    #listas de los valores de rk4 para cada ecuacion a solucionar     
    k1=[0.]*(n)
    k2=[0.]*(n)
    k3=[0.]*(n)
    k4=[0.]*(n)
    fR=[0.]*(n)
    ydumb=[0.]*(n)
    
    fR=DifEque(t, y) # se llama las ecuaciones diferenciales con los valores t e y                
    for i in range(0,n): 
       k1[i] = h*fR[i]                 
    for i in range(0, n):
        ydumb[i] = y[i] + k1[i]/2. 
    fR=DifEque(t + h/2.,ydumb)
    
    for i in range(0, n): #un for para cada ecuacion diferencial a resolver
        k2[i]=h*fR[i]
        ydumb[i] = y[i] + k2[i]/2.    
    fR=DifEque(t + h/2., ydumb) #se fijan los valores para calcular el siguiente k
    for i in range(0, n):
        k3[i]=h*fR[i]
        ydumb[i] = y[i] + k3[i] 
    fR=DifEque(t + h, ydumb)
    for i in range(0, n):
        k4[i]=h*fR[i]
    for i in range(0, n):
        y[i] = y[i] + (k1[i] + 2.*(k2[i] + k3[i]) + k4[i])/6. #el siguiente y de la solucion
    return y
    
#condiciones iniciales
NumPuntos=np.array([10,100,1000,10000])
t0=0.
tf=12.

x0=1.5 
y0=1.
h=(tf-t0)/NumPuntos #step
ini=[y0,x0]
Difeq=DifEqu(ini,0) #llama las ecuaciones diferenciales para las condiciones iniciales


Allstepst=[] #para los diferentes ts de cada numero de puntos

#Para n2

#cuanto difiere el metodo de la exacta
yE_difference = [] #para cada numerp de puntos
yRK_difference=[] #para cada numerp de puntos
TotalDiffEulerY = []
TotalEulerY = []
TotalRKY=[]
TotalDiffRKY=[]
TotalExactY=[]

#Para n1

xE_difference = []
xRK_difference=[]
#Odeint solution
TotalDiffEulerX = []
TotalEulerX = []
TotalRKX=[]
TotalDiffRKX=[]
TotalExactX=[]

#Para guardar las soluciones encontradas con cada numero de pasos en Numpuntos
AllstepsEulerX=[]
AllstepsRK4X=[]
AllstepsEulerY=[]
AllstepsRK4Y=[]

for j in NumPuntos: #para evaluar el metodo con cada uno de los valores en NumPuntos
    
    #Donde se iran guardando las soluciones de cada metodo para cada numero de puntos
    TotalEulerY = []
    TotalRKY=[]
    TotalEulerX = []
    TotalRKX=[]
    
    ts = np.linspace(t0,tf,j) #genera el tiempo
    
    #agregamos las condiciones iniciales a la solucion
    TotalEulerY.append(y0)
    TotalRKY.append(y0)
    TotalExactY.append(y0)
    
    TotalEulerX.append(x0)
    TotalRKX.append(x0)
    TotalExactX.append(x0)
    
    for i in ts[1:]: #itera el tiempo, con este for los metodos de euler y rk4 entregaran el valor de y consecutivo i-veces
        yns, xns = Euler(i, TotalEulerX[-1], TotalEulerY[-1], ((tf-t0)/j)) #h=(tf-t0)/NumPuntos
        TotalEulerX.append(xns) #actualizamos y agregamos las soluciones del metodo 
        TotalEulerY.append(yns) #actualizamos y agregamos las soluciones del metodo
        
        SRK4 = RK4(i, ((tf-t0)/j), ini,2)
        TotalRKY.append(SRK4[0])
        TotalRKX.append(SRK4[1])
       
    #soluciones con odeint tomadas como las exactas   
    ini=[y0,x0]
    ys = odeint(DifEqu, ini, ts)
    #plt.plot(ts,ys[:,0])
    #ys = np.array(ys).flatten()
    #print(ys)
    y_exact = ys[:,0]
    x_exact = ys[:,1]
    #print(y_exact)
    
    #diferencia del metodo a la solucion de odeint
    TotalDiffEulerY.append(np.abs(TotalEulerY-y_exact)) #resta de dos vectores, por lo tanto estamos agregando otro vector con la resta de valores de las soluciones, esto se itera 4 veces en j, i.e. para cada numero de puntos
    TotalDiffEulerX.append(np.abs(TotalEulerX-x_exact))
    TotalDiffRKY.append(np.abs(TotalRKY-y_exact))
    TotalDiffRKX.append(np.abs(TotalRKX-x_exact))
    
    #se agregan las soluciones de cada metodo, con cada valor de numero de puntos en Numpuntos
    Allstepst.append(ts)
    AllstepsEulerX.append(TotalEulerX) 
    AllstepsRK4X.append(TotalRKX)
    AllstepsEulerY.append(TotalEulerY)
    AllstepsRK4Y.append(TotalRKY)
    
    #media de la diferencia (de la solucion) respecto a la exacta (odeint method)
    yE_difference.append(np.mean(np.abs(TotalEulerY-y_exact)))
    yRK_difference.append(np.mean(np.abs(TotalRKY-y_exact)))
    xE_difference.append(np.mean(np.abs(TotalEulerX-x_exact)))
    xRK_difference.append(np.mean(np.abs(TotalRKX-x_exact)))
    
#para graficar
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10,10))

axes[0].set_title('n2 Solution')
axes[0].plot(ts,AllstepsEulerY[3], "b--", label="Euler")
axes[0].plot(ts,y_exact, "r" , label="odeint")
axes[0].plot(ts,AllstepsRK4Y[3], "k", label="RK4")
axes[0].grid()
axes[0].legend()


axes[1].set_title('n1 Solutions')
axes[1].plot(Allstepst[2],AllstepsEulerX[2], "b--", label="Euler")
axes[1].plot(ts,x_exact, "r" , label="odeint")
axes[1].plot(Allstepst[2],AllstepsRK4X[2], "k", label="RK4")
axes[1].grid()
axes[1].legend()

axes[2].set_title('n1 vs v2')
axes[2].plot(AllstepsRK4X[3],AllstepsRK4Y[3], "b--", label="RK4")
axes[2].plot(x_exact,y_exact, "r" , label="odeint")
axes[2].plot(AllstepsEulerX[3],AllstepsEulerY[3], "k", label="Euler")
axes[2].grid()
axes[2].legend()


#diferencia entre los metodos y odeint logaritmica en y
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14,9))

axes[0].set_title('Comparing Solutions from Methods, semilogy n2')
axes[0].semilogy(Allstepst[3],TotalDiffEulerY[3], "b--", label="Euler")
#axes[0].semilogy(ts,y_exact, "r" , label="odeint")
axes[0].semilogy(Allstepst[3],TotalDiffRKY[3], "k", label="RK4")
axes[0].grid()
axes[0].legend()

axes[1].set_title('Comparing Solutions from Methods, semilogy n1')
axes[1].semilogy(Allstepst[3],TotalDiffEulerX[3], "b--", label="Euler")
#axes[1].semilogy(ts,x_exact, "r" , label="odeint")
axes[1].semilogy(Allstepst[3],TotalDiffRKX[3], "k", label="RK4")
axes[1].grid()
axes[1].legend()

#promedio de la diferencia entre las soluciones de los metodos y odeint vs el paso (step)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14,9))

axes[0].set_title('Diference between methods solutions n2 vs step')
axes[0].plot(h,yE_difference, "b--", label="Euler")
#axes[0].semilogy(ts,y_exact, "r" , label="odeint")
axes[0].plot(h,yRK_difference, "k", label="RK4")
axes[0].grid()
axes[0].legend()

axes[1].set_title('Diference between methods solutions n2 vs step')
axes[1].plot(h,xE_difference, "b--", label="Euler")
#axes[1].semilogy(ts,x_exact, "r" , label="odeint")
axes[1].plot(h,xRK_difference, "k", label="RK4")
axes[1].grid()
axes[1].legend()
#la distancia del paso es inversa a la cantidad de puntos
#a medida que bajamos el paso, los metodos se parecen mas 
#por lo tanto a medida que aumentamos los puntos las soluciones convergen a la solucion de odeint
print("la distancia del paso es inversa a la cantidad de puntos, a medida que bajamos el paso, los metodos se parecen mas, por lo tanto a medida que aumentamos los puntos las soluciones convergen a la solucion de odeint")
plt.show()

