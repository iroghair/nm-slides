import scipy.io
from scipy.optimize import least_squares
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# load MATLAB dataset
mat = scipy.io.loadmat('tudataset1.mat')
T = mat['T']
U = mat['U']

# define initial value for U0
U0 = 1.00

# define k0, LB, UB, and options
k0 = [2, 3]
LB = [-np.inf, -np.inf]
UB = [np.inf, np.inf]
options = {}

# define fitting function
def fitcrit(k):
    U_pred = odeint(simpleode, U0, T, args=(k,))
    return U_pred.flatten() - U

# optimize k using lsqnonlin
result = least_squares(fitcrit, k0, bounds=(LB, UB), method='lm', options=options)
k_final = result.x

# simulate ode using k_final
def simpleode(U, t, k):
    return k * U

tsim = np.linspace(T[0], T[-1], 100)
usim = odeint(simpleode, U0, tsim, args=(k_final,))

# plot results
plt.plot(tsim, usim, '-', T, U, 'x')
plt.xlabel('Time')
plt.ylabel('U')
plt.legend(['ODE Simulation', 'Observed Data'])
plt.show()