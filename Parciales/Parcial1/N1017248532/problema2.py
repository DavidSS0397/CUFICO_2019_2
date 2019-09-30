import numpy as np # Numpy will be used for its arrays and functions
import matplotlib.pyplot as plt # Matplotlib will be used as graph tool
from scipy.integrate import odeint # Odeint to integrate the ODE system


# Euler integration method
def Euler(yn,tn,h,F):
    ''' Yn: array of the state of each system [n1,n2]. tn: time. h:method's step. F: coupled differential equations, F[0] corresponds to the equation for n1' and F[1] corresponds to the equation for n2' .'''
    y1_np1 = yn[0] + h*F(yn,tn)[0] # Evolution of the gas system n1 (here, denoted
                                   # as y1)
    y2_np1 = yn[1] + h*F(yn,tn)[1] # Evolution of the gas system n2 (here, denoted
                                   # as y2) 

    return [y1_np1, y2_np1] # Array with the updated values for the next step

# Runge-Kutta integration method
def RK4(yn,tn,h,F):
    ''' This method is generalized as the Euler method. Each dependent variable needs its set of K values, denoted K*_1 and K*_2, where * corresponds to each coeffitient for RK4. Inptus are the same as in the Euler method. It must be noted that the K values for each dependen variable must be calculated with the corresponding ODE that describes its evolution, that is, F[0] for the K*_1, and F[1] for the K*_2  '''

    # Calculation of each K-value for the dependent variables, E.g., K2_1 is the K2 coeffitient of the dependent variable y1, while K1_2 is the K1 coeffitient of the dependent variable y2.
    k1_1,k1_2 = h*F([yn[0],yn[1]],tn)[0], h*F([yn[0], yn[1]], tn)[1] 
    k2_1, k2_2 = h*F([yn[0] + h*0.5*k1_1,yn[1] + h*0.5*k1_2], tn + 0.5*h)[0], h*F([yn[0] + h*0.5*k1_1,yn[1] + h*0.5*k1_2], tn + 0.5*h)[1]
    k3_1, k3_2 = h*F([yn[0] + h*0.5*k2_1,yn[1] + h*0.5*k2_2], tn + 0.5*h)[0], h*F([yn[0] + h*0.5*k2_1,yn[1] + h*0.5*k2_2], tn + 0.5*h)[1]
    k4_1, k4_2 = h*F([yn[0] + h*k3_1,yn[1] + 5*k3_2], tn + h)[0], h*F([yn[0] + h*k3_1,yn[1] + h*k3_2], tn + h)[1]

    return [yn[0] + (k1_1  + 2*k2_1 + 2*k3_1 + k4_1)/6, yn[1] + (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)/6] # Array with the updated values for the next stem


# System class, which contains the information of the state of the two gases
class System:
    def __init__(self,g1_0, g2_0, method):
        ''' Class constructor takes que initial states of each gas, g1_0 and g2_0, and the method that will integrate the evolution ODE.  '''
        self.g1 = [g1_0] # Initial condition for gas 1. It is an array in order to append the subsequent states
        self.g2 = [g2_0] # Initial condition for gas 2
        
        self.method = method # Method of integration
        
    def F(self,y,t):
        ''' This is the system of coupled ODEs that describes the rate of evolution of the system. Yakes as input an array of the states [y1,y2], and the time t '''
        rh = np.zeros_like(y) # array of zeros with the shape of Y

        rh[1] = -y[1]*(1-y[0]) # ODE for gas 2
        rh[0] = y[0]*(1-y[1]) # ODE for gas 1


        return rh # array of the rates of evolition for gas 1 and gas 2 respectively

    def evolve(self,t):
        ''' Function that evolves the system, over a temporal interval t=[t_i,t_f]  '''
        
        h = t[1]-t[0] # the step taken for the integration method
        
        for i in t[:-1]: # last value of t is not used, as it is the final state
            y = self.method([self.g1[-1],self.g2[-1]], i, h, self.F) # Evolution of the states
            self.g1.append(y[0]) # updates state of gas 1
            self.g2.append(y[1]) # updates state of gas 2

        self.g1 = np.array(self.g1) # transforms the array to a list to perform vector like calculations
        self.g2 = np.array(self.g2) # transforms the array to a list to perform vector like calculations



mean_div_euler = [] # list to store the divergence of the Euler method for varous steps
mean_div_rk4 = [] # list to store the divergence of the RK4 method for varous steps

t = [] # Time array

dt = [1,0.1,0.01,0.001,0.0001] # array of time steps
#dt = [1.2,0.12,0.012]

counter = 0
for i in dt:
    
    sys_euler = System(1.50,1.00,Euler) # system class for the Euler integrator, with initial conditions n1=1.50, n2=1.00
    sys_rk4 = System(1.50,1.00,RK4)# system class for the RK4 integratrpr, with same initial conditions as above

    t = np.arange(0,12 + i,i) # time array, with step size defined by the iterating variable i

    sys_euler.evolve(t) # evolve the system of the Euler integrator over t
    sys_rk4.evolve(t) # evolve the system of the RK4 integrator over t
    y_od = odeint(sys_euler.F, [sys_euler.g1[0], sys_euler.g2[0]], t) # evolve a new system (not in a class) with same initial conditions, with Odeint integrator, we use the function and initial conditions for the system that uses the euler method, because the functions and initial conditions are independent of the method used
    
    y_od_g1 = y_od[:,0] # Integrated solutions for the gas 1
    y_od_g2 = y_od[:,1] # integrated solutions fot the gas 2
    
    #Defining divergence:
    sys_euler.g1_diff = np.abs(sys_euler.g1 - y_od_g1) # Mean difference between the solutions for the gas 1 with the Euler integrator and Odeint integrator
    sys_euler.g2_diff = np.abs(sys_euler.g2 - y_od_g2) # Mean difference between the solutions for the gas 2 with the Euler integrator and Odeint integrator

    mean_div_euler.append(np.mean((sys_euler.g1_diff+sys_euler.g2_diff)/2)) # divergence is the mean of the mean differences of gas 1 and gas 2 for the whole step
    
    sys_rk4.g1_diff = np.abs(sys_rk4.g1 - y_od_g1) # Mean difference between the solutions for the gas 1 with the RK4 integrator and Odeint integrator
    sys_rk4.g2_diff = np.abs(sys_rk4.g2 - y_od_g2) # Mean difference between the solutions for the gas 2 with the RK4 integrator and Odeint integrator
    mean_div_rk4.append(np.mean((sys_rk4.g1_diff+sys_rk4.g2_diff)/2)) # divergence is the mean of the mean differences of gas 1 and gas 2 for the whole step 
    

'''
We first calculated the mean divergence for each step size. We choose the optimal step size as the one for which the divergence is minimal.
The plots for the solutions and the difference between euler/rk4 and odeint) will be made with this optimal step size. We also included a plot of
mean absolute divergen in function of the step size.
'''
# solution of the system with the optimal step size.
    
sys_rk4 = System(1.50,1.00,RK4) # system class for the Euler integrator, with initial conditions n1=1.50, n2=1.00
sys_euler = System(1.50,1.00,Euler) # system class for the RK4 integrator, with initial conditions n1=1.50, n2=1.00

sys_rk4.dt_opt = dt[np.where(mean_div_rk4 == min(mean_div_rk4))[0][0]] # optimal step size is selected comparing the position of the minimum divergnce and the dt array
sys_euler.dt_opt = dt[np.where(mean_div_euler == min(mean_div_euler))[0][0]] # optimal step size is selected comparing the position of the minimum divergnce and the dt array

sys_rk4.t_opt = np.arange(0,12+sys_rk4.dt_opt, sys_rk4.dt_opt) # time array with optimal step size is contructed
sys_euler.t_opt = np.arange(0,12+sys_euler.dt_opt, sys_rk4.dt_opt) # time array with optimal step size is contructed

sys_euler.evolve(sys_euler.t_opt) # the system of the Euler integrator is evolved according to the time array with the optimal step size
sys_rk4.evolve(sys_rk4.t_opt) # the system of the RK4 integrator is evolved according to the time array with the optimal step size

sys_rk4.y_od = odeint(sys_rk4.F, [sys_rk4.g1[0], sys_rk4.g2[0]], sys_rk4.t_opt) # the system is evolved with the Odeint integrator in order to make the comparation with rk4 method
sys_euler.y_od = odeint(sys_euler.F, [sys_euler.g1[0], sys_euler.g2[0]], sys_euler.t_opt) # the system is evolved with the Odeint integrator in order to make the comparation with euler method

    
#Defining divergence:
sys_euler.g1_diff = np.abs(sys_euler.g1 - sys_euler.y_od[:,0]) # Difference between the solutions for the gas 1 with the Euler integrator and Odeint integrator
sys_euler.g2_diff = np.abs(sys_euler.g2 - sys_euler.y_od[:,1]) # Difference between the solutions for the gas 2 with the Euler integrator and Odeint integrator

    
sys_rk4.g1_diff = np.abs(sys_rk4.g1 - sys_rk4.y_od[:,0]) # Difference between the solutions for the gas 1 with the RK4 integrator and Odeint integrator
sys_rk4.g2_diff = np.abs(sys_rk4.g2 - sys_rk4.y_od[:,1]) # Difference between the solutions for the gas 2 with the RK4 integrator and Odeint integrator

# ------------------------------------------------------------------------------
# Plots

# Plot of the divergence and the difference

fig_d,ax_d = plt.subplots(nrows=1,ncols=2,figsize=(10,6)) # figure and axes for the divergence and difference plot

for div,dif,name in zip([mean_div_euler,mean_div_rk4],[sys_euler,sys_rk4],["Euler","RK4"]): # divergence and difference of each integration method are ploted on the cycle
    ax_d[0].plot(dt,div,label=name) # divergence plot
    ax_d[1].semilogy(dif.t_opt,(dif.g1_diff + dif.g2_diff)/2,label=name) # difference plot. Semilog scale on y is used for better vizualitation


ax_d[0].legend() # allows labels for plots
ax_d[0].set_xlabel("Step size") # x label for divergence plot
ax_d[0].set_ylabel("Mean absolute divergence") # y label for divergence plot
ax_d[0].set_xlim(dt[-1],dt[0]) # x limits for divergence plot
ax_d[0].set_ylim(0,max(mean_div_euler)) # y limits for divergence plot
ax_d[0].set_title("Divergence plot")

ax_d[1].set_xlabel("Time") # x label for difference plot
ax_d[1].set_ylabel("Mean absolute difference") # y label for difference plot
ax_d[1].set_title("Difference plot")
ax_d[1].legend() #allows labels for plots
fig_d.subplots_adjust(left=0.08,bottom=0.14,right=0.96,top=0.85,wspace=0.29,hspace=0.20) # sets the space configration of the plots on the figure


# Plot for time evolution

fig, axes = plt.subplots(3,3,figsize=(10,10)) # creates figur and axes for plot

for sys,ax,name in zip([sys_euler, sys_rk4],axes,["Euler","RK4"]):
    ax[0].plot(sys.t_opt, sys.g1,'-k') # plot of gas 1 vs time
    ax[1].plot(sys.t_opt, sys.g2,'-k') # plot of gas 2 vs time
    ax[2].plot(sys.g1, sys.g2,'-k') # plot of gas 2 vs gas 1

    ax[0].set_ylabel("Particles of gas 1") # y label for gas 1 vs time plot
    ax[0].set_xlabel("Time") # x label for gas 1 vs time plot
    ax[1].set_ylabel("Particles of gas 2") # y label for gas 2 vs time plot
    ax[1].set_xlabel("Time") # x label for gas 2 vs time plot
    ax[2].set_xlabel("Particles of gas 1") # x label for gas 2 vs gas 1 plot
    ax[2].set_ylabel("Particles of gas 2") # y label for gas 2 vs gas 1 plot

    ax[1].set_title(name+" state plots") # title for the plot

# plot of time evolution for Odeint integration method
axes[2,0].plot(t, y_od_g1,'-k') # gas 1 vs time plot
axes[2,1].plot(t, y_od_g2,'-k') # gas 2 vs time plot
axes[2,2].plot(y_od_g1, y_od_g2,'-k') # gas 2 vs gas 1 plot

axes[2,0].set_ylabel("Particles of gas 1") # y label for gas 1 vs time plot
axes[2,0].set_xlabel("Time") # x label for gas 1 vs time plot
axes[2,1].set_ylabel("Particles of gas 2") # y label for gas 2 vs time plot
axes[2,1].set_xlabel("Time") # x label for gas 2 vs time plot
axes[2,2].set_xlabel("Particles of gas 1") # x label for gas 2 vs gas 1 plot
axes[2,2].set_ylabel("Particles of gas 2") # y label for gas 2 vs gas 1 plot

axes[2,1].set_title("Odeint state plots") # title for the plot

fig.subplots_adjust(left=0.07,bottom=0.08,right=0.97,top=0.95,wspace=0.29,hspace=0.47)  # sets the space configration of the plots on the figure

plt.show() # shows all figures

fig_d.savefig("Problema2_Div_dif_plot.png", format="png") # save divergence and difference plot
fig.savefig("Problema2_states_plot.png", format="png") # save states plot

'''
We conclude that the solutions for both the euler and rk4 converge, as can be seen from the difference's plot and the small mean absolute
divergence for small step sizes.
'''
