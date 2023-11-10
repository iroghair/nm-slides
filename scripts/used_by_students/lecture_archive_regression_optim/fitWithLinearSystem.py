# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_excel('myDataSet.xls')

# Store data from columns 1 and 2 into variables x and y
x = data.iloc[:,0]
y = data.iloc[:,1]

# Get length of x and create a vector of ones with length N
N = len(x)
ones = np.ones(N)

# Create matrix X with columns of ones, x, x^2, and x^3
X = np.vstack((ones, x, x**2, x**3)).T

# Solve for A using matrix division
A = np.linalg.lstsq(X, y, rcond=None)[0]

# Create vector yfit using values of A and x
yfit = A[3]*x**3 + A[2]*x**2 + A[1]*x + A[0]

# Plot the data and fitted curve in a subplot
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8,6))
ax1.plot(x, y, 'x')
ax1.plot(x, yfit, '-r')
ax1.set_xlabel('Controlled variable')
ax1.set_ylabel('Measured variable')

# Calculate absolute error and plot on second subplot
abs_error = y - yfit
ax2.stem(x, abs_error)
ax2.set_xlabel('Controlled variable')
ax2.set_ylabel('Absolute error')
mean_res = np.mean(abs_error)
ax2.set_title('Mean residual: ' + str(mean_res))

plt.tight_layout()
plt.show()