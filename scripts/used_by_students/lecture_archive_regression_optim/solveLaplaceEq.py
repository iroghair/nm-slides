import numpy as np
from scipy import sparse

def solve_laplace_eq(Nx, Ny, Tb, Tint):
    # Solves the Laplace equation for steady-state heat conduction
    
    # Fill sparse matrix with [1 1 -4 1 1]
    e = np.ones(Nx*Ny)
    A = sparse.spdiags([e,e,-4*e,e,e], [-Nx, -1, 0, 1, Nx], Nx*Ny, Nx*Ny)
    
    # Right hand side vector
    b = np.zeros(Nx*Ny)
    
    # Set boundary conditions
    A, b = set_boundary_conditions(A, b, Tb, Nx, Ny)
    
    # Set a central node to Tint
    ind = round(Nx * (Ny/2))
    # Reset matrix for boundary cells
    A[ind,:] = 0
    # Add a 1 on the diagonal
    A[ind, ind] = 1
    b[ind] = Tint
    
    # Solve matrix
    T = A\b
    
    return T

def set_boundary_conditions(A, b, Tb, Nx, Ny):
    # Set boundary conditions
    # Top and bottom boundary conditions
    for i in range(Ny):
        # Top row
        ind = i*Nx + 0
        A[ind, ind] = 1
        b[ind] = Tb
        # Bottom row
        ind = i*Nx + Nx - 1
        A[ind, ind] = 1
        b[ind] = Tb
    
    # Left and right boundary conditions
    for i in range(Nx):
        # Left column
        ind = i + 0
        A[ind, ind] = 1
        b[ind] = Tb
        # Right column
        ind = i + (Ny-1)*Nx
        A[ind, ind] = 1
        b[ind] = Tb
    
    return A, b