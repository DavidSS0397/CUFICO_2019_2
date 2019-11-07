#!/bin/python


#Se definen las particulas con sus respectivos atributos e instancias, ademas de las fuciones y operaciones 
#a usar en la simulacion

class Particle:
	
	carga = True
	

	def __init__(self, x, y, z, vx, vy, vz, m, carga):
            
		self.X = x
		self.Y = y
		self.Z = z
		self.VX = vx
		self.VY = vy
		self.VZ = vz
		self.M = m
		self.Carga = carga
		
	def distancia(self, Particle):
	    return ( (self.X - Particle.X)**2
                     + (self.Y - Particle.Y)**2
                     + (self.Z - Particle.Z)**2 )**0.5
	
	def Cambio_pos(self, x, v, a, t):
		return x + (v*t) + (0.5*a*t**2)
		
	def Cambio_vel(self, v, a, t):
		return v + a*t
		
	def Cambio_tmp(self, fx, fy, fz, t):
	    self.Estado_anterior = [self.X, self.Y, self.Z, self.VX, self.VY, self.VZ, self.M, self.Carga]
	    self.X = self.Cambio_pos(self.X, self.VX, fx/self.M, t)
	    self.Y = self.Cambio_pos(self.Y, self.VY, fy/self.M, t)
	    self.Z = self.Cambio_pos(self.Z, self.VZ, fz/self.M, t)
	    self.VX = self.Cambio_vel(self.VX, fx/self.M, t)
	    self.VY = self.Cambio_vel(self.VY, fy/self.M, t)
	    self.VZ = self.Cambio_vel(self.VZ, fz/self.M, t)
		
	def time_slice_print(self):
		print("x = {0:.2f}, y = {1:.2f}, z = {2:.2f}".format(self.X, self.Y, self.Z))


#calculo de la intensidad del campo electrico
def electrico(P1, P2):
    
    r=P1.distancia(P2)
    K=1
    Ex=P1.Carga*(P2.X-P1.X)*K/r**3
    Ey=P1.Carga*(P2.Y-P1.Y)*K/r**3
    Ez=P1.Carga*(P2.Z-P1.Z)*K/r**3

    return [Ex,Ey,Ez]

#calculo de la fuerza de lorenzt
def lorenzt(P1, P2, dt):
    B = (0., 0., 10.)
    Fx = P1.Carga * ( electrico(P2,P1)[0] + (P1.VY * B[2] - P1.VZ * B[1]) )
    Fy = P1.Carga * ( electrico(P2,P1)[1] + (P1.VZ * B[0] - P1.VX * B[2]) )
    Fz = P1.Carga * ( electrico(P2,P1)[2] + (P1.VX * B[1] - P1.VY * B[0]) )

    return [Fx, Fy, Fz, dt]
