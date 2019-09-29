import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint #Integrador de scipy que se usara como solucion exacta


#Asignacion de valores de las constantes
a=1.
b=1.
c=1.
d=1.


#Usando metodo RK4
#Definimos las ecuaciones diferenciales dentro de la misma funcion
def F(N,t):
    n1,n2=N
    return np.array([n1*(a-b*n2), -n2*(c-d*n1)])
#Se implementa el RK4 para la solucion de las ecuaciones acopladas
def RK4(f,u0,t0,tf,n):
    t=np.linspace(t0,tf,n+1) #Se establece la particion para la integracion
    N=np.array((n+1)*[u0]) #Variable en la cual se guarda la solucion
    h=t[1]-t[0]       
    for i in range(n):
        k1=h*f(N[i],t[i])    
        k2=h*f(N[i]+0.5*k1,t[i]+0.5*h)
        k3=h*f(N[i]+0.5*k2,t[i]+0.5*h)
        k4=h*f(N[i]+k3,t[i]+0.5*h)
        N[i+1]=N[i]+(k1+2*k2+2*k3+k4)/6 
    return N, t
#se aplica el metodo con un valor de n=1000, condiciones iniciales n01=1.5 y n02=1.0
N,t=RK4(F, np.array([1.5, 1]), 0., 12., 1000) #se definen los valores arrojados por el RK4 de las poblaciones y a su vez el arreglo temporal globlal para las graficas
n1k4=N[:,0]
n2k4=N[:,1] #Soluciones que arroja el metodo RK4 para las poblaciones de las particulas


#Usando metodo de scipy odeint
def f(sl, t): #de nuevo se define el sistema de ecuaciones dentro de esta funcion
    n1,n2=sl
    return n1*(a-b*n2), -n2*(c-d*n1)
sl0=[1.5,1] #condiciones iniciales del problema
sls=odeint(f,sl0,t)#se usa el mismo t definido por el RK4
n1Od=sls[:,0] #soluciones arrojados por odeint, se consideraran estas como exactas
n2Od=sls[:,1]


#Usando metodo de euler
def F(N,t):#definicion dentro de una funcion del sistema de ecuaciones
    n1,n2=N
    return np.array([n1*(a-b*n2), -n2*(c-d*n1)])
#se define el metodo de euler 
def euler(f,u0,t0,tf,n):
    t=np.linspace(t0,tf,n+1)
    N=np.array((n+1)*[u0])
    h=t[1]-t[0]       
    for i in range(n):
        k1=h*f(N[i],t[i])    
        N[i+1]=N[i]+(k1)
    return N, t
#se aplica el metodo con un valor de n=1000, condiciones iniciales n01=1.5 y n02=1.0
N,t=euler(F, np.array([1.5, 1]), 0., 12., 1000) #se definen los valores arrojados por el metodo de euler de las poblaciones y a su vez el arreglo del tiempo para las graficas
n1Eu=N[:,0]
n2Eu=N[:,1] #Soluciones que arroja el metodo euler para las poblaciones de las particulas

####################################################################
####################################################################

#Grafica de las soluciones

#Graficando para el metodo de scipy odeint
#Grafica en los planos t,n1 y t,n2
plt.figure(figsize=(10,5))
N1Od=plt.plot(t,n1Od, c="red",label="Poblacion 1 ")
N2Od=plt.plot(t,n2Od, c="blue",label="Poblacion 2")
plt.legend(fontsize=10)
plt.xlabel("Tiempo")
plt.ylabel("Poblacion de particulas")
plt.xlim(0,12)
plt.ylim(0,2)
plt.grid(True)
plt.title("Poblaciones de las particulas en el tiempo usando Odeint")
plt.savefig("Figura1")
#plt.show()

#Grafica en los planos n1,n1
plt.figure(figsize=(10,5))
NHG=plt.plot(n2Od,n1Od, c="blue")
plt.xlim(0,12)
plt.ylim(0,2)
plt.ylabel("Poblacion 1")
plt.xlabel("Poblacion 2")
plt.grid(True)
plt.title("Grafica en el plano n1,n2 usando Odeint")
plt.savefig("Figura2")
#plt.show()

#Graficando para el metodo RK4
#Grafica en los planos t,n1 y t,n2
plt.figure(figsize=(10,5))
N1k4=plt.plot(t,n1k4, c="red",label="Poblacion 1 ")
N2k4=plt.plot(t,n2k4, c="blue",label="Poblacion 2")
plt.legend(fontsize=10)
plt.xlabel("Tiempo")
plt.ylabel("Poblacion de particulas")
plt.xlim(0,12)
plt.ylim(0,2)
plt.grid(True)
plt.title("Poblaciones de las particulas en el tiempo usando RK4")
plt.savefig("Figura3")
#plt.show()

#Grafica en los planos n1,n1
plt.figure(figsize=(10,5))
NHGk=plt.plot(n2k4,n1k4, c="blue")
plt.xlim(0,12)
plt.ylim(0,2)
plt.ylabel("Poblacion 1")
plt.xlabel("Poblacion 2")
plt.grid(True)
plt.title("Grafica en el plano n1,n2 usando RK4")
plt.savefig("Figura4")
#plt.show()

#Graficando para el metodo euler
#Grafica en los planos t,n1 y t,n2
plt.figure(figsize=(10,5))
N1Eu=plt.plot(t,n1Eu, c="red",label="Poblacion 1 ")
N2Eu=plt.plot(t,n2Eu, c="blue",label="Poblacion 2")
plt.legend(fontsize=10)
plt.xlabel("Tiempo")
plt.ylabel("Poblacion de particulas")
plt.xlim(0,12)
plt.ylim(0,2)
plt.grid(True)
plt.title("Poblaciones de las particulas en el tiempo usando metodo de euler")
plt.savefig("Figura5")
#plt.show()

#Grafica en los planos n1,n1
plt.figure(figsize=(10,5))
NHGk=plt.plot(n2Eu,n1Eu, c="blue")
plt.xlim(0,12)
plt.ylim(0,2)
plt.ylabel("Poblacion 1")
plt.xlabel("Poblacion 2")
plt.grid(True)
plt.title("Grafica en el plano n1,n2 usando metodo de euler")
plt.savefig("Figura6")
#plt.show()

###################################################################################################
###################################################################################################

#prueba de convergencia
#Se implementa el RK4 y el metodo de euler para diferentes valores del paso h, luego se escoge el valor maximo de la lista de 
#errores derivada del valor absoluto de las soluciones por el metodo y las que se toman como exactas y se grafican estos 
#en funcion del paso h

#En este ciclo se hace la lista de los valores del paso h
tf=12.
t0=0.
H=[]
for n in (10,100,1000,10000,100000):
    h=(tf-t0)/n
    H.append(h)
    n=n+1

#Prueba para el metodo RK4 y la particion t [0,12]
Errores1k4=[]
Errores2k4=[]
for j in H:
    N,t=RK4(F, np.array([1.5, 1]), 0., 12.,int(12/j) ) #se definen los valores arrojados por el RK4 de las poblaciones y a su vez el arreglo temporal globlal para las graficas
    n1k4=N[:,0]
    n2k4=N[:,1]
    sl0=[1.5,1] #condiciones iniciales del problema
    sls=odeint(f,sl0,t)#se usa el mismo t definido por el RK4
    n1Od=sls[:,0] #soluciones arrojados por odeint, se consideraran estas como exactas
    n2Od=sls[:,1]
    Err1=np.abs(n1k4-n1Od)
    Err2=np.abs(n2k4-n2Od)
    Errores1k4.append(max(Err1))
    Errores2k4.append(max(Err2))

#Prueba para el metodo de euler y la particion t [0,12]
Errores1Eu=[]
Errores2Eu=[]
for l in H:
    N,t=euler(F, np.array([1.5, 1]), 0., 12., int(12/l)) #se definen los valores arrojados por el metodo euler de las poblaciones y a su vez el arreglo del tiempo para las graficas
    n1Eu=N[:,0]
    n2Eu=N[:,1]
    sl0=[1.5,1] #condiciones iniciales del problema
    sls=odeint(f,sl0,t)
    n1Od=sls[:,0] #soluciones arrojados por odeint, se consideraran estas como exactas
    n2Od=sls[:,1]
    Err1=np.abs(n1Eu-n1Od)
    Err2=np.abs(n2Eu-n2Od)
    Errores1Eu.append(max(Err1))
    Errores2Eu.append(max(Err2))

#se grafican los maximos de la lista de errores en funcion del paso h, asi se garantiza que los demas convergen igualmente a cero
#grafica para los errores del metodo RK4
plt.figure(figsize=(10,5))
A=plt.plot(H,Errores1k4, c="green", label='Error en la poblacion 1')
B=plt.plot(H,Errores2k4, c="black", label='Error en la poblacion 2')
plt.ylabel("Error")
plt.xlabel("Valor de h")
plt.grid()
plt.legend()
plt.title("Error del metodo RK4 para valores del paso h")
plt.savefig("Figura7")
#plt.show()

#grafica para los errores del metodo de euler
plt.figure(figsize=(10,5))
C=plt.plot(H,Errores1Eu, c="green", label='Error en la poblacion 1')
D=plt.plot(H,Errores2Eu, c="black", label='Error en la poblacion 2')
plt.ylabel("Error")
plt.xlabel("Valor de h")
plt.grid()
plt.legend()
plt.title("Error del metodo de euler para valores del paso h")
plt.savefig("Figura8")
#plt.show()

#de estas graficas se puede observar que ambos metodos convergen ya que el valor del error tomando el odeint como
#la solucion exacta se hace cero mediante h se acerca a cero
