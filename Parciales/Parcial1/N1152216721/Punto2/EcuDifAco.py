#####----- Este Programa soluciona dos ED acopladas-----#####
#-*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.ticker import NullFormatter  # useful for `logit` scale


## Definición de los valores para los parámetros de la Ecu Diferenciales

a=1.
b=1.
c=1.
d =1.0  


#Integrador método de Euler

def Euler(m,n,h,F):

    return m +  h*F(m,n)

#Integrador método de RK4

def RK4(m,n,h,F): 
    k1=h*F(m,n)
    k2=h*F(m + (h*k1/2),n + (h*k1/2))
    k3=h*F(m + (h*k2/2),n + (h*k2/2))
    k4=h*F(m + h*k3,n + h*k3)

    return m + (k1+ 2*k2 + 2*k3 + k4)/6


# Ecuación diferencial a solucionar para n1

def F1(n1,n2):   
    return n1*(a-b*n2)

#Ecuación diferencial a la solucionar para n2

def F2(n2,n1):   
    return -n2*(c-d*n1)

# Ecuación diferencial a solucionar por Odeint 
def F12(y, t):
     n1, n2 = y
     dydt = [F1(n1,n2), F2(n2,n1)]
     return dydt



N=[100,100000,1000000] #número de puntos para la solución
#N=np.array([1e5])

t0=0. #Condición inicial para el tiempo
tf=12. #Donde quiero llegar
n10=1.5 # condición inicial para n1
n20=1. # condición inicial para n2 
y0 = [n10, n20] # arreglo de CI para el utilizar con odeint
ErrME=[]
ErrMRK=[]


###++++BLOQUE DE INTEGRACION++++###



## Este primer ciclo permite realizar la integración para 
## diferentes valores de números de puntos en el dominio de integración 

for j in N:
    #print(j)
    Sn1=[] # lista que almacena las soluciones para n1 por ME
    Sn2=[] # lista que almacena las soluciones para n2 por ME

    SRKn1=[] # lista que almacena las soluciones para n1 por RKM
    SRKn2=[] # lista que almacena las soluciones para n2 por RKM
    
    T=np.linspace(t0,tf,j)
    
   
    Sn1.append(n10)
    Sn2.append(n20)

    SRKn1.append(n10)
    SRKn2.append(n20)

    h=(tf-t0)/j # definición del tamaño de paso

    sol = odeint(F12, y0, T) # solución a la ecuacion diferencial por Odeint


    ## En el segundo ciclo realizamos la iteración para la integración por Euler y RK4     
    
    for i in T[1:]:
        N1 = Euler(Sn1[-1],Sn2[-1],h,F1) ## en esta línea calculamos el valor de n1 en Tn+1 por el método de Euler
        N2 = Euler(Sn2[-1],Sn1[-1],h,F2) ## en esta línea calculamos el valor de n2 en Tn+1 por el método de Euler

        Sn1.append(N1)
        Sn2.append(N2)

        N1rk = RK4(Sn1[-1],Sn2[-1],h,F1) ## en esta línea calculamos el valor de n1 en Tn+1 por el método de RK4
        N2rk = RK4(Sn2[-1],Sn1[-1],h,F2) ## en esta línea calculamos el valor de n1 en Tn+1 por el método de RK4

        SRKn1.append(N1rk)
        SRKn2.append(N2rk)
    
    MaxE=np.amax(np.abs((sol[:, 0]-Sn1)/sol[:, 0]))
    MaxRK=np.amax(np.abs((sol[:, 0]-SRKn1)/sol[:, 0]))
    ErrME.append(MaxE)
    ErrMRK.append(MaxRK)

###++++BLOQUE DE GRAFICACION++++###        
    
    plt.subplot(4, 2, 1)
    plt.plot(T, Sn1, 'r')
    plt.title('Solucion por metodo de Euler para N=%(N)d' %{'N':j} )
    plt.ylabel('n1')
    plt.grid(True)
    
    plt.subplot(4, 2, 3)
    plt.plot(T, Sn2, 'b')
    plt.xlabel('Tiempo')
    plt.ylabel('n2')
    plt.grid(True)

    plt.subplot(4, 2, 5)
    plt.plot(Sn1, Sn2, 'y')
    plt.xlabel('n1')
    plt.ylabel('n2')
    plt.grid(True)

    plt.subplot(4, 2, 2)
    plt.plot(T, SRKn1, 'r')
    plt.title('Solucion por metodo de RK4 para N= %(N)d' %{'N':j})
    plt.ylabel('n1')
    plt.grid(True)

    plt.subplot(4, 2, 4)
    plt.plot(T, SRKn2, 'b')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('n2')
    plt.grid(True)

    plt.subplot(4, 2, 6)
    plt.plot(SRKn1, SRKn2, 'y')
    plt.xlabel('n1')
    plt.ylabel('n2')

    plt.grid(True)
    
    ## Utilizamos el error relativo pues este es más sensible a la magnitud de la variable
    ## presentamos una gráfica semilogaritmica
    plt.subplot(4, 1, 4)
    plt.semilogy(T, np.abs((sol[:, 0]-SRKn1)/sol[:, 0]),'b',label='RK n1')
    plt.semilogy(T, np.abs((sol[:, 0]-Sn1)/sol[:, 0]),'g',label='ME n1')
    #plt.semilogy(T, np.abs((sol[:, 1]-SRKn2)/sol[:, 1]),'r',label='RK n2')
    #plt.semilogy(T, np.abs((sol[:, 1]-Sn2)/sol[:, 1]),'c',label='ME n2')
    plt.title('Error relativo vs Tiempo para el metodo de Euler y RK4 para N= %(N)d' %{'N':j})
    
    plt.xlim(0,13)
    plt.ylim(1,1e-10)
    plt.legend(loc='lower right', borderaxespad=0.)
    plt.grid(True)


    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=1.5,wspace=0.35)

    plt.show()

##Finalmente graficamos el error relativo Máximo para cada una de las iteraciones y para cada método
plt.semilogy(N,ErrME,'k*',label='ME')
plt.semilogy(N,ErrMRK,'r*',label='MRK')
plt.grid(True)
plt.xlabel('Numero de puntos')
plt.ylabel('Error relativo')
plt.title('maximo error relativo vs Numero de puntos')
plt.legend()
plt.show()
