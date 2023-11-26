import numpy as np
from numpy.linalg import norm

# Define the function
def jacobi(A, b, tol=1e-2):
    
    # Set initial guess
    x = b + 1e-16
        
    # Initialize variables
    x_diff = 1
    N = A.shape[0]
    it_jac = 1
    
    # While not converged or max_it not reached
    while (x_diff > tol and it_jac < 1000):
        x_old = x.copy()
        for i in range(N):
            s = 0
            for j in range(N):
                if j != i:
                    # Sum off-diagonal*x_old
                    s += A[i,j] * x_old[j]
            # Compute new x value
            x[i] = (b[i] - s) / A[i,i]
            
        # Increase number of iterations
        it_jac += 1
        x_diff = norm(A@x - b)/norm(b)
        
    # Print number of iterations
    print(it_jac)
    
    return x, it_jac

def jacobi_vec(A, b, tol=1e-2, itmax=1000):
    
    # Set initial guess
    x = b + 1e-16
        
    # Initialize variables
    x_diff = 1
    N = A.shape[0]
    it_jac = 1
    
    # While not converged or max_it not reached
    while (x_diff > tol and it_jac < itmax):
        x_old = x.copy()
        for i in range(N):
            j = np.r_[np.arange(i),np.arange(i+1,N)]
            # Sum off-diagonal*x_old
            s = A[i,j] @ x_old[j]
            # Compute new x value
            x[i] = (b[i] - s) / A[i,i]
            
        # Increase number of iterations
        it_jac += 1
        x_diff = norm(A@x - b)/norm(b)
        
    # Print number of iterations
    print(it_jac)
    
    return x, it_jac

# Define the function
def gaussseidel(A, b, tol=1e-2): 
    # Set initial guess
    x = b + 1e-16
        
    # Initialize variables
    x_diff = 1
    N = A.shape[0]
    it_gs = 1
    
    # While not converged or max_it not reached
    while (x_diff > tol and it_gs < 1000):
        x_old = x.copy()
        for i in range(N):
            s = 0
            for j in range(N):
                if j < i:
                    # Sum off-diagonal*x_new
                    s += A[i,j] * x[j]
                elif j > i:
                    # Sum off-diagonal*x_old
                    s += A[i,j] * x_old[j]
            # Compute new x value
            x[i] = (b[i] - s) / A[i,i]
            
        # Increase number of iterations
        it_gs += 1
        x_diff = norm(A@x - b)/norm(b)
        
    # Print number of iterations
    print(it_gs)
    
    return x, it_gs

def gaussseidel_vec(A, b, tol=1e-2):
     # Set initial guess
    x = b + 1e-16
        
    # Initialize variables
    x_diff = 1
    N = A.shape[0]
    it_gs = 1
    
    # While not converged or max_it not reached
    while (x_diff > tol and it_gs < 1000):
        x_old = x.copy()
        for i in range(N):
            j = np.arange(i)
            # Sum off-diagonal*x_new
            s = A[i,j] @ x[j]
            j = np.arange(i+1,N)
            # Sum off-diagonal*x_old
            s += A[i,j] @ x_old[j]
            # Compute new x value
            x[i] = (b[i] - s) / A[i,i]
            
        # Increase number of iterations
        it_gs += 1
        x_diff = norm(A@x - b)/norm(b)
        
    # Print number of iterations
    print(it_gs)
    
    return x, it_gs

# Only run the test below if you are not trying to import solve_jacobi
if __name__ == "__main___":
    A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
    b = np.array([15, 10, 10, 10])
    x = np.linalg.solve(A,b)
    x_ = solve_jacobi(A,b, 1e-6)[0]
    print(x, x_)