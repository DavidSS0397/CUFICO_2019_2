
# coding: utf-8

# In[215]:

#Se importan las librerias
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'pylab inline')


# In[216]:

#Se crea la clase particle
class Particle:
    #Se inicializan los atributos
    def __init__(self, x, y, z, vx, vy, vz, m, carga):
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.M = m
        self.Carga = carga
        self.vox=vx
        self.voy=vy
        self.voz=vz
        self.xo=x
        self.yo=y
        self.zo=z
    #Metodo para calcular posiciones
    def get_positions(self, Fx, Fy, Fz, t):
        self.X = (Fx*t*t)/(2.*self.M) + self.vox*t + self.xo
        self.Y = (Fy*t*t)/(2.*self.M) + self.voy*t + self.yo
        self.Z = (Fz*t*t)/(2.*self.M) + self.voz*t + self.zo
        return [self.X, self.Y, self.Z]
    #Metodo para calcular velocidades
    def get_velocities(self, Fx, Fy, Fz, t):
        self.VX = Fx*t/self.M + self.vox
        self.VY = Fy*t/self.M + self.voy
        self.VZ = Fz*t/self.M + self.voz
        return [self.VX, self.VY, self.VZ]
    #Metodo para calcular aceleraciones
    def get_acelerations(self, Fx, Fy, Fz, t):
        self.ax = Fx/self.M
        self.ay = Fy/self.M
        self.az = Fz/self.M
        return [self.ax, self.ay, self.az]


# In[217]:

#Calculo de fuerzas
#Fuerza magnetica
def Fmag(q, v, phi, theta, Bx, By, Bz):
    vx = v*np.sin(theta)*np.cos(phi)
    vy = v*np.sin(theta)*np.sin(phi)
    vz = v*np.cos(theta)
    Fx = q*(vy*Bz - vz*By)
    Fy = -q*(vx*Bz - vz*Bx)
    Fz = q*(vx*By - vy*Bx)
    return [Fx, Fy, Fz]
#Fuerza electrica
def Felec(q1, q2, R1, R2):
    r2 = np.sum([(R2[i]-R1[i])**2 for i in range(0, len(R1))])
    Fx = q2*q1*(R2[0]-R1[0])/(r2)**3/2
    Fy = q2*q1*(R2[1]-R1[1])/(r2)**3/2
    Fz = q2*q1*(R2[2]-R1[2])/(r2)**3/2
    return [Fx, Fy, Fz]
#Fuerza de Lorentz
def FLorentz(q2, q1, R1, R2, v, phi, theta, Bx, By, Bz):
    FX = Felec(q2, q1, R1, R2)[0] + Fmag(q1, v, phi, theta, Bx, By, Bz)[0]
    FY = Felec(q2, q1, R1, R2)[1] + Fmag(q1, v, phi, theta, Bx, By, Bz)[1]
    FZ = Felec(q2, q1, R1, R2)[2] + Fmag(q1, v, phi, theta, Bx, By, Bz)[2]
    return [FX, FY, FZ]


# In[218]:

#Constantes
m = 10 #Masa
q = 1  #Carga particula 1
q2 = -1 #Carga particula 1
B = [0, 0, 10]

#Condiciones iniciales en t=0
vxo, vyo, vzo = 5, 0, 0
v = (vxo**2 + vyo**2 + vzo**2)**1/2
phi = 0
theta = np.pi/6
R2 = [1, 0, 0]     #Posiciones iniciales
R1 = [0, 0, 0]     #Posiciones iniciales  


# In[219]:

P1 = Particle(*R1, vxo, vyo, vzo, m, q)
P2 = Particle(*R2, vxo, vyo, vzo, m, q2)
x2=[]; y2=[]; z2=[]
x1=[]; y1=[]; z1=[]
#Iteración de la fuerza para encontrar la posicion
for t in np.arange(0.0, 50, 0.01):
    phi = q*B[2]*t/m
    F1 = FLorentz(q2, q, R1, R2, v, phi, theta, *B)
    F2 = FLorentz(q, q2, R2, R1, v, phi, theta, *B)
    R_1 = P1.get_positions(*F1, t)
    R_2 = P2.get_positions(*F2, t)
    x1.append(R_1[0])
    y1.append(R_1[1])
    z1.append(R_1[2])
    R1 = [R_1[0], R_1[1], R_1[2]]
    x2.append(R_2[0])
    y2.append(R_2[1])
    z2.append(R_2[2])
    R2 = [R_2[0], R_2[1], R_2[2]]


# In[220]:

from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()

x1=np.array([x1])
y1=np.array([y1])
z1=np.array([z1])

x2=np.array([x2])
y2=np.array([y2])
z2=np.array([z2])

ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(x1, y1, z1, c='b', marker='o')
ax1.scatter(x2, y2, z2, c='k', marker='o')
plt.savefig('SegClasesPython.png')
plt.show()


# In[ ]:



