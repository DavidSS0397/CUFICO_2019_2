import numpy as np
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class Particula:
    cargada = True
    def __init__(self, x, y, z, vx, vy, vz, carga, masa):
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.C = carga
        self.M = masa    

    def Radio(self, Particle):
	return ( (self.X - Particle.X)**2 +
	         (self.Y - Particle.Y)**2 + 
	         (self.Z - Particle.Z)**2 )**0.5
    def Posicion(self, x, v, a, t):
	return x + (v*t) + (0.5*a*t**2)
		
    def Velocidad(self, v, a, t):
	return v + a*t

    def Evolucion(self, Fx, Fy, Fz, t):
        self.X = self.Posicion(self.X, self.VX, Fx/self.M, t)
	self.Y = self.Posicion(self.Y, self.VY, Fy/self.M, t)
	self.Z = self.Posicion(self.Z, self.VZ, Fz/self.M, t)
	self.VX = self.Velocidad(self.VX, Fx/self.M, t)
	self.VY = self.Velocidad(self.VY, Fy/self.M, t)
	self.VZ = self.Velocidad(self.VZ, Fz/self.M, t)


cte = 1 / ( 4 * np.pi * 8.85e-12)
B = (0,0,10)
i = 0
dt = 0.01

p1 = Particula(0., 0., 0., 0., 0., 0., 1., 10. )
p2 = Particula(1., 0., 0., 0., 0., 0., -1., 10. )

Posicion1 = [[p1.X], [p1.Y], [p1.Z]]
Posicion2 = [[p2.X], [p2.Y], [p2.Z]]

def Campo(part1, part2):  
    
    r = part1.Radio(part2)

    Ex = part1.C * (part2.X - part1.X) * cte / r**3
    Ey = part1.C * (part2.Y - part1.Y) * cte / r**3
    Ez = part1.C * (part2.Z - part1.Z) * cte / r**3
	
    return [Ex, Ey, Ez]

def Fuerza(part1, part2, dt):
    
    Fx = part1.C * ( Campo(part2,part1)[0] + (part1.VY * B[2] - part1.VZ * B[1]) )
    Fy = part1.C * ( Campo(part2,part1)[1] + (part1.VZ * B[0] - part1.VX * B[2]) )
    Fz = part1.C * ( Campo(part2,part1)[2] + (part1.VX * B[1] - part1.VY * B[0]) )

    return [Fx, Fy, Fz, dt]

while(i <= 10000):
    
    p1.Evolucion(*Fuerza(p1, p2, dt))
    
    Posicion1[0].append(p1.X)
    Posicion1[1].append(p1.Y)
    Posicion1[2].append(p1.Z)

    
    p2.Evolucion(*Fuerza(p2, p1, dt))
    
    Posicion2[0].append(p2.X)
    Posicion2[1].append(p2.Y)
    Posicion2[2].append(p2.Z)
    
    i += 1
    
    
    
# Grafica de la trayectoria de la particula_1 y la particula_2
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(Posicion1[0], Posicion1[1], Posicion1[2], label ="Trayectoria de la particula_1")
ax.plot3D(Posicion2[0], Posicion2[1], Posicion2[2], label ="Trayectoria de la particula_2")
plt.legend(loc = "best")
ax.scatter(0.,0.,0.)
ax.scatter(1.,0.,0., color ="red")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
plt.save()

	

