import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Se cargan los datos
d = np.loadtxt('data_rk6.txt')

#Condiciones iniciales
x0 = 0.0
xf = 5.0
y0 = 1.0

#Numero de puntos y paso
n = np.array([10, 100, 1000, 10000])
h = (xf-x0)/n

df = lambda y, x: x-y            #Ec. Diferencial
f = lambda x: x-1+2*np.exp(-x)   #Solucion exacta

#Arreglo para cargar los valores de RK6
X = []
Y_RK6 = []

#Separacion de los valores para cada h
li=0
lf=0
for i in range(0, 4):
    lf=li+(n[i])+1  
    X.append(d[li:lf, 0])
    Y_RK6.append(d[li:lf, 1])
    li=lf

#Calculo de    
Y_Ex = [f(X[i]).flatten() for i in range(0, 4)]                                   #Solucion exacta
Y_odeint = [odeint(df, y0, X[i]).flatten() for i in range(0, 4)]                  #Solucion de odeint 
Y_Diff = np.abs(np.array(Y_RK6) - np.array(Y_Ex))                                 #Diferencia con Y de RK6 con solucion exacta
Y_diff_odeint = np.abs(np.array(Y_odeint) - np.array(Y_Ex))                       #Diferencia con Y de odeint con solucion exacta
Y_difference = [np.mean(np.abs(Y_RK6[i]-Y_Ex[i])) for i in range(0, 4)]           #Media de la diferencia de Y de RK6 con solucion exacta
Y_odeint_difference = [np.mean(np.abs(Y_odeint[i]-Y_Ex[i])) for i in range(0, 4)] #Media de la diferencia de Y de odeint con solucion exacta

#Grafica
label = ['10 pts', '100 pts', '1000 pts', '10000 pts']

for i in range(0, 4):
    fig = plt.figure(figsize = (12, 4))

    ax0 = fig.add_subplot(131)
    ax1 = fig.add_subplot(132)
    ax2 = fig.add_subplot(133)

    ax0.plot(X[1], Y_Ex[1], 'k-', label = 'Exacta')
    ax0.plot(X[i], Y_RK6[i], 'r-', label = label[i])
    ax0.plot(X[i], Y_odeint[i], 'g--',  label = 'Odeint')
    ax0.set_title("Solucion a EDO")
    
    ax1.semilogy(X[i], Y_Diff[i], 'r--', label = label[i])
    ax1.semilogy(X[i], Y_diff_odeint[i], 'g--', label = 'Odeint')
    ax1.set_title("Diferencia con la solucion exacta")
    
    ax2.semilogy(h, Y_difference, 'r--', label = 'RK6')
    ax2.semilogy(h, Y_odeint_difference, 'g--',  label = 'Odeint')
    ax2.set_title("Paso vs Media del error")
    
    ax0.legend()
    ax1.legend()
    ax2.legend()

    ax0.grid()
    ax1.grid()
    ax2.grid()

    #plt.savefig("RK6_"+str(i)+".png")
    plt.show()
