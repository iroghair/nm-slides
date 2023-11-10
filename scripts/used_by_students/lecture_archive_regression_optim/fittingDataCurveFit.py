# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

# Generate linear space of control points
N = 100                # Number of data points
x = np.linspace(0,1,N) # Points (independent variable)
A = np.array([1, 1/3, 1.5, 3.5]) # Coefficients of polynomial

# Generate 'measurement values' with errors following a normal distribution
# Initialize randomizer
pd = norm(0, 0.5)
# Add scatter data to the polynomial
y = A[3]*x**3 + A[2]*x**2 + A[1]*x + A[0] + pd.rvs(N)

# Plot the generated data
plt.plot(x, y, 'x')
plt.hold(True)

# Initial guess of coefficients
a0 = np.array([1, 2, 1, 3])

# Define the curve fit model function
def curve_fit_model(x, a0):
    return a0[3]*x**3 + a0[2]*x**2 + a0[1]*x + a0[0]

# Perform fitting
a_fit, _ = curve_fit(curve_fit_model, x, y, p0=a0)

# Run the model once more, with fitted coefficients
y_model = curve_fit_model(x, a_fit)

plt.plot(x, y_model, '-r')
plt.show()