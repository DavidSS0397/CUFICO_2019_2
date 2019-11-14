import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random 
from scipy import integrate

#Integrales unidimensionales

a = 1    #Límite inferior
b = 10   #límite superior

N = [10,1000,10000]

def F(x):  
    return x**(-3)
def F1(x):
    return x**(-0.5)

Integral = integrate.quad(F,1,10)       #Integral de la función 1
Integral1 = integrate.quad(F,1,10)      #Integral de la función 2

def MonteCarlo(a,b,f,N):
    I = 0
    I1 = 0
    S = 0
    S1 = 0
    for i in range(N):
    
        x = (b-a)*random() + a   #Genera un número aleatorio en el intervalo (a,b)
        x1 = (b-a)*random() + a
        
        I = I + F(x)        # Integral de Monte Carlo para F(x)
        I1 = I1 + F1(x)     # Integral de MOnte Carlo para F1(x)
    
        E = (1/N)*I         # Muestreo aleatorio de F
        E1 = (1/N)*I1       # Muestreo aleatorio de F1
    
        S = S + F(x)**2 - E**2     
        S1 = S1 + F1(x)**2 - E**2      
    
        S_2 = (1/N)*S            # Información aproximada del error del metodo para F
        S_21 = (1/N)*S1          # Información aproximada del error del metodo para F1
        
    return (b-a)*E, (b-a)*E1, (b-a)*S_2, (b-a)*S_21
    
#x = np.zeros(N)
#x1 = np.zeros(N)

E = []
S = []
E1 = []
S1 = []
    
for i in range(0,len(N)):
    x = MonteCarlo(a,b,F,N[i])
    E.append(x[0])
    S.append(x[2])

for i in range(0,len(N)):
    x1 = MonteCarlo(a,b,F1,N[i])
    E1.append(x[1])
    S1.append(x[3])
    
    
plt.plot(N,E)
plt.plot(N,S)
plt.plot(N,E1)
plt.plot(N,S1)
plt.show()

#Integrales tridimensionales

a = 1    #Límite inferior para x
b = 10   #límite superior para y
c = 0    #límite inferior para y,z
d = 2    #límite superior para y,z

N = [100, 1000, 10000]

def F(x,y,z):
    return 1/x + y + z**2

def MonteCarlo(a,b,c,d,F,N):
    I = 0
    S = 0
    
    for i in range(N):
    
        x = (b-a)*random() + a   #Genera un número aleatorio en el intervalo (a,b)
        y = (d-c)*random() 
        z = (d-c)*random()
    
        I = I + F(x,y,z)
    
        E = (1/N)*I
        S = S + (F(x,y,z))**2 - E**2
        S_2 = (1/N)*S
        
    return (b-a)*(d-c)**2*E , (b-a)*(d-c)**2*S_2


E = []
S = []

for i in range(0,len(N)):
    x = MonteCarlo(a,b,c,d,F,N[i])
    E.append(x[0])
    S.append(x[1])

plt.plot(N,E)
plt.plot(N,S)
plt.show()

# Metropolis

def P(x):      # Defino la probabilidad en el experimento de Rutherfor
    u = 0
    sigma = 0.1
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-u)**2/(2*sigma**2))

x = []
x.append(np.random.random())  # Genero aleatoriamente un estado inicial


for i in range(0,1000):            # Genero 1000 eventos
    x1 = np.random.random()        # Genero una siguiente variable aleatoria
    ds = -np.log(P(x1)/P(x[-1]))   # Calculo delta de S
    if ds < 0:                     # Si ds<0 mi variable es igual a la segunda variable aleatoria que cree
        X.append(x1)
    elif ds > 0:                   # Si es menor que 0
        xnuevo = np.random.random()   # Vuelve a crear otra variable aleatoria hasta que se cumpla la condición
        Pnuevo = P(x1)/P(x[-1])
        if xnuevo < Pnuevo:
            X.append(x1)
            
plt.hist(x,bins=20)      # Grafico theta en un histograma.
plt.show()
