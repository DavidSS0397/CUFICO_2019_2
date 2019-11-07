import matplotlib.pyplot as plt
import numpy as np

#Se compara la solucion analitica con la hallada por Runge Kutta 
def ED(x):
    return x-1+2*np.exp(-x)


x,y = np.loadtxt('RK6.txt', unpack=True)

X=np.linspace(0.,5.,100000)
#plt.plot(X,ED(X),'r')
plt.plot(x,y,'b')

plt.xlabel('x')
plt.ylabel('y')


plt.show()
