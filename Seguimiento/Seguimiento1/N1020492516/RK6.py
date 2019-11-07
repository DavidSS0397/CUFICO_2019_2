import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.system("g++ -o RK6 RK6.cpp && ./RK6 > RK6.csv")

rk = pd.read_csv('RK6.csv')
print(rk.head())

NumPuntos=np.array([10,100,1000,10000]) #Para ver como se acerca la solución a la exacta
xi=0.
xf=5.
y0=1.0
h=(xf-xi)/NumPuntos

fig = plt.figure(figsize = (12, 4))
ax0= fig.add_subplot(131)
ax1= fig.add_subplot(132)
ax2= fig.add_subplot(133)

ax0.plot(rk.iloc[0:10000,0],rk.iloc[0:10000,1],label='Solución RK6')
ax0.plot(rk.iloc[0:10000,0],rk.iloc[0:10000,2],label='Solución Exacta')
ax0.legend()
ax0.grid()
ax0.set_xlabel('X')
ax0.set_ylabel('Y')
ax0.set_title('Soluciones')

ax1.plot(rk.iloc[0:10000,0],rk.iloc[0:10000,3],label='Diferencia')
ax1.legend()
ax1.grid()
ax1.set_xlabel('X')
#ax1.set_ylabel('|Yexacta - Yrk6|')
ax1.set_title('Diferencia')

yrk_difference=[]
yrk_difference.append(np.mean(np.abs(rk.iloc[0:10000,1] - rk.iloc[0:10000,2])))
yrk_difference.append(np.mean(np.abs(rk.iloc[10000:20000,1] - rk.iloc[10000:20000,2])))
yrk_difference.append(np.mean(np.abs(rk.iloc[20000:30000,1] - rk.iloc[20000:30000,2])))
yrk_difference.append(np.mean(np.abs(rk.iloc[20000:30000,1] - rk.iloc[20000:30000,2])))

ax2.plot(h,yrk_difference,label='Runge Kutta 6')
ax2.legend()
ax2.grid()
ax2.set_xlabel('h (Paso)')
#ax2.set_ylabel('|Yexacta - Yrk6|')
ax2.set_title('Divergencia')

plt.show()
