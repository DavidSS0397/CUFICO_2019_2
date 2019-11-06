#Se importan las librerias necesarias para graficar y solucionar el sistema de ecuaciones diferenciales.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definicion de constantes dentro del sistema
a=1.0
b=1.0
c=1.0
d=1.0

#Metodo de Euler para solucionar ecuaciones diferenciales
def Euler(yn, xn, h, F): #yn, xn son las variables sobre las que se soluciona el sistema
    return yn + h*F(yn,xn) #h es el paso del tiempo y F la funcion que define la ecuacion diferencial


#Metodo de Runge Kutta
#El metodo se generaliza dado que se tiene un sistema de ecuaciones diferenciales acoplado
def Runge_Kutta4(xn, yn, h, F1,F2):
#El procedimiento corresponde a definir cada uno de los valores de "k" de manera independiente para cada una de las ecuaiones diferenciales 
    xn1 = xn + h
    k11 = h*F1(yn, xn)
    k12 = h*F2(yn, xn)
    k21 = h*F1(yn+h*k11*0.5, xn+h*0.5)
    k22 = h*F2(yn+h*k12*0.5, xn+h*0.5)
    k31 = h*F1(yn+h*k21*0.5, xn+h*0.5)
    k32 = h*F2(yn+h*k22*0.5, xn+h*0.5)
    k41 = h*F1(yn+h*k31, xn+h)
    k42 = h*F2(yn+h*k32, xn+h)
    y1=yn + (1/6.)*(k11 + 2.*k21 + 2.*k31 + k41)
    y2=yn + (1/6.)*(k12 + 2.*k22 + 2.*k32 + k42)

   
    return y1,y2 #Devuelve el valor de cada una de las iteraciones para las dos ecuaciones diferenciales 

#Definicion de la primera ecuacion diferencial
def F1(n1,n2):
    return n1*(a-b*n2)

#Definicion de la segunda ecuacion diferencial
def F2(n2,n1):
    return -n2*(c-d*n1)


N=np.array([100, 1000, 10000, 100000]) #Arreglo para determinar el numero de iteraciones
t0=0.0 #Tiempo inicial
tf=12.0 #Tiempo final
n1_0=1.5 #Condicion inicial para el gas 1
n2_0=1.0 #Condicion inicial para el gas 2

#Arreglo que contiene la diferencia entre la solucion "exacta" (odeint) y cada uno de los metodos (usados para determinar convergencia.)
DiffEuler_1 = [] 
DiffRK_1 = []
H=[] #Guarda los valores del contador (j)


#Definicion de un ciclo para desarrollar el metodo de Euler y Runge Kutta 
for j in N: #Realiza las iteraciones hasta N
    Sn1_Euler=[] #Guarda las soluciones "locales" para el gas 1 con el metodo de Euler
    Sn2_Euler=[] #Guarda las soluciones "locales" para el gas 2 con el metodo de Euler
    Sn1_RK=[] #Guarda las soluciones "locales" para el gas 1 con el metodo de Runge Kutta
    Sn2_RK=[] #Guarda las soluciones "locales" para el gas 2 con el metodo de Runge Kutta
    T=np.linspace(t0, tf, j) #Arreglo para determinar el tiempo (variable independiente)

    #Se guardan las condiciones iniciales del sistema
    Sn1_Euler.append(n1_0)
    Sn2_Euler.append(n2_0)
    Sn1_RK.append(n1_0)
    Sn2_RK.append(n2_0)
    h=(tf-t0)/j #Valor del paso 

    #Ciclo para barrer sobre todos los valores del tiempo
    for i in T[1:]:
        N1 = Euler(Sn1_Euler[-1], Sn2_Euler[-1], h, F1)#Solucion gas 1 con Euler
        N2 = Euler(Sn2_Euler[-1], Sn1_Euler[-1], h, F2)#Solucion gas 2 con Euler
        N1_RK = Runge_Kutta4(Sn2_RK[-1], Sn1_RK[-1], h,F1, F2)[0]#Solucion gas 1 con Runge Kutta
        N2_RK = Runge_Kutta4(Sn1_RK[-1], Sn2_RK[-1], h, F1, F2)[1]#Solucion gas 2 con Runge Kutta

        #Se guardan las soluciones locales halladas con los metodos
        Sn1_Euler.append(N1)
        Sn2_Euler.append(N2)
        Sn1_RK.append(N1_RK)
        Sn2_RK.append(N2_RK)

        
        #Solucion del sistema con odeint
    def ODEINT(y, t):
        n1, n2 = y #y es un vector que contiene n1 y n2, las variables de estado del sistema
        dydt = [ n1*(a-b*n2), -n2*(c-d*n1)]
        return dydt #Retorna el sistema de ecuaciones diferenciales

    y0 = [n1_0 , n2_0] #Definicion de las condiciones iniciales

    sol=odeint(ODEINT, y0, T) #Solucion con odeint

    #Para determinar la convergencia del sistema, se toma el promedio sobre las diferencias entre el metodo usada y la solucion "exacta" (realizada con odeint)
    DiffEuler_1.append(np.mean(np.abs(Sn1_Euler-sol[:,0])))
    DiffRK_1.append(np.mean(np.abs(Sn1_Euler-sol[:,0])))
    H.append(j)

    #Graficas
    fig = plt.figure(figsize=(12, 4))

    #Subplots
    ax0 = fig.add_subplot(141)
    ax1 = fig.add_subplot(142)
    ax2 = fig.add_subplot(143)
    ax3 = fig.add_subplot(144)
   
   
    ax0.plot(T, sol[:, 0], label="Odeint") #Contiene la solucion para el gas 1 con odeint, con respecto al tiempo 
    ax1.plot(T, sol[:, 1], label="Odeint") #Contiene la solucion para el gas 2 con odeint, con respecto al tiempo 
    ax2.plot(sol[:, 0], sol[:, 1], "c",label="Odeint") #Contiene la solucion para el gas 1 y 2 con odeint, retrato de fase
    ax0.plot(T, Sn1_Euler, "r", label="Euler" ) #Contiene la solucion para el gas 1 con Euler, con respecto al tiempo 
    ax1.plot(T, Sn2_Euler, "r", label="Euler" )#Contiene la solucion para el gas 2 con Euler , con respecto al tiempo 
    ax2.plot(Sn1_Euler, Sn2_Euler,label="Euler") #Contiene la solucion para el gas 1 y 2 con Euler, retrato de fase 
    ax0.plot(T, Sn1_RK, "g", label="RK" ) #Contiene la solucion para el gas 1 con Runge Kutta, con respecto al tiempo 
    ax1.plot(T, Sn2_RK, "g", label="RK" ) #Contiene la solucion para el gas 2 con Runge Kutta, con respecto al tiempo 
    ax2.plot(Sn1_RK, Sn2_RK,label="RK")#Contiene la solucion para el gas 1 y 2 con Runge Kutta, retrato de fase 
    ax2.set_xlabel('n1')
    ax2.set_ylabel('n2')
    ax1.set_xlabel("t")
    ax1.set_ylabel("n2")
    ax0.set_xlabel("t")
    ax0.set_ylabel("n1")
    ax3.set_xlabel('h')
    ax3.set_ylabel('Error')
    ax0.legend()
    ax1.legend()
    ax2.legend()
    ax3.plot(H,DiffEuler_1,label="Euler") #Grafica del error para el metodo de Euler 
    ax3.plot(H,DiffRK_1,label="RK")#Grafica del error para el metodo de Runge Kutta
    ax3.legend()

    #De la ultima grafica logra identificarse que, a medida que aumenta el valor de H (es decir, aumentan el numero de puntos y por tanto disminuye el paso), el error disminuye y por tanto, los valores convergen.
    plt.show()

   
    


