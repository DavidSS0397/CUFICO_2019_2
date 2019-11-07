import matplotlib.pyplot as plt
import numpy as np

def ES(x):
    return x-1+2*np.exp(-x)


x,y = np.loadtxt('RK6.txt', unpack=True)

X=np.linspace(0.,5.,10000)


fig = plt.figure(figsize=(12, 4))

ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)

ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_title('Interesting Graph\nCheck it out')
ax0.plot(X,ES(X),'r--')
ax0.plot(x,y, label='Loaded from file!')
plt.grid()

ax1.set_xlabel('E')
ax1.set_ylabel('x')
ax1.set_title('Error')
E=np.abs(ES(X)-y[:10000]) 
ax1.semilogy(X,E,'--')
plt.grid()

plt.show()

