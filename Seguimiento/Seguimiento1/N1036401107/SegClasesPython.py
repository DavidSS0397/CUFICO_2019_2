import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

class Particula:
    
    def __init__(self,x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2,carga1,masa1,carga2,masa2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.vx1 = vx1
        self.vy1 = vy1
        self.vz1 = vz1
        self.vx2 = vx2
        self.vy2 = vy2
        self.vz2 = vz2
        self.q1 = carga1
        self.m1 = masa1
        self.q2 = carga2
        self.m2 = masa2
        
    def Movimiento(self,dt):
        Bz = 10.0
        
        F1x = self.q1*(self.vy1*Bz)
        F1y = self.q1*(-self.vx1*Bz)
        F1z = self.q1
        F2x = self.q2*(self.vy2*Bz)
        F2y = self.q2*(-self.vx2*Bz)
        F2z = self.q2
        
        self.x1 = self.x1 + self.vx1*dt + 0.5*(F1x/self.m1)*dt**2
        self.y1 = self.y1 + self.vy1*dt + 0.5*(F1y/self.m1)*dt**2
        self.z1 = self.z1 + self.vz1*dt + 0.5*(F1z/self.m1)*dt**2  
        self.x2 = self.x2 + self.vx2*dt + 0.5*(F2x/self.m1)*dt**2
        self.y2 = self.y2 + self.vy2*dt + 0.5*(F2y/self.m1)*dt**2
        self.z2 = self.z2 + self.vz2*dt + 0.5*(F2z/self.m1)*dt**2
        
        
        
        return X1,X2,Y1,Y2,Z1,Z2
    
dt = 0.01
N = 10000
X1 = []
Y1 = []
Z1 = []
X2 = []
Y2 = []
Z2 = []

particula = Particula(0,0,0,0,0,0,1,0,0,0,0,0,1,10,-1,10)

for i in range(N+1):
    X1.append(particula.x1)
    Y1.append(particula.y1)
    Z1.append(particula.z1)
    X2.append(particula.x2)
    Y2.append(particula.y2)
    Z2.append(particula.z2)
    
    particula.Movimiento(dt)
    

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
#ax = fig.gca(projection="3d")
ax.set_title("Trayectorias")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.text(0.2,0.1,-0,"$\\uparrow\\, \\vec{B}$",color="red")
ax.plot(X1,Y1,Z1)
ax.plot(X2,Y2,Z2)
