# curve_fitting_ode.py
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def simpleode(t, u, k1, k2):
    dudt = -k1*u + k2
    return dudt

def fitcrit(k,expdata):
    t = expdata[0]
    u = expdata[1]
    u0 = [u[0]]
    tspan = [0,max(t)]
    k1,k2 = k
    sol = sp.integrate.solve_ivp(simpleode, tspan, u0, args=(k1, k2), t_eval=t)
    return sol.y[0] - u

# Load your data here (adjust as necessary)
T, U = np.loadtxt('./slides/scripts/optimization/tudataset1.txt',unpack=True, skiprows=1)

# Initial guesses for model parameters
k0 = [1.0, 1.0]

# Perform the curve fitting
expdata = [T,U]
fit = sp.optimize.least_squares(fitcrit, k0, args=(expdata,))
params = fit.x
params_covariance = fit.jac
print('Fitted coefficients:', params)

plt.plot(T,U,'x')
odesol = sp.integrate.solve_ivp(simpleode,[0,max(T)],[U[0]],args=(params))
plt.plot(odesol.t,odesol.y[0])
plt.xlabel('Time [s]')
plt.ylabel('U [-]')
plt.show()

# Postprocessing
alpha = 0.05 # 95% confidence interval = 100*(1-alpha)
n = len(U) # number of data points
p = len(params) # number of parameters
dof = max(0, n - p) # number of degrees of freedom
# t value for the dof and confidence level
tval = stats.t.ppf(1.0-alpha/2., dof)
sigma = np.sqrt(np.diag(params_covariance))
ci = sigma * tval
print('Confidence intervals:')
print('k1:', params[0] - ci[0], params[0] + ci[0])
print('k2:', params[1] - ci[1], params[1] + ci[1])