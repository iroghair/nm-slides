# Python

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags

# Set parameters
Nx = 100
Nt = 40000
Dax = 1e-8
cL = 1
cR = 0
tend = 5000
length = 5e-3

# Calculate time and space steps
dt = tend/Nt
dx = length/Nx

# Calculate Fourier number
Fo = Dax*dt/(dx*dx)

# Create array of x values
x = np.linspace(0, length, Nx+1)

# Initialize matrix A
A = diags([-Fo, 1-2*Fo, -Fo], [-1,0,1], shape=(Nx+1, Nx+1))

# Initialize concentration array
c = np.zeros((Nt+1, Nx+1))

# Set boundary conditions
c[:, 0] = cL
c[:, Nx] = cR

# Transpose c for calculation convenience
c = c.T

# Perform time steps
for n in range(1, Nt+1):
    c[1:Nx, n] = A.dot(c[1:Nx, n-1])

# Transpose c back to original orientation
c = c.T

# Define desired output points
out = [12.6, 62.5, 125, 625, 5000]

# Calculate corresponding time steps
outdt = (np.array(out)//dt).astype(int)

# Plot results
plt.plot(x, c[outdt,:])
plt.xlabel('x')
plt.ylabel('Concentration')
plt.show()