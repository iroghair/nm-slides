import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xdata = np.arange(0,6)
fun = lambda x: x**3/2 -(10*x**2)/3 + 11*x/2 + 1
ydata = fun(xdata)

fint = interp1d(xdata,ydata,kind='cubic')
print(fint(-1.5))
xc = np.linspace(0,5,101)
yc = fint(xc)


plt.plot(xc,yc,'x-')
plt.plot(xdata,ydata,'s')
plt.plot(1.5, fint(1.5), 'r*')
plt.show()