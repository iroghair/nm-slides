import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate linear space of control points
N = 100 # Number of data points
x = np.linspace(0,1,N) # Points (independent variable)
A = np.array([1, 1/3, 1.5, 3.5]) # Coefficients of polynomial

# Generate 'measurement values' with errors following a normal distribution
# Initialize randomizer
pd = norm(0,0.5)
# Add scatter data to the polynomial
y = A[3]*x**3 + A[2]*x**2 + A[1]*x + A[0] + pd.rvs(N)

# Plot the generated data
plt.plot(x, y, 'x')

# Fit using backslash division
# Generate coefficient matrix
X = np.ones((N, 4))
X[:, 1] = x
X[:, 2] = x**2
X[:, 3] = x**3
# Solve and print coefficients
Amod = np.linalg.lstsq(X, y, rcond=None)[0]

# Plot the fitted data
ymod = Amod[3]*x**3 + Amod[2]*x**2 + Amod[1]*x + Amod[0]
plt.plot(x, ymod, '-r')
plt.show()