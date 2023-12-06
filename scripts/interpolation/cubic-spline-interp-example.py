import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Generate random data set
xdata = np.arange(0, 26)
ydata = np.random.rand(len(xdata))

# Interpolant on a fine mesh
xc = np.linspace(0, 25, 1001)
ifun = make_interp_spline(xdata, ydata)
yc = ifun(xc)

# Plot the data
plt.plot(xdata, ydata, 'o')
plt.plot(xc, yc, '-r')
plt.show()