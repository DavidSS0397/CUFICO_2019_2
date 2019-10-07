#------
# Interaccion entre las particulas de dos gases 
# Verificamos convergencia de metodos de integracion Euler y RK4
# Además de el punto ideal donde la ODE se puede considerar la exacta.
#------

#------ Librerias 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

#------ Metodos
a = b = c = d = 1  #Constantes de las ecuaciones

def Euler(tn, yn, h, MyF):  #Solucion por Euler
	xn1, xn2 = yn
	x1 = xn1 + h*MyF(yn, tn, a, b, c, d)[0]
	x2 = xn2 + h*MyF(yn, tn, a, b, c, d)[1] 
	return [x1, x2] #Retorna una lista. x1 para los valores del gas 1 y x2 para el gas 2

#Para RK4 hacemos lo mismo, recibe listas y devuelve un array con las dos soluciones, x1 y x2:
def RK4(tn, yn, h, MyF):
	yn = np.array(yn)
	k1 = np.array(MyF(yn, tn, a, b, c, d))
	k2 = np.array(MyF(yn + 0.5*k1*h, tn+0.5*h, a, b, c, d))
	k3 = np.array(MyF(yn + 0.5*k2*h, tn+0.5*h, a, b, c, d))
	k4 = np.array(MyF(yn + h*k3, tn+h, a, b, c, d))

	return yn+(k1+ 2*k2 + 2*k3 + k4)*(h/6.)

#------Funcion de interaccion 

def gases(y, t, a, b, c, d):
	n1, n2 = y 
	dn2 = -n2*(c - d*n1); dn1 = n1*(a - b*n2)
	return [dn1, dn2]  #De nuevo devolvemos una lista con las dos ecuaciones

#-------- Condiciones y parametros

xi = 0.0; xf = 12.0 #Condiciones inicial y final para x
DT = [0.1, 0.01, 0.001, 0.0001] ##Numero de pasos, esto nos servirá para evaluar convergencia
y0 = [1.5 , 1.0] #Más condiciones iniciales pero para y
parm = (1,1,1,1) #Parametros que seran entrada del odeint

diff_Euler=[] #Para guardar las diferencias entre Euler y ODE
diff_RK4=[]   #Para guardar las diferencias entre RK4 y ODE

Total_time = []  #Para guardar los datos del tiempo
Total_ode = []   #Soluciones del ODE para ambos gases (una lista cuyos elementos son arrays con las series de tiempo de n1 y n2)
Total_euler = [] #Soluciones de Euler para ambos gases (")
Total_rk4 = []   #Soluciones de rk4 para ambos gases (")

Totaldiff_euler = [] #Diferencia de euler y Ode de los dos gases
Totaldiff_rk4 = []   #Diferencia con de rk4 y Ode de los dos gases

for dt in DT: #Para dt en 0.1, 0.01...

	time = np.arange(xi, xf, dt) #como un linspace pero no tan melo es decir, el intervalo de x dividido en dt partes
	Total_time.append(time)      #Guardamos el tiempo para graficarlo despues

	#------ Solucion con Odeint 
	ode_sol = odeint(gases, y0, time, args=parm) #solucion con odeint para dt actual
	Total_ode.append(ode_sol) # Agregamos solucion actual al total

	#------ Solucion con metodos propuestos
	Euler_sol = [] #Soluciones inmediatas de euler y RK4
	RK4_sol = []

	Euler_sol.append(y0) #Agruegamos la condicion inicial
	RK4_sol.append(y0)

	for i in time[1:]: #Iteramos las soluciones desde time 1 hasta time final
                 #Soluciones punto a punto:
		eu_sol = Euler(i, Euler_sol[-1], dt, gases)
		rk4_sol = RK4(i, RK4_sol[-1], dt, gases)

                #Agruegamos las soluciones punto a punto a las listas
		Euler_sol.append(eu_sol)
		RK4_sol.append(rk4_sol)

        #Agruegamos las listas como arrays a otras listas (una lista de arrays)
        #Para tener las soluciones de x1 y x2 compactas
	Total_euler.append(np.array(Euler_sol))
	Total_rk4.append(np.array(RK4_sol))

        #Restamos las listas Euler y Ode elemento a elemento y tomamos su valor absoluto para la diferencia total y así verificar convergencia. 
	Totaldiff_euler.append(np.abs(np.array(Euler_sol)-ode_sol))
	Totaldiff_rk4.append(np.abs(np.array(RK4_sol)-ode_sol))

#------ Convergencia en los máximos de la solución de odeint para mirar el paso óptimo, donde podemos decir que el error se vuelve despreciable.

#Ya vimos la gráfica y notamos que tiene 2 máximos y 2 minimos, así que para tomar solo uno de los máximos numericos, acotamos el intervalo de evaluación del maximo para cada una de las soluciones (diferenciando entre n1 y n2)

Ode_convergencen1=[np.max(Total_ode[0][50:,0])-np.max(Total_ode[1][500:,0]),
	np.max(Total_ode[1][500:,0])-np.max(Total_ode[2][5000:,0]), np.max(Total_ode[2][5000:,0])-np.max(Total_ode[3][50000:,0])]

Ode_convergencen2=[np.max(Total_ode[0][:50,1])-np.max(Total_ode[1][:500,1]),
	np.max(Total_ode[1][:500,1])-np.max(Total_ode[2][:5000,1]), np.max(Total_ode[2][:5000,1])-np.max(Total_ode[3][:50000,1])]

#Definimos la convergencia de Ode mirando cuando el error (la resta del máximo con n puntos con el maximo con menos puntos, un n menor) es menor al umbral determinado por nosotros
Ode_convergencen1 = np.abs(Ode_convergencen1)
Ode_convergencen2 = np.abs(Ode_convergencen2)

epsilon = 1e-5 #Umbral de diferencia determinado por nosotros, es donde creemos que el error es despreciable

k=1 # Posición del dt optimo
for l,m in zip(Ode_convergencen1,Ode_convergencen2): #recorremos todos los valores de convergencia para n1 y n2
	if (l<epsilon and m<epsilon): #cuando ambos cumplan con el umbral, entonces el dt es optimo
		print("Paso que cumple nuestro criterio de convergencia es: ", DT[k])
		break
	k+=1

#------- Convergencia métodos 

mean_n1 = [] #Lista paraa guardar la media de las diferencias entre ode y un método 
mean_n2 = [] #rk4 o euler

#Mean tendrá 4 tuplas de 2 elementos cada una
for i in range(0, len(DT)):
        #Anexamos a mean la media de la diferencia en el dt[i] para euler y rk4
	mean_n1.append((np.mean(Totaldiff_euler[i][:,0]), np.mean(Totaldiff_rk4[i][:,0])))
	mean_n2.append((np.mean(Totaldiff_euler[i][:,1]), np.mean(Totaldiff_rk4[i][:,1])))

mean_n1 = np.array(mean_n1) #Volvemos array para graficar
mean_n2 = np.array(mean_n2)

#------- Graficas

fig = plt.figure(figsize=(12,6)) #Tamaño de la figura total

#6 figuras:
ax0 = fig.add_subplot(231); ax3 = fig.add_subplot(234)
ax1 = fig.add_subplot(232); ax4 = fig.add_subplot(235)
ax2 = fig.add_subplot(233); ax5 = fig.add_subplot(236)

#Soluciones para n1
ax0.plot(Total_time[k], Total_ode[k][:,0], 'k-', label="ode_sol") #Recordemos que en la posición k está el paso ideal, así que tomamos ese punto. 
ax0.plot(Total_time[k], Total_euler[k][:,0], 'c-.', label="euler_sol")
#De la posición k, graficamos todos los valores para el gas 1, la primera tupla, es decir  [k][:,0]
ax0.plot(Total_time[k], Total_rk4[k][:,0], 'm--',label="rk4_sol")
ax0.set_ylabel(r'$n_1 (t)$')
ax0.set_xlabel("Tiempo")
ax0.grid() #Grid para que se vea mas pispo
ax0.legend()

#Soluciones para n2
ax1.plot(Total_time[k], Total_ode[k][:,1], 'k-', label="ode_sol")
#De la posición k, graficamos todos los valores para el gas 2, la primera tupla, es decir  [k][:,1]
ax1.plot(Total_time[k], Total_euler[k][:,1], 'c-.', label="euler_sol")
ax1.plot(Total_time[k], Total_rk4[k][:,1], 'm--',label="rk4_sol")
ax1.set_ylabel(r'$n_2 (t)$')
ax1.set_title("Soluciones n1 y n2 con paso óptimo ") #Titulo de las gráficas de arriba
ax1.set_xlabel("Tiempo")
ax1.grid()
ax1.legend()

#Grafica n1 vs n2
ax2.plot(Total_ode[k][:,0], Total_ode[k][:,1], 'k-', label="ode_sol")
#En la tupla 0 están las soluciones del gas 1 y en la 1 está el gas 1
ax2.plot(Total_euler[k][:,0], Total_euler[k][:,1], 'c-.', label="euler_sol")
ax2.plot(Total_rk4[k][:,0], Total_rk4[k][:,1], 'm--',label="rk4_sol")
ax2.set_ylabel(r'$n_2 (t)$')
ax2.set_xlabel(r'$n_1 (t)$')
ax2.grid()
ax2.legend()

#Convergencia n1 y n2 de la solucion ode:
ax3.loglog(DT[1:], np.abs(Ode_convergencen1), 'k-', label='convergencia odeint n1')
#log log nos da más información. graficamos los pasos versus la convergencia de ode
ax3.loglog(DT[1:], np.abs(Ode_convergencen2), 'k-.', label='convergencia odeint n2')
ax3.set_ylabel("Diferencia con paso anterior")
ax3.set_xlabel("dt (paso)")
ax3.grid()
ax3.legend()

#el tiempo con paso optimo k vs la diferencia entre euler y ode para n1 y n2
ax4.semilogy(Total_time[k], Totaldiff_euler[k][:,0], 'b-.', label='euler n1')
ax4.semilogy(Total_time[k], Totaldiff_euler[k][:,1], 'c-.', label='euler n2')
#el tiempo con paso optimo k vs la diferencia entre rk4 y ode para n1 y n2
ax4.semilogy(Total_time[k], Totaldiff_rk4[k][:,0], 'r-', label='rk4 n1')
ax4.semilogy(Total_time[k], Totaldiff_rk4[k][:,1], 'm-', label='rk4 n2')
ax4.set_ylabel("diferencia con odeint")
ax4.set_xlabel("Tiempo")
ax4.set_title(" Gráficas para visualizar los criterios de convergencia ")#titulo gráficas de abajo
ax4.grid()
ax4.legend()

#Convergencia de las soluciones: numero de pasos vs la media del error
#Con esto demostramos que los metodos si convergen con respecto a la solucion de odeint
ax5.semilogy(DT, mean_n1[:,0], 'b-.', label='conv euler n1')
ax5.semilogy(DT, mean_n2[:,0], 'c-.', label='conv euler n2')
ax5.semilogy(DT, mean_n1[:,1], 'r-', label='conv rk4 n1')
ax5.semilogy(DT, mean_n2[:,1], 'm-', label='conv rk4 n2')
ax5.set_ylabel("Promedio de las diferencias")
ax5.set_xlabel("dt (paso)")
ax5.grid()
ax5.legend()

plt.tight_layout() #Para separar bien y que no se junten las gráficas
plt.show()
