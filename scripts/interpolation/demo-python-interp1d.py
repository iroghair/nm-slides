# WARNING: Changes in this file will be reflected in the slides!
from scipy.interpolate import interp1d
import numpy as np

fun = lambda x: x**3/2 - (10*x**2)/3 + 11*x/2 + 1
xdata = np.arange(0,6)
ydata = fun(xdata)

f = interp1d(xdata,ydata)
xint = np.linspace(0,5,31)
yint = f(xint)

import matplotlib.pyplot as plt
xc = np.linspace(0,5,1001,endpoint=True)
yc = fun(xc)
plt.figure(figsize=(5,4))
plt.plot(xdata,ydata,'o',markersize=12,label='Input')
plt.plot(xint,yint,'s',label='Interpolated')

plt.plot(xc,yc,color='#344b7444',label='Function')
plt.legend()
plt.tight_layout()
plt.savefig('figures/demo-python-interp1d.pdf')
plt.show()