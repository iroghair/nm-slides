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

def solve_laplace_eq(Nx, Ny, Tb):
    # Fill sparse matrix with [1, 1, -4, 1, 1]
    e = np.ones(Nx*Ny)
    A = diags([e, e, -4*e, e, e], [-Nx, -1, 0, 1, Nx], shape=(Nx*Ny, Nx*Ny))
    b = np.zeros(Nx*Ny)

    A, b = set_boundary_conditions(A, b, Tb, Nx, Ny)

    T = spsolve(A, b)  # Solve matrix
    Tc = T.reshape(Nx, Ny)  # Reshape x-vec to mat Nx, Ny
    xc, yc = np.meshgrid(range(Nx), range(Ny))  # Get position arrays
    return xc, yc, Tc


def main():
    # First plot is created inside solve_laplace_eq, which also returns Tnum
    Nx = 35; Ny = 35
    Tb = [0, 1, 0, 0]  # Fixed boundary temperatures
    xc, yc, Tnum = solve_laplace_eq(Nx, Ny, Tb) 

    fig, ax = plt.subplots(1, 1, figsize=(4, 4), subplot_kw=dict(projection='3d'))
    # Plot the numerical 
    ax.plot_surface(xc, yc, Tnum, cmap = "coolwarm")
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('T')
    ax.set_title("Numerical solution")
    plt.show()

if __name__ == "__main__":
    main()