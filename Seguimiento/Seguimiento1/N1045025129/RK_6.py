import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  #Libreria para EDO

def Runge_Kutta(xn, yn, h, MyF):
    xn1 = xn + h
    k1 = h*MyF(yn, xn)
    k2 = h*MyF(yn+h*k1/2, xn+h/2)
    k3 = h*MyF(yn+h*k2/2, xn+h/2)
    k4 = h*MyF(yn+h*k3, xn+h)
    return yn + (1/6.)*(k1 + 2*k2 + 2*k3 + k4)

def Runge_Kutta3(xn, yn, h, MyF):
    a31 = -1
    a32 = 2
    b1 = 1/6; b3 = 1/6
    b2 = 2/3

    a21 = 1/2; c2 = 1/2; c3 = 1

    k1 = MyF(yn, xn)
    k2 = MyF(yn + h*(a21*k1), xn + h*c2)
    k3 = MyF(yn + h*(a31*k1 + a32*k2), xn + h*c2)
    return yn + h*(b1*k1 + b2*k2 + b3*k3)

def Runge_Kutta6(xn, yn, h, MyF):
    a21=1/3.
    a31 = 123./256; a32 = 315./256
    a41=191./750; a42=184./1250; a43=176./1875
    a51=26./81; a52=7./13; a53=304./4435; a54=175./291
    a61=151./150; a62=351./250; a63=304./4123; a64=7./71; a65=245./173

    
    b1 = 1/24.; b3 = 0
    b2 = 0; b4=125./336
    b5=27./56 ; b6=5./48

    c2 = 1/3.; c3 = 3/4.; c4=1/5.; c5=2/3.; c6=1.

    k1 = MyF(yn, xn)
    k2 = MyF(yn + h*(a21*k1), xn + h*c2)
    k3 = MyF(yn + h*(a31*k1 + a32*k2), xn + h*c3)
    k4 = MyF(yn + h*(a41*k1 + a42*k2+a43*k3), xn + h*c4)
    k5 = MyF(yn + h*(a51*k1 + a52*k2+a53*k3*a54*k4), xn + h*c5)
    k6 = MyF(yn + h*(a61*k1 + a62*k2+a63*k3*a64*k4+a65*k5), xn + h*c6) 
    return yn + h*(b1*k1 + b2*k2 + b3*k3 + b4*k4 + b5*k5 + b6*k6)
    
def Euler(xn, yn, h, MyF):
    return yn + h*MyF(yn, xn)

def Euler_mod(xn, yn, h, MyF):
    yn2 = yn + 0.5*h*MyF(yn, xn)
    xn2 = xn + 0.5*h
    return yn + h*MyF(yn2, xn2)


def MyFirstODE(y, x):
    return x-y

def ExactSolution(x):
    return x-1+2*np.exp(-x)

def MyFirstODE(y, x):
    return x-y



NumPuntos=np.array([10, 100, 1000, 10000])
x0=0.0
xf=5.0
y0=1.0
h=(xf-x0)/NumPuntos

y1_difference = []
yE_difference = []
yEM_difference = []
yRK_difference = []
yRK3_difference = []
yRK6_difference = []


TotalEuler = []
TotalDiffEuler = []
TotalEuler_mod = []
TotalDiffEuler_mod = []
TotalRK = []
TotalDiffRK = []
TotalRK3 = []
TotalDiffRK3 = []
TotalRK6 = []
TotalDiffRK6 = []
TotalExact = []
TotalYS = []
TotalDiffYS = []
TotalXS =[]


for j in NumPuntos:

    EulerSolutions = []
    Euler_modSolutions = []
    RKSolutions = []
    RK3Solutions = []
    RK6Solutions = []

    xs = np.linspace(x0, xf, j)
    EulerSolutions.append(y0)
    Euler_modSolutions.append(y0)
    RKSolutions.append(y0)
    RK3Solutions.append(y0)
    RK6Solutions.append(y0)
 
    for i in xs[1:]:

         CurrentSolution = Euler(i, EulerSolutions[-1], ((xf-x0)/j), MyFirstODE)
         CurrentSolution_mod = Euler_mod(i, Euler_modSolutions[-1], ((xf-x0)/j), MyFirstODE)
         CurrentSolution_RK = Runge_Kutta(i, RKSolutions[-1], ((xf-x0)/j), MyFirstODE)
         CurrentSolution_RK3 = Runge_Kutta3(i, RK3Solutions[-1], ((xf-x0)/j), MyFirstODE)
         CurrentSolution_RK6 = Runge_Kutta6(i, RK6Solutions[-1], ((xf-x0)/j), MyFirstODE)

         EulerSolutions.append(CurrentSolution)
         Euler_modSolutions.append(CurrentSolution_mod)
         RKSolutions.append(CurrentSolution_RK)
         RK3Solutions.append(CurrentSolution_RK3)
         RK6Solutions.append(CurrentSolution_RK6)

    ys = odeint(MyFirstODE, y0, xs)
    ys = np.array(ys).flatten()

    y_exact = ExactSolution(xs)

    TotalDiffEuler.append(np.abs(EulerSolutions-y_exact))
    TotalDiffEuler_mod.append(np.abs(Euler_modSolutions-y_exact))
    TotalDiffRK.append(np.abs(RKSolutions-y_exact))
    TotalDiffRK3.append(np.abs(RK3Solutions-y_exact))
    TotalDiffRK6.append(np.abs(RK6Solutions-y_exact))
    TotalDiffYS.append(np.abs(ys-y_exact))
    
    TotalEuler.append(EulerSolutions)
    TotalEuler_mod.append(Euler_modSolutions)
    TotalRK.append(RKSolutions)
    TotalRK3.append(RK3Solutions)
    TotalRK6.append(RK6Solutions)
    TotalExact.append(y_exact)
    TotalYS.append(ys)
    TotalXS.append(xs)

    y1_difference.append(np.mean(np.abs(ys-y_exact)))
    yE_difference.append(np.mean(np.abs(EulerSolutions-y_exact)))
    yEM_difference.append(np.mean(np.abs(Euler_modSolutions-y_exact)))
    yRK_difference.append(np.mean(np.abs(RKSolutions-y_exact)))
    yRK3_difference.append(np.mean(np.abs(RK3Solutions-y_exact)))
    yRK6_difference.append(np.mean(np.abs(RK6Solutions-y_exact)))

    
    
    
        
for i in range(0, len(TotalYS)):
    
    

    fig = plt.figure(figsize=(12, 4))

    ax0 = fig.add_subplot(131)
    ax1 = fig.add_subplot(132)
    ax2 = fig.add_subplot(133)

    ax0.plot(TotalXS[i], TotalYS[i], "r")
    ax0.plot(TotalXS[i], TotalEuler[i], "b")
    ax0.plot(TotalXS[i], TotalEuler_mod[i], "k")
    ax0.plot(TotalXS[i], TotalRK[i], "y")
    ax0.plot(TotalXS[i], TotalRK3[i], "c")
    ax0.plot(TotalXS[i], TotalRK6[i], "b--")
    ax0.plot(TotalXS[i], TotalExact[i], "g--")
    

    ax1.semilogy(TotalXS[i], TotalDiffEuler[i], "b")
    ax1.semilogy(TotalXS[i], TotalDiffEuler_mod[i], "k")
    ax1.semilogy(TotalXS[i], TotalDiffRK[i], "y")
    ax1.semilogy(TotalXS[i], TotalDiffRK3[i], "c")
    ax1.semilogy(TotalXS[i], TotalDiffRK6[i], "b--")
    ax1.semilogy(TotalXS[i], TotalDiffYS[i], "r")

    ax2.plot(h, y1_difference, "r")
    ax2.plot(h, yE_difference, "b")
    ax2.plot(h, yEM_difference, "k")
    ax2.plot(h, yRK_difference, "y")
    ax2.plot(h, yRK3_difference, "b--")
    ax2.plot(h, yRK6_difference, "c")

    plt.show()
        
