import numpy as np 
import  matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d



class Particle:
    cargada = True 

    def __init__(self, x, y, z, vx, vy, vz, m, carga):
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.M = m
        self.Carga = carga

    def Vel (self, v0, a, t):
            v = v0 + a*t 
            return v
    def Pos (self, x0,v0,a,t):
            x = x0 + v0*t + 0.5*v0*t**2
            return x


  

    def Mov (self, a, t):
            self.R=np.zeros((1,6))
            self.X = self.Pos(self.X, self.VX,a,t)
            self.VX = self.Vel(self.VX, a, t)
            self.Y = self.Pos(self.Y, self.VY, a,t)
            self.VY = self.Vel(self.VY,a,t)
            self.Z = self.Pos(self.Z, self.VZ, a,t)
            self.VZ = self.Vel(self.VZ, a ,t)
            self.R[0,0] = self.X 
            self.R[0,1] = self.Y
            self.R[0,2] = self.Z 
            self.R[0,3] = self.VX 
            self.R[0,4] = self.VY 
            self.R[0,5] = self.VZ 
            return self.R


def Ace (F, M):
    a=np.zeros((1,3))
    Fx=F[0,0] ; Fy=F[0,1] ; Fz=F[0,2] ;
    a[0,0]=Fx/M
    a[0,1]=Fy/M
    a[0,2]=Fz/M
    return a        


   
    
A = Particle(0.,0.,0.,0.,0.,0.,10.,1.)
B = Particle(1.,0.,0.,0.,0.,0.,10.,-1.)
M=10.
#F = [10,10,10]
#a = [F/A.M,F/A.M,F/A.M]

print A.VX
XA=[]
XB=[]
RA=np.zeros((1000000,8))  # x, y, z, vx, vy, vz, a, t
RB=np.zeros((1000000,8))

j=0
for i  in np.arange(0,1000,0.01):
    
    k=9.9e9
    F=np.zeros((1,3))
    F[0,0] = k * (A.Carga * B.Carga)*(A.X+B.X)/((A.X-B.X)**2 + (A.Y-B.Y)**2 + (A.Z-B.Z)**2)**(3./2) - A.VY*M
    F[0,1] = k * (A.Carga * B.Carga)*(A.Y+B.Y)/((A.X-B.X)**2 + (A.Y-B.Y)**2 + (A.Z-B.Z)**2)**(3./2) - A.VX*M
    F[0,2] = k * (A.Carga * B.Carga)*(A.Z+B.Z)/((A.X-B.X)**2 + (A.Y-B.Y)**2 + (A.Z-B.Z)**2)**(3./2)
    aA = Ace(F, A.M)
    aB = -Ace(F, B.M) 
    RA[j,0] = A.Pos( A.X, A.VX, aA[0,0],i) ; RA[j,1] = A.Pos( A.Y, A.VY,aA[0,1],i) ; RA[j,2] = A.Pos( A.Z, A.VZ, aA[0,2],i) 
    RA[j,3] = A.Vel( A.VX,aA[0,0],i) ; RA[j,4] = A.Vel( A.VY,aA[0,1],i) ; RA[j,5] = A.Vel( A.VZ,aA[0,2],i)
    RA[j,6] = i 
    RB[j,0] = B.Pos( B.X, B.VX ,aB[0,0],i) ; RB[j,1] = B.Pos( B.Y, B.VY ,aB[0,1],i) ; RB[j,2] = B.Pos( B.Z, B.VZ,aB[0,2],i) 
    RB[j,3] = B.Vel( B.VX,aB[0,0],i) ; RB[j,4] = B.Vel( B.VY,aB[0,1],i) ; RB[j,5] = B.Vel( B.VZ,aB[0,2],i)
    RB[j,6] = i 
    A.X = RA[j,0] ; A.Y = RA[j,1] ; A.Z = RA[j,2] ; A.VX = RA[j,3] ; A.VY = RA[j,4] ; A.VZ = RA[j,5]
    B.X = RB[j,0] ; B.Y = RB[j,1] ; B.Z = RB[j,2] ; B.VX = RB[j,3] ; B.VY = RB[j,4] ; B.VZ = RB[j,5]
    j+=1
 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xA = np.array(RA[:,0])
yA = np.array(RA[:,1])
zA = np.array(RA[:,2])

xB = np.array(RB[:,0])
yB = np.array(RB[:,1])
zB = np.array(RB[:,2])


ax.plot(xA,yA,zA)
ax.plot(xB,yB,zB)
plt.show()
