import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0 as e0
from mpl_toolkits.mplot3d import Axes3D

class particle():
    def __init__(self, pos, vel, mass, charge):
        self.r = np.array(pos).astype('float64')
        self.v = np.array(vel).astype('float64')
        self.mass = mass
        self.charge = charge

    def E(self, r1, r2):
        return (1./(4.*np.pi*e0))*self.charge*(r1 - r2)/np.linalg.norm(r1-r2)**3

def trajectory(p1, p2, B):
    dt = 0.01

    pos1 = [[],[],[]]
    pos2 = [[],[],[]]

    for n in range(10000):
        v1 = p1.charge/p1.mass*(p2.E(p1.r,p2.r) + np.cross(p1.v,B))*dt
        p1.v += v1

        v2 = p2.charge/p2.mass*(p1.E(p2.r,p1.r) + np.cross(p2.v,B))*dt
        p2.v += v2

        r_1 = dt*p1.v
        p1.r += r_1

        r_2 = dt*p2.v
        p2.r += r_2

        for i in range(3):
            pos1[i].append(p1.r[i])
            pos2[i].append(p2.r[i])
            
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    ax.plot3D(pos1[0], pos1[1], pos1[2])
    ax.plot3D(pos2[0], pos2[1], pos2[2])
    ax.legend()

    plt.show()

r1, v1 = [0,0,0], [0,0,0]
r2, v2 = [1,0,0], [0,0,0]
B = np.array([0,0,10.])
    
P1 = particle(r1, v1, 10, 1)
P2 = particle(r2, v2, 10, -1)

trajectory(P1, P2, B)
