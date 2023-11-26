# Python code
import numpy as np
from scipy.optimize import minimize
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# Define variables
Nx = 25
Ny = 35
Tb = [40, 10, 40, 10]  # Fixed boundary temperatures
T0 = 0
T_set = 20
UB = np.inf
LB = -np.inf

def fitcrit_laplace(T, Nx, Ny, Tb, T_set):
    # Objective function to minimize
    T = np.reshape(T, (Nx, Ny))
    Tb = np.reshape(Tb, (2, 2))

    # Create sparse matrix for solving Laplace equation
    diagonals = [np.ones(Nx * Ny) * -4,  # Main diagonal
                 np.ones(Nx * Ny - 1),  # Right diagonal
                 np.ones(Nx * Ny - 1),  # Left diagonal
                 np.ones(Nx * Ny - Nx),  # Upper diagonal
                 np.ones(Nx * Ny - Nx)]  # Lower diagonal
    diagonals[0][Ny - 1::Ny] = 0
    diagonals[1][Ny - 1::Ny] = 0
    diagonals[2][Ny::Ny] = 0
    diagonals[3][:Nx] = 0
    diagonals[4][-Nx:] = 0
    A = sp.sparse.diags(diagonals, [0, 1, -1, Nx, -Nx]).toarray()

    # Insert boundary conditions into matrix and right-hand side
    A[0, :] = 0  # Top row
    A[0, Ny] = 1
    A[-1, :] = 0  # Bottom row
    A[-1, -Ny] = 1
    A[:, 0] = 0  # Left column
    A[Nx * Ny - Ny : Nx * Ny, 0] = 0
    A[:, Ny - 1] = 0  # Right column
    A[Nx * Ny - 1, Ny - 1 : Nx * Ny + Ny - 1 : Ny] = -1

    # Solve linear system
    b = T_set * np.ones(Nx * Ny)
    b[0] = Tb[0, 0]
    b[-1] = Tb[0, 1]
    b[1 : Ny - 1] = 0
    b[-2 * Ny + 1 : -Ny - 1] = 0
    T_model = spsolve(A, b)
    return T_model

# Use scipy's minimize function to solve for T_fit
T_fit = minimize(fitcrit_laplace, T0, args=(Nx, Ny, Tb, T_set), method='Nelder-Mead').x
T_model = fitcrit_laplace(T_fit, Nx, Ny, Tb, T_set)

# Reshape T_model for plotting
T_plot = np.reshape(T_model, (Nx, Ny))

# Create x and y arrays for surface plot
x = np.arange(1, Ny + 1)
y = np.arange(1, Nx + 1)
xx, yy = np.meshgrid(x, y)

# Plot the surface
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, T_plot)
plt.show()

# Calculate and print mean T_model
mean_T = np.mean(T_model)
print('Mean temperature: ' + str(mean_T))