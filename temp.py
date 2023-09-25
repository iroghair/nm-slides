import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# Generate random data set
x = np.arange(0, 26)
y = np.random.rand(len(x))
# Interpolant on a fine mesh
xc = np.linspace(0, 25, 1001)
yc = interp1d(x, y, kind='cubic')(xc)
# Plot the data
plt.plot(x, y, 'o')
plt.plot(xc, yc, '-r')
plt.show()