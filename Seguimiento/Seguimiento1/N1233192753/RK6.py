import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

Data=np.loadtxt('Datos_RK.txt')                     # Importacion de datos

X1=Data[0:10,0]                                      # NumPuntos = 10 
X2=Data[11:111,0]                                    # NumPuntos = 100   
X3=Data[112:1112,0]                                  # NumPuntos = 1000  
X4=Data[1113:11113,0]                                # NumPuntos = 10000 

Y1=Data[0:10,1]                                      # NumPuntos = 10
Y2=Data[11:111,1]                                    # NumPuntos = 100
Y3=Data[112:1112,1]                                  # NumPuntos = 1000
Y4=Data[1113:11113,1]                                # NumPuntos = 10000

def MyFirstODE(y, x):             # Ecuacion diferencial
    return x-y

def ExactSolution(x):             # Solucion Exacta 
    return x-1+2*np.exp(-x)

NumPuntos = np.array([10,100,1000,10000]) 
x0=0.0                                      # Condiones iniciales 
xf=5.0
y0=1.0
h=(xf-x0)/NumPuntos                         # Paso

TotalDiffYS1 = []                     # Arreglos para guardar resultados
TotalDiffRK1 = []
TotalDiffYS2 = []
TotalDiffRK2 = []
TotalDiffYS3 = []
TotalDiffRK3 = []  
TotalDiffYS4 = []
TotalDiffRK4 = []

XS1=np.linspace(0,5,10)                #Arreglos de valores de x
XS2=np.linspace(0,5,100)
XS3=np.linspace(0,5,1000)
XS4=np.linspace(0,5,10000)

ys1 = odeint(MyFirstODE, y0, XS1)      # Solucion Odeint NumPuntos = 10
ys1 = np.array(ys1).flatten()

ys2 = odeint(MyFirstODE, y0, XS2)      # Solucion Odeint NumPuntos = 100
ys2 = np.array(ys2).flatten()

ys3 = odeint(MyFirstODE, y0, XS3)      # Solucion Odeint NumPuntos = 1000
ys3 = np.array(ys3).flatten()

ys4 = odeint(MyFirstODE, y0, XS4)      # Solucion Odeint NumPuntos = 10000
ys4 = np.array(ys4).flatten()

EY1 = ExactSolution(X1)            # Solucion exacta NumPuntos = 10
EY2 = ExactSolution(X2)            # Solucion exacta NumPuntos = 100
EY3 = ExactSolution(X3)            # Solucion exacta NumPuntos = 1000
EY4 = ExactSolution(X4)            # Solucion exacta NumPuntos = 10000

EYS1 = ExactSolution(XS1)
EYS2 = ExactSolution(XS2)
EYS3 = ExactSolution(XS3)
EYS4 = ExactSolution(XS4)

for i1 in xrange(len(X1)):                       # Calculo errores NumPuntos = 10
    
    TotalDiffYS1.append(np.abs(ys1[i1]-EYS1[i1]))
    TotalDiffRK1.append(np.abs(Y1[i1]-EY1[i1]))
ys1_difference=np.mean(np.abs(ys1-EYS1))
y1_difference=np.mean(np.abs(Y1-EY1))    
    
for i2 in xrange(len(X2)):                        # Calculo errores NumPuntos = 100
    
    TotalDiffYS2.append(np.abs(ys2[i2]-EYS2[i2]))
    TotalDiffRK2.append(np.abs(Y2[i2]-EY2[i2]))
ys2_difference=np.mean(np.abs(ys2-EYS2))                    
y2_difference=np.mean(np.abs(Y2-EY2)) 

for i3 in xrange(len(X3)):                         # Calculo errores NumPuntos = 1000
    
    TotalDiffYS3.append(np.abs(ys3[i3]-EYS3[i3]))
    TotalDiffRK3.append(np.abs(Y3[i3]-EY3[i3]))
ys3_difference=np.mean(np.abs(ys3-EYS3))
y3_difference=np.mean(np.abs(Y3-EY3))    
      
for i4 in xrange(len(X4)):                         # Calculo errores NumPuntos = 10000
    
    TotalDiffYS4.append(np.abs(ys4[i4]-EYS4[i4]))
    TotalDiffRK4.append(np.abs(Y4[i4]-EY4[i4]))
ys4_difference=np.mean(np.abs(ys4-EYS4))
y4_difference=np.mean(np.abs(Y4-EY4))        

HS=[ys1_difference, ys2_difference, ys3_difference, ys4_difference]
HY=[y1_difference, y2_difference, y3_difference, y4_difference]

fig, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(10, 6))  # Graficas


ax1.plot(X1, Y1,'g', label='RK6')
ax1.plot(XS1, ys1,'m', label= 'Odeint')
ax1.plot(X1, EY1,'k', label= 'Solucion Exacta')
ax1.grid()
ax1.legend()
ax1.set_title('10 Puntos')


ax2.semilogy(X1, TotalDiffRK1, 'g', label='RK6')
ax2.semilogy(XS1, TotalDiffYS1, 'm', label= 'Odeint')
ax2.grid()
ax2.legend()
ax2.set_title('10 Puntos')


ax3.plot(h,HY, 'g', label='RK6')
ax3.plot(h,HS, 'm', label= 'Odeint')
ax3.grid()
ax3.legend()
ax3.set_title('10 Puntos')

fig2, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(10, 6))

ax1.plot(X2, Y2, 'g', label='RK6')
ax1.plot(XS2, ys2, 'm', label= 'Odeint')
ax1.plot(X2, EY2, 'k', label= 'Solucion Exacta')
ax1.grid()
ax1.legend()
ax1.set_title('100 Puntos')


ax2.semilogy(X2, TotalDiffRK2, 'g', label='RK6')
ax2.semilogy(XS2, TotalDiffYS2, 'm', label= 'Odeint')
ax2.grid()
ax2.legend()
ax2.set_title('100 Puntos')


ax3.plot(h,HY, 'g', label='RK6')
ax3.plot(h,HS, 'm', label= 'Odeint')
ax3.grid()
ax3.legend()
ax3.set_title('100 Puntos')

fig3, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(10, 6))

ax1.plot(X3, Y3, 'g', label='RK6')
ax1.plot(XS3, ys3, 'm', label= 'Odeint')
ax1.plot(X3, EY3, 'k', label= 'Solucion Exacta')
ax1.grid()
ax1.legend()
ax1.set_title('1000 Puntos')


ax2.semilogy(X3, TotalDiffRK3, 'g', label='RK6')
ax2.semilogy(XS3, TotalDiffYS3, 'm', label= 'Odeint')
ax2.grid()
ax2.legend()
ax2.set_title('1000 Puntos')


ax3.plot(h,HY, 'g', label='RK6')
ax3.plot(h,HS, 'm', label= 'Odeint')
ax3.grid()
ax3.legend()
ax3.set_title('1000 Puntos')

fig4, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(10, 6))

ax1.plot(X4, Y4, 'g', label='RK6')
ax1.plot(XS4, ys4, 'm', label= 'Odeint')
ax1.plot(X4, EY4, 'k', label= 'Solucion Exacta')
ax1.grid()
ax1.legend()
ax1.set_title('10000 Puntos')


ax2.semilogy(X4, TotalDiffRK4, 'g', label='RK6')
ax2.semilogy(XS4, TotalDiffYS4, 'm', label= 'Odeint')
ax2.grid()
ax2.legend()
ax2.set_title('10000 Puntos')


ax3.plot(h,HY, 'g', label='RK6')
ax3.plot(h,HS, 'm', label= 'Odeint')
ax3.grid()
ax3.legend()
ax3.set_title('10000 Puntos')


plt.show()
