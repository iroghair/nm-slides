import numpy as np
from scipy.integrate import odeint

def simpleode(u, t, k):
    return k * u

def fitcrit(k, T, U, U0):
    tsim, usim = odeint(simpleode, U0, T, args=(k,))
    err = usim - U
    return err