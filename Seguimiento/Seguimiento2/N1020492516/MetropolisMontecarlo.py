###     Montecarlo
import matplotlib.pyplot as plt
from scipy import integrate
import random

N=[100,1000,10000]

def f1(x):
    return x**(-3)
def f2(x):
    return x**(-0.5)
def f3(x,y,z):
    return (1/x) + y + z**2

If1=integrate.quad(f1,1,10)
If2=integrate.quad(f2,1,10)
#If3=integrate.quad(f3,1,10,0,2,0,2)
xi = [1,0,0]
xf = [10,2,2]

def montd1(N,f,xi,xf):
    suma1 = 0
    suma2 = 0
    ##para E##
    for i in range(0,N):
        xn = (xf-xi)*random.random()+xi
        #yn = (yf-yi)*random.random()+yi
        #zn = (zf-zi)*random.random()+zi
        suma1 +=f(xn)
        E = (1/N)*suma1
        
        suma2 +=(f(xn))**2 - E**2
        S2 = (1/N)*suma2
        
    return (xf-xi)*E,(xf-xi)*S2

def montd2(N,f,xi,yi,zi,xf,yf,zf):
    suma1 = 0
    suma2 = 0
    ##para E##
    for i in range(0,N):
        xn = (xf-xi)*random.random()+xi
        yn = (yf-yi)*random.random()+yi
        zn = (zf-zi)*random.random()+zi
        suma1 +=f(xn,yn,zn)
        E = (1/N)*suma1
        
        suma2 +=(f(xn,yn,zn))**2 - E**2
        S2 = (1/N)*suma2
        
    return (xf-xi)*(yf-yi)*(zf-zi)*E,(xf-xi)*(yf-yi)*(zf-zi)*S2

###OJOOOO con el reescalamiento. Para 3 dimensiones es un volumen o algo así.
x1 = [0.]*len(N)
EG1 =[]
SG1 =[]
x2 = [0.]*len(N)
EG2 =[]
SG2=[]
x3 = [0.]*len(N)
EG3 =[]
SG3=[]
print('Integral f1:',If1)
for i in range(0,len(N)):
    x1[i]=(montd1(N[i],f1,1,10))
    print(x1[i][0],N[i])
    EG1.append(x1[i][0])
    SG1.append(x1[i][1])

print('Integral f2:',If2)
for i in range(0,len(N)):
    x2[i]=(montd1(N[i],f1,1,10))
    print(x2[i][0],N[i])
    EG2.append(x2[i][0])
    SG2.append(x2[i][1])

print('Integral f3:')
for i in range(0,len(N)):
    x3[i]=(montd2(N[i],f3,1,0,0,10,2,2))
    print(x3[i][0],N[i])
    EG3.append(x3[i][0])
    SG3.append(x3[i][1])

fig, ([ax1,ax2,ax3],[ax4,ax5,ax6]) = plt.subplots(2,3)#filas, columnas

ax1.plot(N,EG1,'r--',label='x^-3')
ax2.plot(N,EG2,label='x^-1/2')
ax3.plot(N,EG3,label='3D')
ax4.plot(N,SG1,'r--',label='x^-3')
ax5.plot(N,SG2,label='x^-1/2')
ax6.plot(N,SG3,label='3D')

ax1.grid()
ax1.set_title('x^3')
ax1.set_xlabel('N')
ax1.set_ylabel('E')
ax4.set_xlabel('N')
ax4.set_ylabel('S')
ax2.grid()
ax2.set_title('x^-1/2')
ax3.grid()
ax3.set_title('3D')
plt.tight_layout()
plt.show()


### Metropolis


import numpy as np
from numpy import pi
import random
import matplotlib.pyplot as plt

def P(x):
    mu = 0
    sigma = 0.1
    p= (1/(sigma*np.sqrt(2*pi)))*np.exp(-(x-mu)**2/(2*sigma**2))
    return p


x=[]
xa=[]
x.append(2*pi*random.random()-pi)
for i in range(0,10000):
    xp = 2*pi*random.random()-pi
    ds = -np.log(P(xp)/P(x[-1]))
    if ds<0:
        x.append(xp)
    elif ds > 0:
        xnada = random.random()
        Pg = P(xp)/P(x[-1])
        if xnada < Pg:
                 x.append(xp)

plt.hist(x,bins=30)
plt.xlim(-3,3)
plt.grid()
plt.show()
