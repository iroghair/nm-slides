import numpy as np

def setBoundaryConditions(A, b, Tb, Nx, Ny):
    # Set boundary conditions over x-direction
    for i in range(1, Nx+1):
        j = 1
        ind = i + Nx * (j - 1)
        A[ind - 1] = 0  # Reset matrix for boudary cells
        A[ind - 1, ind - 1] = 1  # Add a 1 on the diagonal
        b[ind - 1] = Tb[0]
        j = Ny
        ind = i + Nx * (j - 1)
        A[ind - 1] = 0  # Reset matrix for boudary cells
        A[ind - 1, ind - 1] = 1  # Add a 1 on the diagonal
        b[ind - 1] = Tb[1]

    # Set boundary conditions over y-direction
    for j in range(1, Ny+1):
        i = 1
        ind = i + Nx * (j - 1)
        A[ind - 1] = 0  # Reset matrix for boudary cells
        A[ind - 1, ind - 1] = 1  # Add a 1 on the diagonal
        b[ind - 1] = Tb[2]
        i = Nx
        ind = i + Nx * (j - 1)
        A[ind - 1] = 0  # Reset matrix for boudary cells
        A[ind - 1, ind - 1] = 1  # Add a 1 on the diagonal
        b[ind - 1] = Tb[3]

    return A, b