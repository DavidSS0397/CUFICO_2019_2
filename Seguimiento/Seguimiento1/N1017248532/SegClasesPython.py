import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, pi
from mpl_toolkits.mplot3d import Axes3D

ke = 1/(4*pi*epsilon_0) #Coulombs constant

class Particle:
    def __init__(self, x, y, z, vx, vy, vz, m, charge): #Initial conditions and parameters
        self.M = m
        self.Charge = charge
        self.R = np.array([x,y,z])
        self.V = np.array([vx,vy,vz])

        self.R_plot = np.array([self.R]) #this array will be used for plotting later

        # rp: coordinates of the source particle, qp: charge of the source particle, B magnetic field
        self.Lorentz_Force = lambda rp,qp,B: self.Charge*(ke*qp*(self.R - rp)/np.sqrt(np.sum((self.R-rp)**2))**3 + np.cross(self.V,B))

#the class system consists of each particle and their interaction
class System:
    def __init__(self):
        self.P1 = Particle(0,0,0,0,0,0,10,1)
        self.P2 = Particle(1,0,0,0,0,0,10,-1)
        self.B = [0,0,10]
        self.Interaction(0,100,0.01)

    def Interaction(self,to,tf,dt): #Simulates the interaction of the particles with the magnetic field and eachother

        for _ in np.arange(to,tf,dt):
            #Cinematic equations with the aproximation df ~ f(t+dt) - f(t)
            '''
            The cinematic equations are thus:
            x(t+dt) = x(t) + v(t+dt)*dt
            v(t+dt) = v(t) + a(t+dt)*dt
            '''
            
            self.P1.A = self.P1.Lorentz_Force(self.P2.R,self.P2.Charge,self.B)/self.P1.M
            self.P2.A = self.P2.Lorentz_Force(self.P1.R,self.P1.Charge,self.B)/self.P2.M

            self.P1.V = self.P1.V + self.P1.A*dt
            self.P2.V = self.P2.V + self.P2.A*dt

            self.P1.R = self.P1.R + self.P1.V*dt
            self.P2.R = self.P2.R + self.P2.V*dt


            self.P1.R_plot = np.append(self.P1.R,self.P1.R_plot)
            self.P2.R_plot = np.append(self.P2.R,self.P2.R_plot)


    def plot(self):
        self.P1.R_plot = np.reshape(self.P1.R_plot, (-1, 3))
        self.P2.R_plot = np.reshape(self.P2.R_plot, (-1, 3))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')
        ax.plot3D(self.P1.R_plot[:,0], self.P1.R_plot[:,1],self.P1.R_plot[:,2], color = 'r', label = 'Particle 1', linewidth = 1)
        ax.plot3D(self.P2.R_plot[:,0], self.P2.R_plot[:,1],self.P2.R_plot[:,2], color = 'blue', label = 'Particle 2', linewidth = 1)

        ax.legend(loc = "upper right")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        plt.show()

s = System()
s.plot()
