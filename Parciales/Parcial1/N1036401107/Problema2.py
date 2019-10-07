# -*- coding: utf-8 -*-
"""
Parcial 1
Samuel Quitian Gallego 1152222545
Elizabeth Jiménez Gómez 1036401107
"""

import numpy as np                   #Para calculos
import matplotlib.pyplot as plt      #para graficar 
from scipy.integrate import odeint   #para resolver


a=1. # Parametri de la ecuación.
b=1. # Parametro de la ecuación.
c=1. # Parametro de la ecuación.
d=1. # Parametro de la ecuación.


tf=12  # Tiempo final.
t0=0   # Condición inicial de la variable t.
y0=[1.5,1.] # Condiciones iniciales de n_1 y n_2.

def dn2(n2,t,n1):             # Evolucion del gas 2
    return -n2*(c-d*n1)       # Devuelve la derivada n_2'
def dn1(n1,t,n2):             # Evolucion del gas 1
    return n1*(a-b*n2)        # Devuelve la derivada n_1'
def f(y,t):                   # Se define una función F(N)=N' donde N=(n_1,n_2) y N'=(n_1',n_2').
    n1, n2= y                 # Por simplicidad en el cálculo se redefinen las variables.
    return [n1*(a-b*n2),-n2*(c-d*n1)] # Devielve un arreglo con las derivadas

def Euler(xn,yn,h,MyF):                  # Método de Euler
        return yn+(h*MyF(yn,t,xn))       # El método nos dice que y_n+1 = y_n + (h*F(t, x_n, y_n)) donde y_n+1=y'
    
def RK(xn,yn,h,f):                               #Método de Runge Kutta

       k1=h*f(yn,t,xn)                           #Parametro k1 del método RK4.
       k2=h*f(yn+h*k1/2.,t+h/2.,xn+h*k1/2.)      #Parametro k2 del método RK4.
       k3=h*f(yn+h*k2/2.,t+h/2.,xn+h*k2/2.)      #Parametro k3 del método RK4.
       k4=h*f(yn +h*k3,t+h,xn+h*k3)              #Parametro k4 del método RK4.

       return yn + (k1+2.*k2+2.*k3+k4)/6.        # Devuelve el valor de la derivada de la función.
    
NumPuntos=np.array([100,1000,10000])             #Número de puntos que tendra el intervalo.
    
    
h=(tf-t0)/NumPuntos  #paso, delta t.  

Totalen1=[]        #lista que tendra los resultados para el gas 1 con metodo de euler
Totalen2=[]        #lista que tendra los resultados para el gas 2 con metodo de euler
TotalRKn1=[]       #lista que tendra los resultados para el gas 1 con metodo de RK
TotalRKn2=[]       #lista que tendra los resultados para el gas 2 con metodo de RK
Totalns1=[]        #lista que tendra los resultados con odeint para el gas 1
Totalns2=[]        #lista que tendra los resultados con odeint para el gas 2
Totalt=[]          #lista que tendra los intervalos de tiempo

Diffen1=[]         #Lista que tendrá la diferencia entre euler y la solución con odeint del gas 1.
Diffen2=[]         #Lista que tendrá la diferencia entre euler y la solución con odeint del gas 2.
DiffRn1=[]         #Lista que tendrá la diferencia entre RK4 y la solución con odeint del gas 1.
DiffRn2=[]         #Lista que tendrá la diferencia entre RK4 y la solución con odeint del gas 2.

for i in NumPuntos:                #ciclo que hace las soluciones para distintos numeros de puntos en el intervalo temporal
    EulerSolutionsn1=[]            #lista que trendra las soluciones del metodo de euler para el gas 1 con i puntos 
    EulerSolutionsn2=[]            #lista que trendra las soluciones del metodo de euler para el gas 2 con i puntos 
    RKSoln1=[]                     #lista que trendra las soluciones del metodo de RK para el gas 1 con i puntos 
    RKSoln2=[]                     #lista que trendra las soluciones del metodo de RK para el gas 2 con i puntos 
    
    #se añaden las condiciones iniciales a los arreglos 
    EulerSolutionsn1.append(y0[0])  #Se añade la condición inicial al arreglo de la solución con Euler para el gas 1.
    EulerSolutionsn2.append(y0[1])  #Se añade la condición inicial al arreglo de la solución con Euler para el gas 2.
    RKSoln1.append(y0[0])           #Se añade la condición inicial al arreglo de la solución con RK4 para el gas 1.
    RKSoln2.append(y0[1])           #Se añade la condición inicial al arreglo de la solución con RK4 para el gas 2.
    
    
    t=np.linspace(t0,tf,i)          #arreglo de tiempo (Espacio muestral) 
    
    for j in t[1:]:                 #Empieza desde el elemento dos para que no haya un sobreconteo.
         CurrentSolutionn1=Euler(EulerSolutionsn2[-1],EulerSolutionsn1[-1],((tf-t0)/i),dn1) #solución inmediata para el gas 1 con metodo de euler
         CurrentSolutionn2=Euler(EulerSolutionsn1[-1],EulerSolutionsn2[-1],((tf-t0)/i),dn2) #solucion inmediata para el gas 2 con metodo de euler
         CurrentSolRKn1=RK(RKSoln2[-1],RKSoln1[-1],((tf-t0)/i),dn1) #solucion inmediata para el gas 1 con metodo de RK4
         CurrentSolRKn2=RK(RKSoln1[-1],RKSoln2[-1],((tf-t0)/i),dn2) #solucion inmediata para el gas 2 con metodo de RK4
 
         EulerSolutionsn1.append(CurrentSolutionn1)  #Se añade la solución inmediata del gas 1 por el método de Euler al arreglo.
         EulerSolutionsn2.append(CurrentSolutionn2)  #Se añade la solución inmediata del gas 2 por el método de Euler al arreglo.
         RKSoln1.append(CurrentSolRKn1)              #Se añade la solución inmediata del gas 1 por el método de RK4 al arreglo.
         RKSoln2.append(CurrentSolRKn2)              #Se añade la solución inmediata del gas 1 por el método de RK4 al arreglo.
         
    
    y=odeint(f,y0,t) #solucion usando odeint

    Totalen1.append(EulerSolutionsn1)   #Se añade la solución encontrada para el gas 1 por Euler. 
    Totalen2.append(EulerSolutionsn2)   #Se añade la solución encontrada para el gas 2 por Euler.
    TotalRKn1.append(RKSoln1)           #Se añade la solución encontrada para el gas 1 por RK4.
    TotalRKn2.append(RKSoln2)           #Se añade la solución encontrada para el gas 2 por RK4.
    Totalns1.append(y[:,0])             #Se añade la solución encontrada para el gas 1 por odeint.
    Totalns2.append(y[:,1])             #Se añade la solución encontrada para el gas 2 por odeint. 
    Totalt.append(t)                    #Se añade un arreglo de tiempo.
    

    Diffen1.append(abs(EulerSolutionsn1-y[:,0]))   #Se añade el error entre Euler y odeint para el gas 1.
    Diffen2.append(abs(EulerSolutionsn2-y[:,1]))   #Se añade el error entre Euler y odeint para el gas 2.
    DiffRn1.append(abs(RKSoln1-y[:,0]))            #Se añade el error entre RK4 y odeint para el gas 1.
    DiffRn2.append(abs(RKSoln2-y[:,1]))            #Se añade el error entre RK4 y odeint para el gas 2.

#comparacion de los metodos con odeint para ver la convergencia

DifeP1=[]     # Lista para el promedio de la diferencia en comparación con el paso del método de Euler para el gas 1.
DifeP2=[]     # Lista para el promedio de la diferencia en comparación con el paso del método de Euler para el gas 2.
DifRP1=[]     # Lista para el promedio de la diferencia en comparación con el paso del método de RK4 para el gas 1.
DifRP2=[]     # Lista para el promedio de la diferencia en comparación con el paso del método de RK4 para el gas 2.

for k in range(len(NumPuntos)):   #Ciclo que va a calcular los promedios de las diferencias.
    
    DifeP1.append(np.mean(Diffen1[k]))    # np.mean() calcula el promedio de la diferencia para el gas 1 por Euler.
    DifeP2.append(np.mean(Diffen2[k]))    # Se añade el promedio de la diferencia para el gas 2 por Euler.
    DifRP1.append(np.mean(DiffRn1[k]))    # Se añade el promedio de la diferencia para el gas 1 por RK4.
    DifRP2.append(np.mean(DiffRn2[k]))    # Se añade el promedio de la diferencia para el gas 2 por RK4.

plt.figure()      # Prepara el espacio de graficación.

ax0=plt.subplot() # Sub gráfica que contiene la evolución de los gases por los 3 métodos.

ax0.plot(Totalen1[2],Totalen2[2],'r--',label='Euler')             #Evolución de los gases por Euler.  
ax0.plot(TotalRKn1[2],TotalRKn2[2],'g--',label='Runge Kutta')     #Evolución de los gases por RK4.
ax0.plot(Totalns1[2],Totalns2[2],'b--',label='odeint')            #Evolución de los gases por odeint.

ax0.set_ylabel('n1')        # Nombre del eje y.                           
ax0.set_xlabel('n2')        # Nombre del eje x.
ax0.set_title('n1 vs n2')   # Titulo del gráfico.
ax0.legend()                # Permite que aprezcan los nombres de los ejes y el título
plt.figure()                # Prepara el espacio de graficación.

ax1=plt.subplot()  # Grafica el tiempo contra la evolución de cada gas mostrando como varia en el intervalo temporal.

plt.figure()       # Prepara el espacio de graficación.

ax1.plot(Totalt[2],Totalen1[2],'r--',label='Euler-n1')  # Evolución del gas 1 por Euler en el tiempo.
ax1.plot(Totalt[2],Totalen2[2],'g',label='Euler-n2')    # Evolución del gas 2 por Euler en el tiempo.
ax1.plot(Totalt[2],TotalRKn1[2],'c',label='RK-n1')      # Evolución del gas 1 por RK4 en el tiempo.
ax1.plot(Totalt[2],TotalRKn2[2],'m--',label='RK-n2')    # Evolución del gas 2 por RK4 en el tiempo.
ax1.plot(Totalt[2],Totalns1[2],'y--',label='Odeint-n1') # Evolución del gas 1 por odeint en el tiempo.
ax1.plot(Totalt[2],Totalns2[2],'b--',label='Odeint-n2') # Evolución del gas 2 por odeint en el tiempo.
ax1.set_ylabel('a.u')                        #Nombre del eje y.
ax1.set_xlabel('t(s)')                       #Nombre del eje x.
ax1.set_title('tiempo vs cantidad del gas')  #Titulo de la grafica.
ax1.legend()                                 #Permite que aparezcan los nombres de los ejes y el título.
    

ax2=plt.subplot(121)     # Grafica los errores de los métodos.

#diferencias y su evolucion temporal para cierto valor de paso
ax2.semilogy(Totalt[1],Diffen1[1],'r--',label='Diff euler-n1')  # Evolución temporal del error del gas 1 con Euler.  
ax2.semilogy(Totalt[1],Diffen2[1],'g--',label='Diff euler-n2')  # Evolución temporal del error del gas 2 con Euler.
ax2.semilogy(Totalt[1],DiffRn1[1],'b--',label='Diff RK-n1')     # Evolución temporal del error del gas 1 con RK4.
ax2.semilogy(Totalt[1],DiffRn2[1],'m--',label='Diff RK_n2')     # Evolución temporal del error del gas 2 con RK4.
ax2.set_ylabel('diff')        # Nombre del eje y.
ax2.set_xlabel('t(s)')        # Nombre del eje x.
ax2.set_title('tiempo vs Error') #Titulo del grafico
ax2.legend()                  # Permite que aparezcan los nombres de los ejes y el título.


ax3=plt.subplot(122)      #Grafica las diferencias promedio con respecto al paso, lo que nos habla de la convergencia de los métodos.

ax3.plot(h,DifeP1,'r--',label='Error-paso. euler-n1' )  # Convergencia de Euler para el gas 1.
ax3.plot(h,DifeP2,'g--',label='Error-paso. euler-n2' )  # Convergencia de Euler para el gas 2.
ax3.plot(h,DifRP1,'b--',label='Error-paso. RK4-n1' )  # Convergencia de RK4 para el gas 1.
ax3.plot(h,DifRP2,'m--',label='Error-paso. RK4-n2' )  # Convergencia de RK4 para el gas 2. 
ax3.set_ylabel('Prom-err')        # Nombre del eje y.
ax3.set_xlabel('Paso')            # Nombre del eje x.
ax3.set_title('Paso vs Err')      # Titulo del grafico.
ax3.legend()                      # Permite que aparezcan los nombres de los ejes y el título.

#de esta ultima grafica se puede ver que las soluciones convergen 
plt.show() # Para que muestre las gráficas.
