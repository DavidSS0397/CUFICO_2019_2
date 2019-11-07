# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:53:04 2019

@author: Samuel
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import os 


os.system("g++ -o RK6 Runge-Kutta-6.cpp && ./RK6")

datos = pd.read_csv("RK6.csv", sep=" ")

X=datos['X']
Y=datos['Y']
YE=datos['YE']
Diff=datos['Diff']


xf=5.
x0=0

Num=np.array([10,100,1000,10000])
h=(xf-x0)/Num

ax0=plt.subplot(131)
ax1=plt.subplot(132)
ax2=plt.subplot(133)


#se grafica los resultados para distintos numeros de puntos, lo que cambia también el paso 
ax0.plot(X.iloc[112:1113],YE.iloc[112:1113],'r',label= 'Exacta')
ax0.plot(X.iloc[0:11],Y.iloc[0:11],'g--',label= 'Nump=10')
ax0.plot(X.iloc[11:112],Y.iloc[11:112],'b--',label='Nump=100')
ax0.plot(X.iloc[112:1113],Y.iloc[112:1113],'c--',label= 'Nump=1000')
ax0.plot(X.iloc[1113:11114],Y.iloc[1113:11114],'m',label= 'Nump=10000')
ax0.set_ylabel("y")
ax0.set_xlabel("x")

ax0.legend()


ax1.semilogy(X[0:11],Diff[0:11],'r--',label= 'Nump=10-err')
ax1.semilogy(X[11:112],Diff[11:112],'b--',label= 'Nump=100-err')
ax1.semilogy(X[112:1113],Diff[112:1113],'c--',label= 'Nump=1000-err')
ax1.semilogy(X[1113:11114],Diff[1113:11114],'m--',label= 'Nump=10000-err')
ax1.set_ylabel("Error")
ax1.set_xlabel("x")

ax1.legend()

DifP=[]

DifP.append(np.mean(Diff[0:11]))
DifP.append(np.mean(Diff[11:112]))
DifP.append(np.mean(Diff[112:1113]))
DifP.append(np.mean(Diff[1113:11114]))

ax2.plot(h,DifP,label='Error vs Paso')
ax2.set_xlabel("h")
ax2.set_ylabel("Prom-err")
ax2.legend()

plt.show()





