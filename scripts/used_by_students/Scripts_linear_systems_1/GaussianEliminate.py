import numpy as np

def GaussianEliminate(A, b):
    # Convert A and b to numpy arrays for easier manipulation
    A = np.array(A)
    b = np.array(b)
    
    # Perform elimination to obtain an upper triangular matrix
    N = len(b)
    for column in range(N-1):
        # Select pivot
        for row in range(column+1, N):
            # Loop over subsequent rows (below pivot)
            d = A[row, column]/A[column, column]
            A[row, :] = A[row, :] - d*A[column, :]
            b[row] = b[row] - d*b[column]
    
    # Perform backsubstitution
    x = np.zeros(N)
    for row in range(N-1, -1, -1):
        x[row] = b[row]
        for i in range(row+1, N):
            x[row] = x[row] - A[row, i]*x[i]
        x[row] = x[row]/A[row, row]
    
    # Transpose the solution to vertical
    x = x.reshape(N, 1)
    return x