"""
! ===========================================================================
! interaccion.py
! ===========================================================================
! 
!   Este programa soluciona de manera numerica la evolucion de la interaccion
!   entre dos gases que solo interacturan entre ellos.
!   Se usa el metodo de Euler y el de RK4 y ademas se usa Odeint como solucion
!   exacta. 
!
!     Carolina Herrera Segura, carolina.herreras@udea.edu.co    
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co
!
! Up to date: 29 septiembre 2019            
"""

#Librerias
import numpy as np # Libreria para operaciones. De aqui se usan arreglos
import matplotlib.pyplot as plt # Libreria para graficas
from scipy.integrate import odeint # Libreria para resolver EDO numericamente

# Runge Kutta 4 para sistema de dos EDO acopladas
def runge_kutta_4(yn, t, h, ode_system):
    # yn: arreglo de numpy con xn y yn
    # t: parametro
    # h: tamano de paso
    # ode_system: arreglo con sistema de ecuaciones acopladas
    
    # Coeficientes para el método de RK4
    k1 = h*ode_system(yn,t) # Coeficiente k1
    k2 = h*ode_system(yn+h*k1/2,t+0.5*h) # Coeficiente k2
    k3 = h*ode_system(yn+h*k2/2,t+0.5*h) # Coeficiente k3
    k4 = h*ode_system(yn+h*k3, t+h) # Coeficiente k4
    
    # Retorna arreglo yn actualizado
    return yn+(k1+2*k2+2*k3+k4)/6.


# Metodo de Euler para sistema de dos EDO acopladas
def euler(yn, t, h, ode_system):
    # yn: arreglo de numpy con xn y yn
    # t: parametro
    # h: tamano de paso
    # ode_system: arreglo con sistema de ecuaciones acopladas
    
    # Se define el valor numerico de las EDO
    dy1, dy2 = ode_system(yn, t)
    
    # Se actualizan las entradas de yn
    yn[0] += h*dy1 # Actualizacion de yn
    yn[1] += h*dy2 # Actualizacion de xn
   
    # Retorna arreglo yn actualizado
    return yn


# Sistema de ecuaciones acopladas
def interaction(n, t):
    # n: arreglo de numpy con valores de n1 y n2
    # t: parametro
    
    # Constantes de las ecuaciones son la misma en este caso
    a = b = c = d = 1
    
    # Se determina valor numerico de cada EDO
    dn2 = -n[1]*(c-d*n[0]) # Ecuacion de movimiento de n2 
    dn1 = n[0]*(a-b*n[1]) # Ecuacion de movimiento de n1
    
    # Retorna arreglo con valor numerico de cada EDO en diferentes entradas
    return np.array([dn1,dn2])


# ------ Parametros y condiciones iniciales ------

t0, tf = 0, 12 # t inicial y final
n01, n02 = 1.5, 1. # Condiciones iniciales para n1 y n2

# Definimos arreglo con valores iniciales de n1 y n2
n0 = np.array([n01, n02])

# Arreglo con numero de pasos que se usara para solucionar las EDO
num_steps = np.array([10, 100, 1000, 10000])

# Listas donde se guardaran las soluciones de cada metodo para cada
# valor de num_steps
total_solutions_RK4 = [] # Metodo de RK4
total_solutions_Euler = [] # Metodo de Euler
total_solutions_Odeint = [] # Metodo de Odeint 

# Listas donde se guardaran las diferencias de cada metodo con la
# solucion de Odeint para evaluar convergencia
difference_RK4 = [] # Metodo de RK4
difference_Euler = [] # Metodo de Euler


# Ciclo sobre numero de puntos
for n in num_steps:
    
    # Arreglo con n numero de puntos en el intervalo [t0, tf]
    steps = np.linspace(t0, tf, n)
    h = (tf-t0)/n # Tamaño del paso
    
    # Arreglos donde se agregaran soluciones a las EDO con cada metodo.
    # Ambos son arreglos de arreglos que guardan cada solucion [n1, n2]
    # en cada paso t del siguiente ciclo
    N_RK4 = np.array([n0]) # Metodo de RK4
    N_Euler = np.array([n0]) # Metodo de Euler
    
    # Ciclo para evolucion temporal
    for t in steps[:-1]:
        
        # Arreglos con soluciones de n1 y n2 luego a aplicar respectivo metodo
        solutions_RK4 = runge_kutta_4(N_RK4[-1], t, h, interaction) # Metodo de RK4
        solutions_Euler = euler(N_Euler[-1], t, h, interaction) # Metodo de Euler
        
        # Se actualizan arreglos con anterior solucion para respectivo metodo
        N_RK4 = np.append(N_RK4, [solutions_RK4], axis = 0) # Metodo de RK4
        N_Euler = np.append(N_Euler, [solutions_Euler], axis = 0) # Metodo de Euler
    
    # Arreglo con la solucion a las EDO utilizando Odeint
    N_Odeint = odeint(interaction, n0, steps)
    
    # Se agrega solucion obtenida en ciclo anterior.
    # Estas listas tienen tres dimensiones: la primera corresponde al
    # numero de puntos, mientras que las otras dos son el arreglo de
    # soluciones [n1, n2]
    total_solutions_Odeint.append(N_Odeint) # Metodo de Odeint
    total_solutions_RK4.append(N_RK4) # Metodo de RK4
    total_solutions_Euler.append(N_Euler) # Metodo de Euler
    
    # Se agrega promedio de valor absoluto de diferencias para evaluar
    # convergencia
    difference_RK4.append(np.mean(np.abs(N_Euler-N_Odeint))) # Metodo de RK4
    difference_Euler.append(np.mean(np.abs(N_RK4-N_Odeint))) # Metodo de Euler
    
    
time = [np.linspace(t0, tf, n) for n in num_steps] # Arreglos con los tiempos para diferente numero de pasos
h = (tf-t0)/num_steps  # Arreglo con los diferentes tamanos de pasos

#--------- Graficas de los resultados ---------

plt.figure(figsize=[21,7]) # Figura con los resultados
plt.suptitle('Solucion para %d puntos'%num_steps[-1]) # Titulo de la figura

plt.subplot(131) # Grafica de n1 vs t para diferentes metodos
plt.plot(time[-1],total_solutions_Odeint[-1][:,0],'k',label = 'Odeint') # Solucion con odeint 
plt.plot(time[-1],total_solutions_Euler[-1][:,0],'m',label = 'Euler') # Solucion con Euler
plt.plot(time[-1],total_solutions_RK4[-1][:,0],'g--',label = 'RK4') # Solucion con RK4
plt.grid() # Cuadricula en la grafica
plt.xlabel('Tiempo') #Nombre del eje x
plt.ylabel('n1') # Nombre del eje y
plt.legend() # Activa los indicadores de cada grafica
plt.title('n1 vs. t') # Titulo de la grafica

plt.subplot(132) # Grafica de n2 vs t para diferentes metodos
plt.plot(time[-1],total_solutions_Odeint[-1][:,1],'k',label = 'Odeint') # Solucion con odeint
plt.plot(time[-1],total_solutions_Euler[-1][:,1],'m',label = 'Euler') # Solucion con Euler
plt.plot(time[-1],total_solutions_RK4[-1][:,1],'g--',label = 'RK4') # Solucion con RK4
plt.grid() # Cuadricula en la grafica
plt.xlabel('Tiempo') # Nombre del eje x
plt.ylabel('n2') # Nombre del eje y
plt.legend() # Activa los indicadores de cada grafica
plt.title('n2 vs. t') # Titulo de la grafica

plt.subplot(133) # Grafica de n2 vs n1 para diferentes metodos
plt.plot(total_solutions_Odeint[-1][:,0],total_solutions_Odeint[-1][:,1],'k',label = 'Odeint') # Solucion con odeint
plt.plot(total_solutions_Euler[-1][:,0],total_solutions_Euler[-1][:,1],'m',label = 'Euler') # Solucion con Euler
plt.plot(total_solutions_RK4[-1][:,0],total_solutions_RK4[-1][:,1],'g--',label = 'RK4') # Solucion con RK4
plt.grid() # Cuadricula en la grafica
plt.xlabel('n1') # Nombre del eje x
plt.ylabel('n2') # Nombre del eje y
plt.legend() # Activa los indicadores de cada grafica
plt.title('n2 vs. n1') # Titulo de la grafica

plt.show() # Muestra la figura

plt.plot(h, difference_RK4, 'k--') # Grafica de las diferencias para RK4 punteada
plt.plot(h, difference_RK4, 'or',label='RK4') # Grafica de los puntos de  las diferencias de RK4
plt.plot(h, difference_Euler, 'k--') # Grafica de las diferencias para Euler punteada
plt.plot(h, difference_Euler, 'og',label='Euler') # Grafica de los puntos de  las diferencias de Euler
plt.grid() # Cuadricula en la grafica
plt.legend() # Activa los indicadores de cada grafica
plt.title('Convergencia') # Titulo de la grafica
plt.xlabel('Tamano de paso') # Nombre del eje x

plt.show() # Muestra la figura
