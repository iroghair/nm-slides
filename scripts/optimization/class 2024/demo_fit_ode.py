# demo_fit_ode.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
expdata = np.loadtxt('slides/scripts/optimization/tudataset1.txt',skiprows=1)

T = expdata[:,0]
U = expdata[:,1]
# plt.show()

def odefun(t,u,k1,k2):
    return -k1*u + k2

def fitcrit(k,T,U):
    tspan = [min(T), max(T)]
    u0 = U[0]
    sol = solve_ivp(odefun,tspan,[u0],args=(*k,), t_eval=T)
    return sol.y[0] - U

k0 = [1,2]
kfit = least_squares(fitcrit, k0, args=(T,U))
print(kfit)


tspan = [min(T), max(T)]
u0 = U[0]
k1 = 1
k2 = 2
sol = solve_ivp(odefun,tspan,[u0],args=(*kfit.x,))
plt.plot(T,U,'o')
plt.plot(sol.t, sol.y[0])
plt.show()