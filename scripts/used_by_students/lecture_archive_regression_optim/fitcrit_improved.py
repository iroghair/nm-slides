.dot(err)

k_est, success = leastsq(fitcrit, 1.0, args=(T, U, u0))

if success:
    tsim, usim = odeint(simpleode, U0, T, args=(k_est,))

There is no indentation on line 9, so the code will not run. The code should look like this:

import numpy as np
from scipy.integrate import odeint

def simpleode(u, t, k):
    return k * u

def fitcrit(k, T, U, U0):
    tsim, usim = odeint(simpleode, U0, T, args=(k,))
    err = usim - U
    return err.dot(err)

k_est, success = leastsq(fitcrit, 1.0, args=(T, U, u0))

if success:
    tsim, usim = odeint(simpleode, U0, T, args=(k_est,))