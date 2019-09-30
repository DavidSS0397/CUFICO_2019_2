import numpy as np #For mathematical functions
import matplotlib.pyplot as plt #For graphing
from scipy.integrate import odeint as odeint #For numerical methods

n1Zero = 1.5#Initial condition for n1
n2Zero = 1.#Initial condition for n2
tZero = 0.#initial condition for the time
tFin = 0.12#final time
nArr = np.array([1e1,1e2,1e3,1e4])#Array with diferent posible numbers of step, you are welcome to add more entries to ensure divergence          
hArr = (tFin-tZero)/nArr#array with different widths of step for every number of steps
tLis = []#A list to store the sets of time

for i in range(0,nArr.size):#iterates over all the posible number of steps. This loop might take a while to end
    toAppend = np.arange(tZero,tFin,hArr[i])#creates a set of times for each stepsize from tZero to tFin
    tLis.append(toAppend)#Adds the set of times to the list

def sci(yPrime,xPrime,yN,xN,h,n):#a function that uses odeint to return the values of n1 and n2 (or x and y in any order)
    toReturnY = np.array([yN])#Adds the initial value to the Y array
    toReturnX = np.array([xN])#Adds the initial value to the X array
    yPlus = odeint(yPrime,yN,[xN,xN+h])[1]#calculates the first new value of y in the ssecond entry
    xPlus = odeint(xPrime,xN,[yN,yN+h])[1]#calculates the first new value of x in the ssecond entry
    toReturnY = np.append(toReturnY,yPlus)#appends the new value to the array to return
    toReturnX = np.append(toReturnX,xPlus)#appends the new value to the array to return
    xN = xPlus[0]#updates the x value
    yN = yPlus[0]#updates the y value
    n = int(n)#converts n from numpy64 to int to allow using range()
    for i in range(0,n-2):#iterates from 0 to n-2 because we already have two values
        yPlus = odeint(yPrime,yN,[xN,xN+h])[1]#calculates a new value of y in the ssecond entry
        xPlus = odeint(xPrime,xN,[yN,yN+h])[1]#calculates anew value of x in the second entry
        toReturnY = np.append(toReturnY,yPlus)#stores the new value of y
        toReturnX = np.append(toReturnX,xPlus)#stores the new value of x
        xN = xPlus[0]#updates the value of xn
        yN = yPlus[0]#updates the value of yn
    return toReturnX,toReturnY#returns the vectors with the values of n1 and n2
   
def n2Prime(n1,n2,c=1,d=1):#the diferential equation for the change in gas2
    return -n2*(c-d*n1)#returns the slope of n2 for n1 and n2. Note there is no explicit time dependency

def n1Prime(n1,n2,a=1,b=1):#the diferential equation for the change in gas2
    return n1*(a-b*n2)#returns the slope of n1 for n1 and n2. Note there is no explicit time dependency

def eulerMod(x,y,h,funk):#Euler method for coupled diferential equations, x and y are both "independent" variables EXPLAIN BETTER
    return y+h*funk(x,y)#returns the numerical solution's vlaue for y+1

def rK4Mod(x,y,h,funk):#RungeKutta order 4 for coupled equations, x and y are both "independent" variables EXPLAIN BETTER
    k1 = h*funk(x,y)#The first coeficient, taking x and y as "independent" variables
    k2 = h*funk(x+h*k1/2,y+h*k1/2)#The second coeficient, taking x and y as "independent" variables
    k3 = h*funk(x+h*k2/2,y+h*k2/2)#The third coeficient, taking x and y as "independent" variables
    k4 = h*funk(x+h*k3,y+h*k3)#The fourth coeficient, taking x and y as "independent" variables
    return y+(k1+2*k2+2*k3+k4)/6#the calculation of the new y value

n1EulerMod = []#An array to store the n1 values for the Euler method
n2EulerMod = []#An array to store the n2 values for the Euler method
n1RK4Mod = []#An array to store the n1 values for the rk4 method
n2RK4Mod = []#An array to store the n2 values for the rk4 method
n1Sci = []#An array to store the n1 values for Scipy's method
n2Sci = []#An array to store the n2 values for Scipy's method


for i in range(0,hArr.size):#iterates over the number of posible stepsizes
    for j in range(0,tLis[i].size):#iterates over the steps
        if (j == 0):#checks if it's the initial value of n1 and n2
            n1EulerMod.append([n1Zero])#adds the n1 initial value to the array
            n2EulerMod.append([n2Zero])#adds the n2 initial value to the array
            n1RK4Mod.append([n1Zero])#adds the n1 initial value to the array
            n2RK4Mod.append([n2Zero])#adds the n2 initial value to the array
        else:#this is executed if it's not the initial values of n1 and n2
            h = hArr[i]#stores the step size corresponding to the ith 
            n1 = n1EulerMod[i][j-1]#stores the actual value of n1 calculated by the modified Euler method
            n2 = n2EulerMod[i][j-1]#stores the actual value of n2 calculated by the modified Euler method
            n1EulerMod[i].append(eulerMod(n2,n1,h,n1Prime))#Calculates the new value of n1 using the modified Euler method and appends it
            n2EulerMod[i].append(eulerMod(n1,n2,h,n2Prime))#Calculates the new value of n2 using the modified Euler method and appends it
            n1 = n1RK4Mod[i][j-1]#stores the actual value of n1 calculated by the modified RK4 method
            n2 = n2RK4Mod[i][j-1]#stores the actual value of n2 calculated by the modified RK4 method
            n1RK4Mod[i].append(rK4Mod(n2,n1,h,n1Prime))#Calculates the new value of n2 using the modified RK4 method and appends it
            n2RK4Mod[i].append(rK4Mod(n1,n2,h,n2Prime))#Calculates the new value of n2 using the modified RK4 method and appends it

for k in range(0,hArr.size):#iterates over the number of posible stepsizes
    n1Sci.append( sci(n2Prime,n1Prime,n2Zero,n1Zero,hArr[k],nArr[k])[0] )#uses sci to calculate the arrays of n1 and n2 torugh time and takes n1
    n2Sci.append( sci(n2Prime,n1Prime,n2Zero,n1Zero,hArr[k],nArr[k])[1] )#uses sci to calculate the arrays of n1 and n2 torugh time and takes n1


plt.plot(tLis[2],n1Sci[2], label = "odeint")#Graphs 1000 points of the Scipy method for n1
plt.plot(tLis[2],n1EulerMod[2], label = "Euler")#Graphs 1000 points of the modified Euler method for n1
plt.plot(tLis[2],n1RK4Mod[2], label = "RK4")#Graphs 1000 points of the modified rungeKutta4 method for n1
plt.title("n1(t)")#puts the title of the graph
plt.ylabel("n1")#A label for the y-axis
plt.xlabel("t")#A label for the x-axis
plt.legend()#shows the labels
plt.show()#Shows the Graph

plt.plot(tLis[2],n2Sci[2], label = "odeint")#Graphs 1000 points of the Scipy method for n2
plt.plot(tLis[2],n2EulerMod[2], label = "Euler")#Graphs 1000 points of the modified Euler method for n2
plt.plot(tLis[2],n2RK4Mod[2], label = "RK4")#Graphs 1000 points of the modified rungeKutta4 method for n2
plt.title("n2(t)")#puts the title of the graph
plt.ylabel("n2")#A label for the y-axis
plt.xlabel("t")#A label for the x-axis
plt.legend()
plt.show()#Shows the Graph

plt.plot(n1Sci[2],n2Sci[2], label = "odeint")#Graphs 1000 points of the Scipy method for n1 and n2
plt.plot(n1EulerMod[2],n2EulerMod[2], label = "Euler")#Graphs 1000 points of the Euler method for n1 and n2
plt.plot(n1RK4Mod[2],n2RK4Mod[2], label = "RK4")#Graphs 1000 points of the rk4 method for n1 and n2
plt.title("n2(n1)")#puts the title of the graph
plt.ylabel("n2")#A label for the y-axis
plt.xlabel("n1")#A label for the x-axis
plt.legend()#shows the labels
plt.show()#Shows the Graph

'''
Note: At first glance Euler's method and the RK4 method do not differ; but they do at an order of 1e-11 
'''
'''
Note: in the n2(n1) graph we see that n2 decreases almost one by one as n1 increases, this sugests the conservation of matter
'''


n1diffEul = []#a vector to store the difference between the final values of n1 of the Euler method and Scipy's method
n1diffRK4 = []#a vector to store the difference between the final values of n1 of the rk4 method and Scipy's method
n2diffEul = []#a vector to store the difference between the final values of n2 of the Euler method and Scipy's method
n2diffRK4 = []#a vector to store the difference between the final values of n2 of the rk4 method and Scipy's method
for i in range(0,hArr.size):#iterates over the number of posible step sizes
    n1diffEul.append(np.abs(n1EulerMod[i][-1]-n1Sci[i][-1]))#appeds the abs of the difference between final values of n1 by Euler and Scipy
    n1diffRK4.append(np.abs(n1RK4Mod[i][-1]-n1Sci[i][-1]))#appeds the abs of the difference between final values of n1 by rk4 and Scipy
    n2diffEul.append(np.abs(n2EulerMod[i][-1]-n2Sci[i][-1]))#appeds the abs of the difference between final values of n2 by Euler and Scipy
    n2diffRK4.append(np.abs(n2RK4Mod[i][-1]-n2Sci[i][-1]))#appeds the abs of the difference between final values of n2 by rk4 and Scipy

    
plt.semilogx(nArr,n1diffEul, label = "Euler")#graphs the difference between the Euler method and scipy's method as more steps are taken
plt.semilogx(nArr,n1diffRK4, label = "RK4")#graphs the difference between the rk4 method and scipy's method as more steps are taken
plt.title("Absolute differences with respect to Scipy's solution's last value")
plt.ylabel("absolute difference")#A label for the y-axis
plt.xlabel("number of steps")#A label for the x-axis
plt.legend()#shows the labels
plt.show()#shows the graph

'''
Note: The diferences of the Euler and RK4 methods with the odeint method are farther from 0 as n increases, the solutions are considered Divergent
Note: Despite what was just said, it is recommended to study bigger numbers of steps to ensure divergence
'''
