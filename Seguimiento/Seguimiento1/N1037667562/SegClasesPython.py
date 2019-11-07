import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.constants import epsilon_0
from mpl_toolkits.mplot3d import Axes3D

class Particles:
	'''Sistema formado por dos particulas cargadas bajo un campo magnetico
	constante en dirección z'''

	def __init__(self, pv0, m1, m2, q1, q2, B):
		self.pv0=pv0
		self.m1=m1; self.m2=m2
		self.q1=q1; self.q2=q2
		self.B=B

	def Graphics(self):
		self.solutions()

		fig = plt.figure(figsize=(10,6))
		ax1 = fig.add_subplot(121, projection='3d')
		ax2 = fig.add_subplot(122, projection='3d')

		ax1.plot(self.X1, self.Y1, self.Z1, 'c-', label='Particle 1')
		ax2.plot(self.X2, self.Y2, self.Z2, 'm-', label='Particle 2')

		ax1.plot([self.X1[-1]], [self.Y1[-1]], [self.Z1[-1]], 'ko', label='last position')
		ax2.plot([self.X2[-1]], [self.Y2[-1]], [self.Z2[-1]], 'ko', label='last position')

		ax1.set_xlabel("x(t)"); ax1.set_ylabel("y(t)"); ax1.set_zlabel("z(t)")
		ax2.set_xlabel("x(t)"); ax2.set_ylabel("y(t)"); ax2.set_zlabel("z(t)")

		#ax1.set_title("Particula 1"); ax2.set_title("Particula 2")

		ax1.legend(); ax2.legend()
		plt.tight_layout()

		plt.show()

	def solutions(self):
		dt = 0.01
		T = np.arange(0,10000,dt)

		y0 = self.pv0

		#---- numerical solution
		X1=[]; Y1=[]; Z1=[]; X2=[]; Y2=[]; Z2=[]

		for t in T:
		    y0 = self.rk4(self.f1,t,dt,y0,12)
		    X1.append(y0[0])
		    Y1.append(y0[1])
		    Z1.append(y0[2])
		    X2.append(y0[3])
		    Y2.append(y0[4])
		    Z2.append(y0[5])

		self.X1=np.array(X1); self.Y1=np.array(Y1); self.Z1=np.array(Z1)
		self.X2=np.array(X2); self.Y2=np.array(Y2); self.Z2=np.array(Z2)


	def f1(self, t,y):  #Ecuaciones que rigen el movimiento del sistema
	    rhs = [0]*12
	    c=4*np.pi*epsilon_0
	    
	    #y[0] = x1; y[1] = y1; y[2] = z1; y[3] = x2; y[4] = y2; y[5] = z2
	    #y[6] = vx1; y[7] = vy1; y[8] = vz1; y[9] = vx2; y[10] = vy2; y[11] = vz2

	    rr = ((y[0]-y[3])**2 + (y[1]-y[4])**2 + (y[2]-y[5])**2 )**(3/2)

	    #Position's equation for both particles
	    rhs[0] = y[6]; rhs[1] = y[7]; rhs[2] = y[8]
	    rhs[3] = y[9]; rhs[4] = y[10]; rhs[5] = y[11]

	    #velocity equations - Particle 1
	    rhs[6] = self.q1*self.q2*(y[0]-y[3])/(self.m1*c*rr) + self.q1*y[7]*self.B/self.m1
	    rhs[7] = self.q1*self.q2*(y[1]-y[4])/(self.m1*c*rr) - self.q1*y[6]*self.B/self.m1
	    rhs[8] = self.q1*self.q2*(y[2]-y[5])/(self.m1*c*rr)

	    #velocity equations - Particle 2
	    rhs[9] = self.q2*self.q1*(y[3]-y[0])/(self.m2*c*rr) + self.q2*y[10]*self.B/self.m2
	    rhs[10] = self.q2*self.q1*(y[4]-y[1])/(self.m2*c*rr) - self.q2*y[9]*self.B/self.m2
	    rhs[11] = self.q2*self.q1*(y[5]-y[2])/(self.m2*c*rr)

	    return rhs


	def rk4(self, f,t,h,y,n):  #Método de Runge_Kuta para la solución
	    k1 = [0.]*(n)
	    k2 = [0.]*(n)
	    k3 = [0.]*(n)
	    k4 = [0.]*(n)
	    
	    ymudo = [0]*(n)
	    fR = f(t,y)
	    
	    for i in range(0,n):
	        k1[i] = h*fR[i]

	    for i in range(0,n):
	        ymudo[i] = y[i] + k1[i]*0.5
	        
	    fR = f(t+h*0.5, ymudo)

	    for i in range(0,n):
	        k2[i] = h*fR[i]
	        ymudo[i] = y[i] + k2[i]*0.5
	        
	    fR = f(t+h*0.5,ymudo)
	    
	    for i in range(0,n):
	        k3[i] = h*fR[i]
	        ymudo[i] = y[i] + k3[i]
	        
	    fR = f(t+h, ymudo)    
	    for i in range(0,n):
	        k4[i] = h*fR[i]
	               
	    for i in range(0,n):
	        y[i] = y[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6.
	        
	    return y

##----------------- Usando la Clase --------------------------

m1 = 10; m2 = 10
q1 = 1; q2 = -1
B = 10

yy0=[0,0,0,1,0,0,0,0,0,0,0,0]

SISTEM = Particles(yy0, m1, m2, q1, q2, B)

SISTEM.Graphics()











