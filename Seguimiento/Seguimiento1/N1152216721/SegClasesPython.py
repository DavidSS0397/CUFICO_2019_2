#!/usr/bin/env python
#-*- coding:utf-8 -*-

####LIBRARIES
import time as time
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

####TIME START
start = time.time()

####BEGIN PROGRAM

####VARIABLES AND CONSTANTS
q = 1.0e-5 #1.0e-19 #fundamental charge
m = 10.0 #9.109e-31 #mass of the electron
r = 1.0 #5.29e-11 #Bohr radius, to locate the particles
eic = 8.9875e+09 #electric interaction constant, 1/(4 pi epsilon0)
mic = 1.0e-07 #magnetic interaction constant, mu0/(4 pi)
Eext = np.array([0.0, 0.0, 0.0]) #external electric field
Bext = np.array([0.0, 0.0, 10.0]) #external magnetic field
TotalT = 1000 #total time of interaction
N = 1000 #Number of iterations
Tstep = TotalT/N #time step for evolution of the system


####CLASSES AND FUNCTIONS
class Particle:
    """A class for storing each particle information: mass, charge,
    position and velocity, in cartesian coordinates."""

    def __init__(self, mass, charge, pos, vel):
        self.mass = mass #inertial mass
        self.charge = charge #electric charge
        self.pos = pos #position three-vector
        self.vel = vel #velocity three-vector

def ExtLorentz(evc):
    #Lorentz force on the evaluation charge "evc" due to external fields Eext and Bext
    FL = evc.charge * (Eext + np.cross(evc.vel, Bext) )
    return FL
        
def Eforce(src, evc):
    #Electric force due to the source charge "src" on the evaluation charge "evc"
    FE = eic * src.charge * evc.charge * (evc.pos - src.pos)
    return FE / LA.norm(evc.pos - src.pos)**3

def Mforce(src, evc):
    #Magnetic force due to the source charge "src" on the evaluation charge "evc"
    FB = mic * src.charge * evc.charge * np.cross(evc.vel, np.cross(src.vel, (evc.pos - src.pos)))
    return FB / LA.norm(evc.pos - src.pos)**3


####DEFINITION OF ATTRIBUTES FOR PARTICLES 1 AND 2
init_pos1 = np.array([0., 0., 0.])
init_pos2 = np.array([r, 0., 0.])
init_vel1 = np.array([0., 0., 0.])
init_vel2 = np.array([0., 0., 0.])
particle1 = Particle(m, q, init_pos1, init_vel1)
particle2 = Particle(m, -q, init_pos2, init_vel2)


####DISCRETE NUMERICAL EVOLUTION OF THE SYSTEM

#Lists for storing particles positions
part1_posx = [particle1.pos[0]]
part1_posy = [particle1.pos[1]]
part1_posz = [particle1.pos[2]]

part2_posx = [particle2.pos[0]]
part2_posy = [particle2.pos[1]]
part2_posz = [particle2.pos[2]]


for DeltaT in np.linspace(0., TotalT, N):

    #Particle 1
    Force1 = ExtLorentz(particle1) + Eforce(particle2, particle1) + Mforce(particle2, particle1)
    Accel1 = Force1 / particle1.mass
    particle1_new_vel = particle1.vel + DeltaT * Accel1
    particle1_new_pos = particle1.pos + particle1.vel * DeltaT + 0.5 * Accel1 * DeltaT**2

    #Particle 2
    Force2 = ExtLorentz(particle2) + Eforce(particle1, particle2) + Mforce(particle1, particle2)
    Accel2 = Force2 / particle2.mass
    particle2_new_vel = particle2.vel + DeltaT * Accel2
    particle2_new_pos = particle2.pos + particle2.vel * DeltaT + 0.5 * Accel2 * DeltaT**2

    #Updating particles attributes
    particle1.pos = particle1_new_pos
    particle1.vel = particle1_new_vel

    particle2.pos = particle2_new_pos
    particle2.vel = particle2_new_vel

    #Adding computed position values to the storing lists
    part1_posx.append(particle1_new_pos[0])
    part1_posy.append(particle1_new_pos[1])
    part1_posz.append(particle1_new_pos[2])

    part2_posx.append(particle2_new_pos[0])
    part2_posy.append(particle2_new_pos[1])
    part2_posz.append(particle2_new_pos[2])
    

####TIME FINISH
finish = time.time()
duration = finish - start
print("Excecution duration: %.3f seconds."%duration)

    
####PLOTTING
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Initial positions
ax.scatter(init_pos1[0], init_pos1[1], init_pos1[2], 'ro', label='Initial position of particle 1')
ax.scatter(init_pos2[0], init_pos2[1], init_pos2[2], 'go', label='Initial position of particle 2')

#Trajectories
ax.plot(part1_posx, part1_posy, part1_posz, 'r-', label='Trajectory of particle 1')
ax.plot(part2_posx, part2_posy, part2_posz, 'g-', label='Trajectory of particle 2')

ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

####END PROGRAM
