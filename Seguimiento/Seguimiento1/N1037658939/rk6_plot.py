import numpy as np
import matplotlib.pyplot as plt

"""
Plots solution of ODE for different
number of steps using C++ RK6.

By: Carolina Herrera
Last update: september 18, 2019
"""

x_10, y_rk6_10, y_exact_10, diff_10 = np.loadtxt('data10.txt', unpack=True, delimiter=',')
x_100, y_rk6_100, y_exact_100, diff_100 = np.loadtxt('data100.txt', unpack=True, delimiter=',')
x_1000, y_rk6_1000, y_exact_1000, diff_1000 = np.loadtxt('data1000.txt', unpack=True, delimiter=',')
x_10000, y_rk6_10000, y_exact_10000, diff_10000 = np.loadtxt('data10000.txt', unpack=True, delimiter=',')

h = np.array([10, 100, 1000, 10000])
h = (x_10[-1]-x_10[0])/h

diff_mean = [np.mean(diff_10), np.mean(diff_100), np.mean(diff_1000), np.mean(diff_10000)]

fig, ax = plt.subplots(1, 3)

ax[0].plot(x_10, y_rk6_10, 'g', label='RK6 10')
ax[0].plot(x_100, y_rk6_100, 'r', label='RK6 100')
ax[0].plot(x_1000, y_rk6_1000, 'y', label='RK6 1000')
ax[0].plot(x_10000, y_rk6_10000, 'm', label='RK6 10000')
ax[0].plot(x_10000, y_exact_10000, '--k', label='exact')
ax[0].title.set_text('Solution')
ax[0].grid()
ax[0].legend()

ax[1].semilogy(x_10, diff_10, 'g', label='10')
ax[1].semilogy(x_100, diff_100, 'r', label='100')
ax[1].semilogy(x_1000, diff_1000, 'y', label='1000')
ax[1].semilogy(x_10000, diff_10000, 'm', label='10000')
ax[1].title.set_text('Log Error')
ax[1].grid()
ax[1].legend()

ax[2].plot(h, diff_mean, 'b')
#ax[2].plot(h, diff_mean, 'og')
ax[2].title.set_text('Mean of absolute difference')
ax[2].grid()

plt.show()
