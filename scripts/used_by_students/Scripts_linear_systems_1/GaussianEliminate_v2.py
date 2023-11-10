import numpy as np
def GaussianEliminate_v2(A,b):
    # Perform elimination to obtain an upper triangular matrix
    N = len(b)
    for column in range(0,N-1):
        # Select pivot
        # Find maximum element below pivot row in this column
        index = np.argmax(np.abs(A[column:,column]))
        index = index+column # Get actual column in A (max gets only below pivot)
        # Store current row in temp
        temp = A[column,:]
        # Swap pivot row and desired row
        A[column,:] = A[index,:]
        A[index,:] = temp
        # Swap values in b
        temp = b[column]
        b[column] = b[index]
        b[index] = temp
        for row in range(column+1,N):
            d = A[row,column]/A[column,column]
            A[row,:] = A[row,:] - d*A[column,:]
            b[row] = b[row] -d*b[column]
        # Perform backsubstitution
    for row in range(N-1,-1,-1):
        x[row] = b[row]
        for i in range(row+1,N):
            x[row] = x[row] - A[row,i]*x[i]
        x[row] = x[row]/A[row,row]
    # Transpose the solution to vertical
    x = x.T
    return x