import matplotlib.pyplot as plt
import numpy as np

def exact_solution(xe):
	return (np.exp(xe)*xe-1*np.exp(xe)+2)/np.exp(xe)
	
x,y = np.loadtxt('RK6.txt', unpack=True)
ye=exact_solution(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solucion exacta y RK6')
plt.plot(x,ye, label= 'Solucion exacta', color='red')
plt.plot(x,y, label='Solucion RK6', color='green')
plt.legend()
plt.grid()
plt.show()
yer=np.abs(ye-y)/y
plt.semilogy(x,yer, label='Diferencia entre los metodos', color='black')
plt.grid()
plt.title("Error")
plt.xlabel('x')
plt.ylabel('log(y)')
plt.show()


