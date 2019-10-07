"""
Solucion a Ecuaciones diferenciales acopladas 
"""
#Se importan las librerias
import numpy as np                   #Libreria para uso de array, 
import matplotlib.pyplot as plt      #Libreria para graficar
from scipy.integrate import odeint   #Se importa la herramienta ODEINT de la libreria scipy que es para resolver EDO

#Se escribe una funcion que ejecuta el metodo de Euler
def Euler(y0, x0, t0, h, F2, F1):     #Toma como parametros los valores iniciales, el paso y las EDO a solucionar
        xn = x0 + h*F1(y0,x0,t0)      #Valor que devuelve el metodo un paso despues para la primera EDO 
        yn = y0 + h*F2(y0,x0,t0)      #Valor que devuelve el metodo un paso despues para la segunda EDO  
        return [yn,xn]                #La funcion devuelve ambos valores un paso despues
    
    
#Se escribe una funcion que ejecuta el metodo de Runge Kutta 4     
def RK4(y0, x0, t0, h, F2, F1):     #Toma como parametros los valores iniciales, el paso y las EDO a solucionar

    #Se escriben las constantes para solucionar las EDO por metodo de Runge Kutta  
    ky1 = h*F2( y0, x0, t0)        #K1 para la primera EDO
    kx1 = h*F1( y0, x0, t0)        #K1 para la segunda EDO
    
    ky2 = h*F2( y0+h*ky1/2, x0+h*kx1/2, t0+h/2) #K2 para la primera EDO
    kx2 = h*F1( y0+h*ky1/2, x0+h*kx1/2, t0+h/2) #K2 para la segunda EDO
    
    ky3 = h*F2( y0+h*ky2/2, x0+h*kx2/2, t0+h/2) #K3 para la primera EDO
    kx3 = h*F1( y0+h*ky2/2, x0+h*kx2/2, t0+h/2) #K3 para la segunda EDO
    
    ky4 = h*F2( y0+h*ky3, x0+h*kx3, t0+h) #K4 para la primera EDO
    kx4 = h*F1( y0+h*ky3, x0+h*kx3, t0+h) #K4 para la segunda EDO
     
    yn = y0 + (1/6.)*(ky1 + 2*ky2 + 2*ky3 + ky4) #Valor que devuelve el metodo un paso despues para la primera EDO 
    xn = x0 + (1/6.)*(kx1 + 2*kx2 + 2*kx3 + kx4) #Valor que devuelve el metodo un paso despues para la segunda EDO 
    
    return [yn,xn]         #La funcion devuelve ambos valores un paso despues
    
    
def F1(y,x,t):       #Se define la primera EDO
    return x*(1-y)   #Devuelve la forma de la primera EDO

def F2(y,x,t):       #Se define la segunda EDO
    return -y*(1-x)  #Devuelve la forma de la segunda EDO


def df_dt(y,t):      #Funcion vectorial con F2 en su primera entrada y F1 en la segunda, sera usada para Odeint 
    a, b, c, d = 1., 1., 1., 1.  # Constantes de F1 y F2 son 1
    n2, n1 = y                       #La funcion toma como valor de entrada y y con este se calcula F1 Y F2
    f = [-n2*(c - d*n1), n1*(a - b*n2)]   # Devuelve F1(y) en la primera componente y F2(y) en la segunda 
    return f
    
Numpuntos=np.array([10,100,1000,10000]) #Se define un arreglo para las cantidad de puntos a usar para solucionar la EDO
x0=1.50       #Valor inicial para la primera EDO 
y0=1.00       #Valor inicial para la segunda EDO 
t0=0.         #Valor inicial de la variable independiente
tf=12.        #Valor final de la variable independiente
H=(tf-t0)/Numpuntos #Definicion de paso


diffy_Euler=[]             # Arreglo vacio para guardad la diferencia promedio de N2   ( Y_Euler - Y_Odeint )
diffx_Euler=[]             # Arreglo vacio para guardad la diferencia promedio de N1  ( X_Euler - X_Odeint )
diffy_RK4=[]               # Arreglo vacio para guardad la diferencia promedio de N2  ( Y_RK4 - Y_Odeint )
diffx_RK4=[]               # Arreglo vacio para guardad la diferencia promedio de N2  ( X_RK4 - X_Odeint )

Errx_Euler=[]              # Arreglo vacio para guardad la diferencia de N1  (X_Euler - X_Odeint) 
Erry_Euler=[]              # Arreglo vacio para guardad la diferencia de N2  (Y_Euler - Y_Odeint) 
Errx_RK4=[]                # Arreglo vacio para guardad la diferencia de N1  (X_RK4 - X_Odeint) 
Erry_RK4=[]                # Arreglo vacio para guardad la diferencia de N1  (Y_RK4 - Y_Odeint) 

Total_X_Euler=[]           # Arreglo para almazenar soluciones de x para [10,1000,10000,100000] puntos con metodo Euler 
Total_Y_Euler=[]           # Arreglo para almazenar soluciones de y para [10,1000,10000,100000] puntos con metodo Euler 
Total_X_RK4=[]             # Arreglo para almazenar soluciones de x para [10,1000,10000,100000] puntos con metodo RK4 
Total_Y_RK4=[]             # Arreglo para almazenar soluciones de y para [10,1000,10000,100000] puntos con metodo RK4 
Total_N2=[]                # Arreglo para almazenar soluciones de y para [10,1000,10000,100000] puntos con Odeint
Total_N1=[]                # Arreglo para almazenar soluciones de x para [10,1000,10000,100000] puntos con Odeint
Total_T=[]                 # Arreglo para almazenar arreglos  de t para [10,1000,10000,100000] puntos 


for j in Numpuntos:           # Inicia cilco para calcular soluciones con j Numero de puntos en T 
    T=np.linspace(t0,tf,j)     # Se crea un arreglo desde t0 a tf con j numero de puntos

    Y_Euler=[]                # Arreglo para almacenar yn calculada con metodo Euler 
    X_Euler=[]                # Arreglo para almacenar xn calculada con metodo Euler 
    Y_RK4=[]                  # Arreglo para almacenar yn calculada con metodo RK4 
    X_RK4=[]                  # Arreglo para almacenar xn calculada con metodo RK4
    Y_Euler.append(y0)        # Se almacenan valor inicial de y 
    X_Euler.append(x0)        # Se almacenan valor inicial de x 
    Y_RK4.append(y0)          # Se almacenan valor inicial de y 
    X_RK4.append(x0)          # Se almacenan valor inicial de x 
    
    errx_Euler=[]             # Arreglo para guardar el error entre x-Euler con respecto a x-Odeint
    erry_Euler=[]             # Arreglo para guardar el error entre y-Euler con respecto a y-Odeint
    errx_RK4=[]               # Arreglo para guardar el error entre x-RK4 con respecto a x-Odeint
    erry_RK4=[]               # Arreglo para guardar el error entre y-RK4 con respecto a y-Odeint
    
    P0=[1.0,1.5]                 # Condiciones inicales de y,x para Odeint 
    sol = odeint(df_dt, P0, T)     # Uso de Odeint para el sistema acopadlo de EDO
    N2=sol[:,0]                    # Solucion para y (N2)
    N1=sol[:,1]                    # Solucion para x (N1)
    l=1                            # Contador 
    
    for i in T[1:]:         #Comienza ciclo para calcular los j puntos de la solucion de X y Y
        h=(tf-t0)/j         # Paso 
        
        yn_E = Euler(Y_Euler[-1], X_Euler[-1], i, h, F2, F1)[0]        # Caculo yn con Euler
        xn_E = Euler(Y_Euler[-1], X_Euler[-1], i, h, F2, F1)[1]        # Caculo xn con Euler
    
        yn_RK = RK4(Y_RK4[-1], X_RK4[-1], i, h, F2, F1)[0]             # Caculo yn con RK4
        xn_RK = RK4(Y_RK4[-1], X_RK4[-1], i, h, F2, F1)[1]             # Caculo xn con RK4
    
        Y_Euler.append(yn_E)                       # Almacenamiento soluciones y Euler       
        X_Euler.append(xn_E)                       # Almacenamiento soluciones x Euler
    
        Y_RK4.append(yn_RK)                       # Almacenamiento soluciones y RK4 
        X_RK4.append(xn_RK)                       # Almacenamiento soluciones y RK4 

    for l in np.arange(len(N1)):                     # Ciclo para calcular errores de las solucoines con respecto a Odeint
        errx_Euler.append(np.abs(N1[l]-X_Euler[l]))    # Error sol x Euler 
        erry_Euler.append(np.abs(N2[l]-Y_Euler[l]))    # Error sol y Euler 
        errx_RK4.append(np.abs(N1[l]-X_RK4[l]))        # Error sol x RK4
        erry_RK4.append(np.abs(N2[l]-Y_RK4[l]))        # Error sol y RK4
        
    Total_X_Euler.append(X_Euler)       #Almacenamiento de soluciones x_Euler para [10,1000,10000,100000] puntos
    Total_Y_Euler.append(Y_Euler)       #Almacenamiento de soluciones y_Euler para [10,1000,10000,100000] puntos
    Total_X_RK4.append(X_RK4)           #Almacenamiento de soluciones x_RK4 para [10,1000,10000,100000] puntos
    Total_Y_RK4.append(Y_RK4)           #Almacenamiento de soluciones y_RK4 para [10,1000,10000,100000] puntos
    Total_N2.append(N2)                 #Almacenamiento de soluciones y_Odeint para [10,1000,10000,100000] puntos
    Total_N1.append(N1)                 #Almacenamiento de soluciones x_Odeint para [10,1000,10000,100000] puntos
    Total_T.append(T)                   #Almacenamiento de arreglos de t para [10,1000,10000,100000] puntos

    Errx_Euler.append(errx_Euler)       # Almacenamiento errores de x_Euler para [10,1000,10000,100000] puntos
    Erry_Euler.append(erry_Euler)       # Almacenamiento errores de y_Euler para [10,1000,10000,100000] puntos
    Errx_RK4.append(errx_RK4)           # Almacenamiento errores de x_RK4 para [10,1000,10000,100000] puntos
    Erry_RK4.append(erry_RK4)           # Almacenamiento errores de y_RK4 para [10,1000,10000,100000] puntos

    diffx_Euler.append(np.mean(np.abs(N1-X_Euler)))  # Almacenamiento error promedio x_Euler para [10,1000,10000,100000] puntos
    diffy_Euler.append(np.mean(np.abs(N2-Y_Euler)))  # Almacenamiento error promedio y_Euler para [10,1000,10000,100000] puntos
    diffx_RK4.append(np.mean(np.abs(N1-X_RK4)))      # Almacenamiento error promedio x_RK4 para [10,1000,10000,100000] puntos
    diffy_RK4.append(np.mean(np.abs(N2-Y_RK4)))      # Almacenamiento error promedio y_RK4 para [10,1000,10000,100000] puntos

for k in np.arange(len(Numpuntos)):       # Comienza ciclo para graficar 

    fig = plt.figure(figsize=(17, 8))    # Tamano figura
    
    
    ax1 = fig.add_subplot(251)     # Tamano y forma sub-plot 1
    ax2 = fig.add_subplot(252)     # Tamano y forma sub-plot 2
    ax3 = fig.add_subplot(253)     # Tamano y forma sub-plot 3
    ax4 = fig.add_subplot(245)     # Tamano y forma sub-plot 4
    ax5 = fig.add_subplot(246)     # Tamano y forma sub-plot 5
    ax6 = fig.add_subplot(154)     # Tamano y forma sub-plot 6
    ax7 = fig.add_subplot(155)     # Tamano y forma sub-plot 7


    ax1.plot(Total_T[k], Total_X_Euler[k],'y', label= 'Euler')  # Grafica X(t) vs. t con Euler  
    ax1.plot(Total_T[k], Total_X_RK4[k], 'b', label= 'RK4')     # Grafica X(t) vs. t con RK4
    ax1.plot(Total_T[k], Total_N1[k],'g', label= 'Odeint')      # Grafica X(t) vs. t con Odeint
    ax1.grid()                                                  # Cudricula
    ax1.set_title('N1')                                         # Titulo de la grafica
    ax1.set_xlabel('t')                                         # Titulo eje x
    ax1.set_ylabel('N1(t)')                                     # Titulo eje y 
    ax1.legend()                                                # Legend 
    
    ax2.plot(Total_T[k], Total_Y_Euler[k],'y', label= 'Euler')  # Grafica Y(t) vs. t con Euler
    ax2.plot(Total_T[k], Total_Y_RK4[k], 'b', label= 'RK4')     # Grafica Y(t) vs. t con RK4
    ax2.plot(Total_T[k], Total_N2[k],'g', label= 'Odeint')      # Grafica Y(t) vs. t con Odeint
    ax2.grid()                                                  # Cudricula
    ax2.set_title('N2')                                         # Titulo de la grafica
    ax2.set_xlabel('t')                                         # Titulo eje x
    ax2.set_ylabel('N2(t)')                                     # Titulo eje y
    ax2.legend()                                                # Legend 
    
    ax3.plot(Total_X_Euler[k], Total_Y_Euler[k],'y', label= 'Euler')  # Grafica Y(t) vs. X(t) con Euler
    ax3.plot(Total_X_RK4[k], Total_Y_RK4[k], 'b', label= 'RK4')       # Grafica Y(t) vs. X(t) con RK4
    ax3.plot(Total_N1[k], Total_N2[k],'g', label= 'Odeint')           # Grafica Y(t) vs. X(t) con Odeint 
    ax3.grid()                                                        # Cudricula
    ax3.set_title('N1 vs N2')                                         # Titulo de la grafica
    ax3.set_xlabel('N1')                                              # Titulo eje x
    ax3.set_ylabel('N2')                                              # Titulo eje y
    ax3.legend()                                                      # Legend 
    
    ax4.plot(Total_T[k], Errx_Euler[k],'y', label= 'Euler')  # Grafica Error x  vs. t con Euler
    ax4.plot(Total_T[k], Errx_RK4[k], 'b', label= 'RK4')     # Grafica Error x  vs. t con RK4
    ax4.grid()                                               # Cudricula
    ax4.set_title('Error N1')                                # Titulo de la grafica
    ax4.set_xlabel('t')                                      # Titulo eje x
    ax4.set_ylabel('N1')                                     # Titulo eje y
    ax4.legend()                                             # Legend
    
    ax5.plot(Total_T[k], Erry_Euler[k],'y', label= 'Euler')  # Grafica Error y vs. t con Euler 
    ax5.plot(Total_T[k], Erry_RK4[k], 'b', label= 'RK4')     # Grafica Error y vs. t con RK4
    ax5.grid()                                               # Cuadricula 
    ax5.set_title('Error N2')                                # Titulo de la grafica
    ax5.set_xlabel('t')                                      # Titulo eje x
    ax5.set_ylabel('N2')                                     # Titulo eje y 
    ax5.legend()                                             # Legend 
    
    
    ax6.plot(H,diffx_Euler,'y', label= 'Euler')   # Grafica Error medio x  vs. paso (h) con Euler 
    ax6.plot(H,diffx_RK4, 'b', label= 'RK4')      # Grafica Error medio x  vs. paso (h) con RK4 
    ax6.grid()                                    # Cudricula 
    ax6.set_title('Error medio N1')               # Titulo de la grafica 
    ax6.set_xlabel('h')                           # Titulo eje x 
    ax6.set_ylabel('N1')                          # Titulo eje y
    ax6.legend()                                  # Legend
    
    
    ax7.plot(H,diffy_Euler,'y', label= 'Euler')   # Grafica Error medio y  vs. paso (h) con Euler
    ax7.plot(H,diffy_RK4, 'b', label= 'RK4')      # Grafica Error medio y  vs. paso (h) con RK4
    ax7.grid()                                    # Cudricula 
    ax7.set_title('Error medio N2')               # Titulo de la grafica 
    ax7.set_xlabel('h')                           # Titulo eje x 
    ax7.set_ylabel('N2')                          # Titulo eje y
    ax7.legend()                                  # Legend

    plt.show()                                    # Mostrar figura 
    
