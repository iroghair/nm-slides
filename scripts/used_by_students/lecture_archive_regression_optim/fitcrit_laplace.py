import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve

def fitcrit_laplace(actuate_T, Nx, Ny, boundary_T, setpoint_T):
    # Compute model:
    T = solveLaplaceEq(Nx, Ny, boundary_T, actuate_T)

    # Compute error (deviation of mean T with desired setpoint T)
    err = np.mean(T) - setpoint_T

    return err

def solveLaplaceEq(Nx, Ny, boundary_T, actuate_T):
    # Create empty matrix for T values
    T = np.zeros((Nx,Ny))

    # Apply boundary conditions
    T[:,0] = boundary_T[0] # left boundary
    T[:,-1] = boundary_T[1] # right boundary
    T[0,:] = boundary_T[2] # top boundary
    T[-1,:] = boundary_T[3] # bottom boundary

    # Create sparse matrix for coefficients
    A = spdiags([-1,-1,4,-1,-1],[-Nx,-1,0,1,Nx],Nx*Ny,Nx*Ny)

    # Solve for T
    T = spsolve(A,T.flatten()).reshape(Nx,Ny)

    # Add actuate_T values
    T[1:-1,1:-1] += actuate_T

    return T