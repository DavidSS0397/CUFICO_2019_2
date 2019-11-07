#!/usr/bin/python

#Importing useful tools
import numpy as np
from scipy.constants import G #Gravitational constan
import matplotlib.pyplot as plt
k_e = 8.987e9 # Coulomb's constant



# Arrays to save particles' positions
q1_x = np.array([])
q1_y = np.array([])
q1_z = np.array([])
q2_x = np.array([])
q2_y = np.array([])
q2_z = np.array([])


# Magnetic field components
B_x = 0
B_y = 0
B_z = 10


#Defining the "particle" class
class particle:


    #Initialization
    def __init__(self,x,y,z,vx,vy,vz,m,carga):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.m = m
        self.carga = carga

    # Calculates relative position respect to other particle
    def calc_rel_pos(self,other):
        x_rel = self.x-other.x
        y_rel = self.y-other.y
        z_rel = self.z-other.z

        return x_rel, y_rel, z_rel

    # Calculates gravitational force experienced due to other particle
    def calc_f_g(self,other):
        x_rel,y_rel,z_rel = self.calc_rel_pos(other)
        r = (x_rel**2+y_rel**+z_rel**2)**0.5
        f_g = (-G*self.m*other.m)/r**2

        return f_g

    # Calculates electrical force experienced due to other particle
    def calc_f_e(self,other):
        x_rel,y_rel,z_rel = self.calc_rel_pos(other)
        r = (x_rel**2+y_rel**+z_rel**2)**0.5
        f_e = (k_e*self.carga*other.carga)/r**2

        return f_e

    # Calculates electrical force experienced due to other particle
    def calc_B_force(self,B_x,B_y,B_z):

        B_force_x = self.carga* ( self.vy*B_z - self.vz*B_y )
        B_force_y = self.carga* ( -self.vx*B_z + self.vz*B_x )
        B_force_z = self.carga* ( self.vy*B_x - self.vx*B_y )
        return B_force_x, B_force_y, B_force_z

    # Calculates gravitational force experienced due to other particle
    def calc_net_f(self,other):


        e_f = self.calc_f_e(other)
        g_f = self.calc_f_g(other)
        net_f = e_f+g_f

        return net_f

    # Returns the net force on each axis.
    def force_by_axis(self,other,B_x,B_y,B_z):
        net_f = self.calc_net_f(other)
        x_rel,y_rel,z_rel = self.calc_rel_pos(other)

        r = (x_rel**2+y_rel**+z_rel**2)**0.5
        F_z = net_f*(z_rel/r)
        F_y = net_f*( np.sqrt( r ** 2 - z_rel ** 2 ) / r ) * ( y_rel / np.sqrt( r ** 2 - z_rel ** 2 ) )
        F_x = net_f*( np.sqrt( r ** 2 - z_rel ** 2 ) / r ) * ( x_rel / np.sqrt( r ** 2 - z_rel ** 2 ) )
        
        B_force_x, B_force_y, B_force_z = self.calc_B_force(B_x,B_y,B_z)
        F_x = F_x + B_force_x
        F_y = F_y + B_force_y
        F_z = F_z + B_force_z
        
        return F_x, F_y, F_z

    # Calculates acceleration in each axis
    def calc_acc(self,other):
        F_x, F_y, F_z = self.force_by_axis(other,B_x,B_y,B_z)
        acc_x = F_x/self.m
        acc_y = F_y/self.m
        acc_z = F_z/self.m
        return acc_x, acc_y, acc_z

    # Updates velocity in each axis
    def update_vel(self, other, t_step):
        acc_x, acc_y, acc_z = self.calc_acc(other)
        self.vx = self.vx + acc_x*t_step
        self.vy = self.vy + acc_y*t_step
        self.vz = self.vz + acc_z*t_step
        return

    # Updates positions in each axis
    def calc_new_position(self, other, t_step):
        self.update_vel(other,t_step)
        self.x = self.x + self.vx*t_step
        self.y = self.y + self.vy*t_step
        self.z = self.z + self.vz*t_step
        return




q1 = particle(0,0,0,0,0,0,10,6e-6) #Positive point charge
q2 = particle(1,0,0,0,0,0,10,-6e-6) #Negative point charge

N = 10000 # A counter for the simulation

# Calculation of the trayectories
for i in np.arange(0,N):

    q1.calc_new_position(q2,0.01)
    
    q1_x = np.append(q1_x,q1.x)
    q1_y = np.append(q1_y,q1.y)
    q1_z = np.append(q1_z,q1.z)
    
    q2.calc_new_position(q1,0.01)

    q2_x = np.append(q2_x,q2.x)
    q2_y = np.append(q2_y,q2.y)
    q2_z = np.append(q2_z,q2.z)


# Graphing trayectories
plt.plot(q1_x,q1_y,color = "r",label = "q+",ls ='--')
plt.plot(q2_x,q2_y, color = "b",label = "q-",ls ='--')

# Graphing particles
plt.scatter(q1_x[-1],q1_y[-1],color = "r")
plt.scatter(q2_x[-1],q2_y[-1],color = "b")

# Graphing options and displaying
plt.legend(loc='lower right')
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.title("Particles with oposing charges and magnetic field on Z+")
plt.show()
