'''
! ===========================================================================
! SegClasesPython.py
! ===========================================================================
! This program describes the interaction between two charged particles and 
! they are in a magnetic field.
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co

! Up to date: 22 agosto 2019			
'''

# Librarys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

class Particle:

  def __init__(self,r,v,m,carga):

    self.r = r
    self.v = v
    self.m = m
    self.q = carga
  
  def cinematica(self,Fuerza,q_prima,r2,B,dt):
    F = Fuerza(self.r,self.v,self.q,q_prima,B,r2)
    
    a = F/self.m
    self.v = a*dt+self.v
    self.r = a*dt**2/2.+self.v*dt+self.r
    
    return self.r

def FuerzaLorentz(r,v,q,q_prima,B,r2):
	k = 9e9
	F = q*(np.cross(v,B)+k*q_prima*(r-r2)/(np.sum((r-r2)**2))**3/2)
	return F

#Initial conditions
r1 = np.array([0,0,0]) #Initial position for particle 1
r2 = np.array([1,0,0]) #Initial position for particle 2
v1 = np.array([0,0,0]) #Initial velocity for particle 1
v2 = np.array([0,0,0]) #Initial velocity for particle 2

m = 10 #Mass 
B = np.array([0,0,10]) #Magentic field
q1 = 1 #Charge for particle 1
q2 = -1 #Charge for particle 2

part1 = Particle(r1,v1,m,q1) #Particle 1
part2 = Particle(r2,v2,m,q2) #Particle 2

dt = 0.01 #Time step

R1 = part1.r
R2 = part2.r

#Evolution in time
for i in range(0,10000):
  r1_temp = part1.cinematica(FuerzaLorentz, part2.q, r2,B,dt)
  r2_temp = part2.cinematica(FuerzaLorentz, part1.q, r1,B,dt)
  
  r1 = r1_temp
  r2 = r2_temp
  R1 = np.append(r1,R1)
  R2 = np.append(r2,R2)

R1 = np.reshape(R1,(-1,3))
R2 = np.reshape(R2,(-1,3))

#Graphs
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1,2,1,projection='3d')

ax.plot(R2[:,0], R2[:,1], R2[:,2],'g', label='Particula2')
ax.plot(R1[:,0], R1[:,1], R1[:,2],'k', label='Particula1')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Interaccion entre las 2 particulas')
ax.legend(loc=4)

plt.subplot(1,2,2)
plt.plot(R2[:,0], R2[:,1],'g', label='Particula2')
plt.plot(R1[:,0], R1[:,1],'k', label='Particula1')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Proyeccion en el plano XY del movimiento')

plt.savefig('SegClasesPython.png')
plt.show()