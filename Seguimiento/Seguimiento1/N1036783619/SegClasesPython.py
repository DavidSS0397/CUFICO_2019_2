import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d


#Se define la particula dentro de una clase
class P:

    cargada=True

    def __init__(self,x,y,z,vx,vy,vz,m,carga): #instancias de la clase
        self.X=x
        self.Y=y
        self.Z=z
        self.VX=vx
        self.VY=vy
        self.VZ=vz
        self.M=m
        self.Carga=carga

    def PoEv(self,xi,vi,a,t):          #ecuacion cinematica para la posicion
        return xi+(vi*t)+(0.5*a*(t**2))
        
    def VeEv(self,vi,a,t):  #ecuacion cinematica para la velocidad
        return vi+(a*t)
        
    def TiEv(self,fx,fy,fz,t):
        self.X=self.PoEv(self.X,self.VX, fx/self.M, t)
        self.Y=self.PoEv(self.Y,self.VY, fy/self.M, t)
        self.Z=self.PoEv(self.Z,self.VZ, fz/self.M, t)
        self.VX=self.VeEv(self.VX,fx/self.M ,t)
        self.VY=self.VeEv(self.VY,fy/self.M ,t)
        self.VZ=self.VeEv(self.VZ,fz/self.M ,t)
        

#particulas cargadas
P1=P(0.0,0.0,0.0,0.0,0.0,0.0,10.0,10)
P2=P(1.0,0.0,0.0,0.0,0.0,0.0,10.0,-10)
B=10. #campo magnetico
dt=0.01 #pasos
PP1=[[],[],[]] #posicion de particula 1
PP2=[[],[],[]] #posicion de particula 2

def BForce (q,v,b): #funcion que define componente de fuerza magnetica
    return q*v*b
def EForce (q1,q2,x1,x2,r):
    return (1/(r**3))*(x1-x2)*(q1*q2) #funcion que define componente de fuerza electrica


i=0
for i in range (0,10000):
    #se anaden las posiciones de las particulas
    PP1[0].append(P1.X);PP1[1].append(P1.Y);PP1[2].append(P1.Z) 
    PP2[0].append(P2.X);PP2[1].append(P2.Y);PP2[2].append(P2.Z)
    #distancias entre las particulas
    r21=((P1.X-P2.X)**2+(P1.Y-P2.Y)**2+(P1.Z-P2.Z)**2)**(1/2) 
    r12=((P2.X-P1.X)**2+(P2.Y-P1.Y)**2+(P2.Z-P1.Z)**2)**(1/2) 
    #componentes de la fuerza sobre la particula 1
    F1x=BForce(P1.Carga,P1.VY,B) + EForce(P1.Carga,P2.Carga,P1.X,P2.X,r21) 
    F1y=-1.0*BForce(P1.Carga,P1.VX,B) + EForce(P1.Carga,P2.Carga,P1.Y,P2.Y,r21)
    F1z=EForce(P1.Carga,P2.Carga,P1.Z,P2.Z,r21)
    #componentes de la fuerza sobre la particula 2
    F2x=BForce(P2.Carga,P2.VY,B) + EForce(P1.Carga,P2.Carga,P2.X,P1.X,r12)
    F2y=-1.0*BForce(P2.Carga,P2.VX,B) +EForce(P1.Carga,P2.Carga,P2.Y,P1.Y,r12)
    F2z=EForce(P1.Carga,P2.Carga,P2.Z,P1.Z,r12)
    #evolucion temporal
    P1.TiEv(F1x, F1y, F1z, dt)
    P2.TiEv(F2x, F2y, F2z, dt)
    i+=1


plt.figure(figsize=(10,10))
A=plt.axes(projection='3d')
A.plot3D( PP1[0], PP1[1], PP1[2],color='red',label= r'$Particula\ positiva$')
A.plot3D(PP2[0],PP2[1], PP2[2],color='black',label= r'$Particula\ negativa$')
A.legend(loc='lower right')
plt.title(r'$Particulas\ con\ cargas\ opuestas\ sometidas\ a\ un\ campo\ magnetico''$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.show()