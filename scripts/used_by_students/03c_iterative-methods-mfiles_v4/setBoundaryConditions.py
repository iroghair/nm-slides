import numpy as np

def setBoundaryConditions(A, b, Tb, Nx, Ny):
    # Set boundary conditions over x-direction
    for i in range(1, Nx+1):
        j = 1
        ind = i + Nx * (j-1)
        A[ind-1,:] = 0 # Reset matrix for boundary cells (numpy indexing starts at 0)
        A[ind-1,ind-1] = 1 # Add a 1 on the diagonal
        b[ind-1] = Tb[0]
        j = Ny
        ind = i + Nx * (j-1)
        A[ind-1,:] = 0 # Reset matrix for boundary cells
        A[ind-1,ind-1] = 1 # Add a 1 on the diagonal
        b[ind-1] = Tb[1]
    
    # Set boundary conditions over y-direction
    for j in range(1, Ny+1):
        i = 1
        ind = i + Nx * (j-1)
        A[ind-1,:] = 0 # Reset matrix for boundary cells
        A[ind-1,ind-1] = 1 # Add a 1 on the diagonal
        b[ind-1] = Tb[2]
        i = Nx
        ind = i + Nx * (j-1)
        A[ind-1,:] = 0 # Reset matrix for boundary cells
        A[ind-1,ind-1] = 1 # Add a 1 on the diagonal
        b[ind-1] = Tb[3]
    
    return A, b

if __name__=="__main__":
    Nx = Ny = 20 # number of internal grid cells over x/y-direction
    h = 1/(Nx+1) # grid spacing in both x- and y-direction
    k = 0.1 * h # heat conduction coefficient
    q = 100 # heat flux over x = 1
    
    #Collocation points
    xg = np.array([i*h for i in range(1,Nx+2)]) # 1/h*i with i=1,2,...,Nx+1
    yg = np.array([i*h for i in range(1,Ny+2)]) # 1/h*i with i=1,2,...,Ny+1
    # Dirichlet boundary conditions
    Tb = [300, 1000, 500, 1000]
    
    A = np.zeros((Nx*Ny,Nx*Ny)) # initialize A
    b = np.zeros(Nx*Ny) # initialize b
    
    setBoundaryConditions(A, b, Tb, Nx, Ny)
