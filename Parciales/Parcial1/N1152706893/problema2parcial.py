import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint #libreria para solucion de ED

def f(y,t,x): #ecuacion diferencial de y
    c=1
    d=1
    return -1*y*(c-d*x)

def g(x,t,y): #ecuacion diferencial de x
    a=1
    b=1
    return x*(a-b*y)

def Euler(tn,Xn,Yn,h,F,G): #solucion de euler
    
    yn=Yn+(h*F(Yn,tn,Xn))
    xn=Xn+(h*G(Xn,tn,Yn))
    
    return yn,xn

def rk4(tn,Xn,Yn,h,F,G): #solucion metodo runge kuta4
    
    k1y=h*F(Yn,tn,Xn)
    k1x=h*G(Xn,tn,Yn)
    
    k2y=h*F(Yn+0.5*h*k1y,tn+h*0.5,Xn+0.5*h*k1x)
    k2x=h*G(Xn+0.5*h*k1x,tn+h*0.5,Yn+0.5*h*k1y)
    
    k3y=h*F(Yn+h*0.5*k2y,tn+0.5*h,Xn+0.5*h*k2x)
    k3x=h*G(Xn+h*0.5*k2x,tn+0.5*h,Yn+0.5*h*k2y)
    
    k4y=h*F(Yn+h*k3y,tn+h,Xn+h*k3x)
    k4x=h*G(Xn+h*k3x,tn+h,Yn+h*k3y)
    
    yn= Yn + (k1y + 2*k2y + 2*k3y + k4y)/6.0
    xn= Xn + (k1x + 2*k2x + 2*k3x + k4x)/6.0

    return yn , xn  
    
NumPuntos=np.array([10,100,1000,10000]) #pasos 

t0=0. #punto inicial
tf=12. #punto final
y0=1. #punto inicial
x0=1.50  #punto inicial

h=(tf - t0)/NumPuntos
print(h)
#la idea es calcular las diferencias entre el real y el predicho

#calcula la diferencia entre el valor predicho por el modelo y el valor real (ojo solo si hay solucion analitica) sol anali=met odeint
yE_difference=[] #metodo euler
yRK4_difference=[] #metodo rk4  
xE_difference=[] #metodo euler
xRK4_difference=[] #metodo rk4 

#sol exact=met odeint
Totalexacty=[] #matriz de etiquetas o valores reales (SI HAY SOL ANALITICA)
Totalexactx=[] #matriz de etiquetas o valores reales (SI HAY SOL ANALITICA) 

Totaleulery=[] #matriz de valores predicho metodo euler
TotalRK4y=[] #matriz de valores predicho metodo RK4
Totaleulerx=[] #matriz de valores predicho metodo euler
TotalRK4x=[] #matriz de valores predicho metodo RK4


Totalts=[] #matriz de variables reales


Totaldiffeulery=[]#euler  #matriz de error de truncamiento valor predicho menos valor real
TotaldiffRK4y=[]#rk4  #matriz de error de truncamiento valor predicho menos valor real
Totaldiffeulerx=[]#euler  #matriz de error de truncamiento valor predicho menos valor real
TotaldiffRK4x=[]#rk4  #matriz de error de truncamiento valor predicho menos valor real

for j in NumPuntos:
    # print("j",j) #j toma valores de 10, 100,1000,10000
    
    Eulersolutionsy=[]  #matriz de solucion de euler 
    RK4solutionsy=[] #matriz de solucion de RK4
    Eulersolutionsx=[]  #matriz de solucion de euler 
    RK4solutionsx=[] #matriz de solucion de RK4
    
    ts=np.linspace(t0,tf,j)  #imprime los ts entre 0 y 12 donde el arreglo tiene en cada for 10,100,1000,10000 elementos


    Eulersolutionsy.append(y0) #agrego primer termino de condicion inicial
    RK4solutionsy.append(y0) #agrego termino de solucion RK4
    Eulersolutionsx.append(x0) #agrego primer termino de condicion inicial
    RK4solutionsx.append(x0) #agrego termino de solucion RK4
    
    for i in ts[1:]:
        Currentsolutiony, Currentsolutionx=Euler(i,Eulersolutionsx[-1],Eulersolutionsy[-1], ((tf- t0)/j),f,g)
        Eulersolutionsy.append(Currentsolutiony) #solucion de euler
        Eulersolutionsx.append(Currentsolutionx) #solucion de euler

  
        CurrentsolutionRK4y, CurrentsolutionRK4x =rk4(i,RK4solutionsx[-1],RK4solutionsy[-1], ((tf - t0)/j),f,g)
        RK4solutionsy.append(CurrentsolutionRK4y) #solucion RK4
        RK4solutionsx.append(CurrentsolutionRK4x) #solucion RK4
        
    def funcion(dyx,ts): #funcion para pasar las dos funciones x y y a odeint
        dy,dx=dyx
        dyxdt=[-dy*(1-dx),dx*(1-dy)]
        return dyxdt
    
    yx0=[y0,x0]
    ys = odeint(funcion, yx0, ts)
    ysy=ys[:,0] #valor exacto en y por odeint
    ysx=ys[:,1] #valor exacto en x por odeint
    

    #error de truncamiento
    
    Totaldiffeulery.append(np.abs(Eulersolutionsy -ysy)) #truncamiento metodo euler
    TotaldiffRK4y.append(np.abs(RK4solutionsy -ysy)) #truncamiento rk4
    Totaldiffeulerx.append(np.abs(Eulersolutionsx -ysx)) #truncamiento metodo euler
    TotaldiffRK4x.append(np.abs(RK4solutionsx -ysx)) #truncamiento rk4
    
    Totaleulery.append(Eulersolutionsy) #matriz solucion predicha met euler
    TotalRK4y.append(RK4solutionsy) #matriz solucion predicha met rk4
    Totaleulerx.append(Eulersolutionsx) #matriz solucion predicha met euler
    TotalRK4x.append(RK4solutionsx) #matriz solucion predicha met rk4
    
    Totalexacty.append(ysy) #matriz de valores reales
    Totalexactx.append(ysx) #matriz de valores reales                                      
    Totalts.append(ts) #matriz de variables

    yE_difference.append(np.mean(np.abs(Eulersolutionsy-ysy))) # matriz de promedio de error de truncamiento con met euler
    yRK4_difference.append(np.mean(np.abs(RK4solutionsy-ysy))) # matriz de promedio de error de truncamiento con met rK4
    xE_difference.append(np.mean(np.abs(Eulersolutionsx-ysx))) # matriz de promedio de error de truncamiento con met euler
    xRK4_difference.append(np.mean(np.abs(RK4solutionsx-ysx))) # matriz de promedio de error de truncamiento con met rK4


fig= plt.figure(figsize=(12,12))

#para graficar 
ax0= fig.add_subplot(141)
ax1= fig.add_subplot(142)
ax2 = fig.add_subplot(143)
ax3=fig.add_subplot(144)

ax0.plot(Totalts[3],Totaleulery[3], "b", label="euler y") #graficas de las respectivas soluciones
ax0.plot(Totalts[3],TotalRK4y[3], "p-", label="RK4 y")
ax0.plot(Totalts[3],Totalexacty[3], "g--", label="solexact y")
ax1.plot(Totalts[3],Totaleulerx[3], "c-", label="euler x")
ax1.plot(Totalts[3],TotalRK4x[3], "y-", label="RK4 x")
ax1.plot(Totalts[3],Totalexactx[3], "k-", label="solexact x")

ax0.legend()

ax1.legend()

ax2.plot(h, yE_difference, "b") #grafica relacionada con la convergencia para h muy pequeño las soluciones convergen 
ax2.plot(h, yRK4_difference, "p-")
ax2.plot(h, xE_difference, "c-")
ax2.plot(h, xRK4_difference, "y-")

ax3.plot(Totaleulerx[3],Totaleulery[3],"g-", label="euler") #graficas de xvsy
ax3.plot(TotalRK4x[3],TotalRK4y[3], "c--", label="RK4")
ax3.legend()

#veamos si la solucion es o no convergente

#Lo que vamos hacer es calcular la diferencia y ver si cuando h tiende a cero
#las diferencias tienden a cero

for i in range(len(NumPuntos)):
    euy=np.reshape(Totaleulery[i],(len(Totaleulery[i]),1))
    eux=np.reshape(Totaleulerx[i],(len(Totaleulerx[i]),1))
    ex=np.reshape(Totalexacty[i],(len(Totalexacty[i]),1))
    rk4y=np.reshape(TotalRK4y[i],(len(TotalRK4y[i]),1))
    rk4x=np.reshape(TotalRK4x[i],(len(TotalRK4x[i]),1))

    difey=np.abs(euy-ex) #error
    promey=np.mean(difey) #promedio del error
    difex=np.abs(eux-ex) #error
    promex=np.mean(difex) #promedio del error
    difrk4y=np.abs(rk4y-ex) #error
    promrk4y=np.mean(difrk4y) #promedio del error
    difrk4x=np.abs(rk4x-ex) #error
    promrk4x=np.mean(difrk4x) #promedio del error
    
    
    print("con tamaño del paso igual", h[i])
    print("el error promedio es para euler en y ", promey)
    print("el error promedio es para rk4 en y ", promrk4y)
    print("el error promedio es para euler en x ", promex)
    print("el error promedio es para rk4 en x ", promrk4x)



plt.show()


