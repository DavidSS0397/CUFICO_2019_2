# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

t=0     
#make the step small relative to the velocity, cause if not euler methods eventually adds a considerable amount of energy to the system   
dt=0.001 #with 0.001 - 0.0001 is optimus to this particular problem
        
class Particle:
    
    #Atributos
    cargada = True
    
    #Instancias (metodos)
    def __init__(self, x, y, z, vx, vy, vz, m, carga): #Funcion que se aplica sobre la classe misma (sel
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.M = m
        self.Carga = carga
        self.trajectoryx = []
        self.trajectoryy = []
        self.trajectoryz = []
        self.V=[self.VX,self.VY,self.VZ]
        
    def ECoulombsLEulerM(self, q, xq, yq, zq): #electric interaction
        
        #rate(100)
        #force 
  
        r=xq-self.X
        ry=xq-self.Y
        rz=xq-self.Z #squared?
        
#        forcex = 9*10**9*self.Carga*q*/r**2
#        forcey = 9*10**9*self.Carga*q/ry**3
#        forcez = 9*10**9*self.Carga*q/rz**3
        
        forcex = 9*10**9*self.Carga*q*self.X/r**3
        forcey = 9*10**9*self.Carga*q*self.Y/ry**3
        forcez = 9*10**9*self.Carga*q*self.Z/rz**3
        #print(force)
        self.ax= forcex/self.M
        self.ay= forcey/self.M
        self.az= forcez/self.M
        #print(self.a,self.Ax)
        
        self.VX = self.VX + self.ax*dt 
        self.X = self.X + self.VX * dt
        self.VY = self.VY + self.ay*dt 
        self.Y = self.Y + self.VY * dt
        self.VZ = self.VZ + self.az*dt 
        self.Z = self.Z + self.VZ * dt

#        self.trajecCentralEFx.append(np.copy(self.X))
#        self.trajecCentralEFy.append(np.copy(self.Y))
#        self.trajecCentralEFz.append(np.copy(self.Z))
        self.trajectoryx.append(np.copy(self.X))
        self.trajectoryy.append(np.copy(self.Y))
        self.trajectoryz.append(np.copy(self.Z))
        self.V=[self.VX,self.VY,self.VZ]
        #print(self.V)
        
        return self.trajectoryx, self.trajectoryy, self.trajectoryz
        
    def BLorentzLEulerM(self, Bx, By, Bz):
        B=[Bx,By,Bz]
        #rate(100)
        #force (lorentz's force)
#        Fz=self.Carga*self.VX*By-
#        Fx=self.Carga*(self.VY*Bz-self.VZ*By)
#        Fy=-self.Carga*self.VX*Bz-
        force = self.Carga * np.cross(self.V,B)
        #print(force)
        self.a= force/self.M
        self.Ax= self.a[0]
        self.Ay= self.a[1]
        self.Az= self.a[2]
        #print(self.a,self.Ax)
        
        self.VX = self.VX + self.Ax*dt 
        self.X = self.X + self.VX * dt
        self.VY = self.VY + self.Ay*dt 
        self.Y = self.Y + self.VY * dt
        self.VZ = self.VZ + self.Az*dt 
        self.Z = self.Z + self.VZ * dt
        
        #if (Fx<0.001):
            #print ('fuerzax = ',Fx,'t =',t)
#            plt.figure(3)
#            plt.plot(pos=(t,self.VX))
#            plt.figure(4)
#            plt.plot(pos=(t,self.X))
        
        #to save trajectory's points
        self.trajectoryx.append(np.copy(self.X))
        self.trajectoryy.append(np.copy(self.Y))
        self.trajectoryz.append(np.copy(self.Z))
        self.V=[self.VX,self.VY,self.VZ]
        #print(self.V)
        return self.trajectoryx, self.trajectoryy, self.trajectoryz, self.X, self.Y, self.Z, self.Carga
        
    def graphs(self,xx,yy,zz,gn):       
        #grphs 2D
        plt.figure(1+gn)
        plt.plot(self.trajectoryx,self.trajectoryz)
        
        #3D graph, position of the particle
        fig=plt.figure(2+gn)
        ax = plt.axes(projection='3d')
        ax.plot3D(self.trajectoryx,self.trajectoryy, self.trajectoryz)#ax.plot3D(self.trajectoryx,self.trajectoryy,self.trajectoryz)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()
        #print(self.VX)
        
Particle1=Particle(0,0,0,3,3,2,10.,1.)
Particle2=Particle(0,0,0,6,6,4,10.,-1.)
#Euler's Method
for i in np.arange(0,100,dt):
    #
    p1x,p1y,p1z,xq,yq,zq,qq =Particle1.BLorentzLEulerM(0,0,10.)
    #pC1x,pC1y,pC1z=Particle1.ECoulombsLEulerM(qq,xq,yq,zq)
    p2x,p2y,p2z,xq2, yq2,zq2,qq2 =Particle2.BLorentzLEulerM(0,0,10.)
    #pC2x,pC2y,pC2z=Particle2.ECoulombsLEulerM(qq2,xq2,yq2,zq2)
#----------al tratar de aplicar la interaccion gravitacional el programa falla
    t=t+dt
p1tx,p1ty,p1tz=p1x,p1y,p1z
Particle1.graphs(p1tx,p1ty,p1tz,1)
Particle2.graphs(p2x,p2y,p2z,3)

#for i in np.arange(0,100,dt):
#    Particle2.EulersMethod(0,0,10.)
#    t=t+dt
#
#Particle2.graphs()


        
        
