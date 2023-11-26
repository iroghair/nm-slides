import numpy as np
from scipy.optimize import curve_fit

def curve_fit_model(a,xdata):
    y = a[0]*xdata**3 + a[1]*xdata**2 + a[2]*xdata + a[3]
    return y