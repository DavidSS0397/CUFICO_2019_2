import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing data from c++ code
data = pd.read_csv('rk6.txt', names=['x', 'y_rk6', 'y_exact', 'diff_rk6'])

#Defining Points
numPoints=np.array([10, 100, 1000, 10000])
x0=0.0; xf=5.
h = (xf-x0)/numPoints

#Defining mean difference with c++ data 
diff_all = np.array([np.mean(np.array(data.iloc[0:10,3])), np.mean(np.array(data.iloc[11:110,3])), 
	np.mean(np.array(data.iloc[111:1110,3])), np.mean(np.array(data.iloc[1111:11110,3]))])

#ploting data
fig = plt.figure(figsize=(8,4))
ax0 = fig.add_subplot(131); ax1 = fig.add_subplot(132)
ax2 = fig.add_subplot(133)

#first subplot 
ax0.plot(data.iloc[111:1110,0], data.iloc[111:1110,1], 'm-', label='rk6 sol')
ax0.plot(data.iloc[111:1110,0], data.iloc[111:1110,2], 'c--', label='exact sol')
ax0.set_xlabel('x'); ax0.set_ylabel('y') 
ax0.legend()

#second subplot
ax1.semilogy(data.iloc[111:1110,0], data.iloc[111:1110,3], 'm-', label='rk6 diff')
ax1.set_xlabel('x'); ax1.set_ylabel(r'log|$y_{exact}$ - $y_{num}$|') 
ax1.legend()

#third subplot
ax2.plot(h, diff_all, 'm-')
ax2.set_xlabel('h'); ax2.set_ylabel('mean difference')

plt.tight_layout()
plt.show()
