import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Two particles in a magnetic field.

By: Carolina Herrera S.

Updated: august 22, 2019
"""

class Particle:
    
    charged = True
    
    def __init__(self, x, y, z, vx, vy, vz, m, charge):
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.M = m
        self.Charge = charge
    
    def distance(self, Particle_b):
        dist = dist_sq = np.sqrt((self.X-Particle_b.X)**2 \
                + (self.Y-Particle_b.Y)**2 + (self.Z-Particle_b.Z)**2)
        return dist
    
    def movement_step(self, force, dt):
        force_x, force_y, force_z = force
        
        ax = force_x/self.M
        self.VX += ax*dt
        self.X += self.VX*dt + ax*dt**2/2
        
        ay = force_y/self.M
        self.VY += ay*dt
        self.Y += self.VY*dt + ay*dt**2/2
        
        az = force_z/self.M
        self.VZ += az*dt
        self.Z += self.VZ*dt + az*dt**2/2


def lorentz_force(Particle_a, Particle_b):
    Bz = 10.
    k = 9e9
    
    Ex = k*Particle_b.Charge*(Particle_b.X-Particle_a.X)/Particle_a.distance(Particle_b)**2
    Ey = k*Particle_b.Charge*(Particle_b.Y-Particle_a.Y)/Particle_a.distance(Particle_b)**2
    Ez = k*Particle_b.Charge*(Particle_b.Z-Particle_a.Z)/Particle_a.distance(Particle_b)**2
    
    force_x = Particle_a.Charge*(Ex + Particle_a.VY*Bz)
    force_y = Particle_a.Charge*(Ey - Particle_a.VX*Bz)
    force_z = Particle_a.Charge*Ez
    
    return force_x, force_y, force_z


if __name__ == '__main__':
    
    # Parameters
    q = 1.
    m = 10.
    x01, y01, z01 = 0., 0., 0.
    x02, y02, z02 = 1., 0., 0.
    vx01, vy01, vz01 = 0., 0., 0.
    vx02, vy02, vz02 = 0., 0., 0.
    
    dt = 0.01
    steps = 10000
    
    x1, y1, z1 = [], [], []
    x2, y2, z2 = [], [], []
    
    # System
    Particle1 = Particle(x01, y01, z01, vx01, vy01, vz01, m, q)
    Particle2 = Particle(x02, y02, z02, vx02, vy02, vz02, m, -q)
    
    # Evolution
    for i in range(steps+1):
        x1.append(Particle1.X)
        y1.append(Particle1.Y)
        z1.append(Particle1.Z)
        
        x2.append(Particle2.X)
        y2.append(Particle2.Y)
        z2.append(Particle2.Z)
        
        force1 = lorentz_force(Particle1, Particle2)
        force2 = lorentz_force(Particle2, Particle1)
        
        Particle1.movement_step(force1, dt)
        Particle2.movement_step(force2, dt)
        
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x1, y1, z1, 'r')
    ax.plot([Particle1.X],[Particle1.Y],[Particle1.Z], 'or')
    ax.plot(x2, y2, z2, 'b')
    ax.plot([Particle2.X],[Particle2.Y],[Particle2.Z], 'ob')
    
    plt.show()



