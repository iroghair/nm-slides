#Import necessary libraries
import numpy as np   #Library for scientific computing
from scipy.integrate import odeint   #Function for solving Ordinary Differential Equations (ODEs)

#Define function
def simpleode(t, u, k):
    dudt = -k[0]*u + k[1]  #Function to be integrated
    return dudt

#Example usage
t = np.linspace(0, 10, 100)   #Time variable
u0 = 1   #Initial value of u
k = [2, 5]   #Values for k1 and k2
u = odeint(simpleode, u0, t, args=(k,))   #Solve ODE using odeint function
print(u)   #Print u at different time points