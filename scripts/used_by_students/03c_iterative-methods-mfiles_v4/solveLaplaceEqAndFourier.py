import numpy as np
from scipy.sparse import diags
import matplotlib.pyplot as plt
from scipy.sparse.linalg import spsolve
from scipy.sparse import lil_matrix

def set_boundary_conditions(A, b, Tb, Nx, Ny):
    A = lil_matrix(A)  # Convert to LIL format for efficient modification
    # Set boundary conditions over x-direction
    for i in range(Nx):
        j = 0
        ind = i + Nx * j
        A[ind, :] = 0  # Reset matrix for boundary cells
        A[ind, ind] = 1  # Add a 1 on the diagonal
        b[ind] = Tb[0]
        
        j = Ny - 1
        ind = i + Nx * j
        A[ind, :] = 0  # Reset matrix for boundary cells
        A[ind, ind] = 1  # Add a 1 on the diagonal
        b[ind] = Tb[1]

    # Set boundary conditions over y-direction
    for j in range(Ny):
        i = 0
        ind = i + Nx * j
        A[ind, :] = 0  # Reset matrix for boundary cells
        A[ind, ind] = 1  # Add a 1 on the diagonal
        b[ind] = Tb[2]
        
        i = Nx - 1
        ind = i + Nx * j
        A[ind, :] = 0  # Reset matrix for boundary cells
        A[ind, ind] = 1  # Add a 1 on the diagonal
        b[ind] = Tb[3]

    A = A.tocsr()  # Convert back to CSR or any other desired format
    return A, b

def solve_laplace_eq(Nx, Ny):
    # Solves the steady-state Laplace equation
    
    Tb = [0, 1, 0, 0]  # Fixed boundary temperatures

    # Fill sparse matrix with [1, 1, -4, 1, 1]
    e = np.ones(Nx*Ny)
    A = diags([e, e, -4*e, e, e], [-Nx, -1, 0, 1, Nx], shape=(Nx*Ny, Nx*Ny))
    b = np.zeros(Nx*Ny)

    A, b = set_boundary_conditions(A, b, Tb, Nx, Ny)

    T = spsolve(A, b)  # Solve matrix
    Tc = T.reshape(Nx, Ny)  # Reshape x-vec to mat Nx, Ny
    xc, yc = np.meshgrid(range(Nx), range(Ny))  # Get position arrays
    return xc, yc, Tc

Nx = 35; Ny = 35;
x, y = np.meshgrid(np.linspace(0,1,Nx), np.linspace(0,1,Ny))
T = np.zeros_like(x) # (*@ \pause @*)
# Fourier series expansion
for n in range(1,100):
    m = 2*n-1
    T += (np.sin(m*np.pi*x) * np.sinh(m*np.pi*y)) / (m * np.sinh(m*np.pi))
Tex = T * (4 / np.pi) # (*@ \pause @*)
# Compute numerical solution and post-process

# First plot is created inside solve_laplace_eq, which also returns Tnum
xc, yc, Tnum = solve_laplace_eq(Nx, Ny) 

fig, axs = plt.subplots(1, 3, figsize=(15, 5), subplot_kw=dict(projection='3d'))
# Plot the numerical 
axs[0].plot_surface(xc, yc, Tnum, cmap = "coolwarm")
axs[0].set_xlabel('x'); axs[0].set_ylabel('y'); axs[0].set_zlabel('T')
axs[0].set_title("the numerical ")
# Plot exact (Fourier)
axs[1].plot_surface(x, y, Tex, cmap='coolwarm')
axs[1].set_xlabel('x'); axs[1].set_ylabel('y'); axs[1].set_zlabel('T')
axs[1].set_title("exact (Fourier)")
# Plot difference
axs[2].plot_surface(x, y, Tex - Tnum, cmap='coolwarm')
axs[2].set_xlabel('x'); axs[2].set_ylabel('y'); axs[2].set_zlabel('T')
axs[2].set_title("difference")
plt.show()