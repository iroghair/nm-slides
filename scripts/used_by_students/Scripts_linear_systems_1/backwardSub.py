import numpy as np

def backwardSub(A,b):
    # Performs backward substitution of Ax=b, using upper
    # triangular matrix A and right hand side b.

    # Error checking; matrix should be square
    N,M = A.shape
    if N != M:
        raise Exception('Matrix A in backwardSub should be square')

    # Assign b to x
    x = b

    # Perform backsubstitution
    for row in range(N-1,-1,-1):
        for j in range(row+1,N):
            x[row] = x[row] - A[row,j]*x[j]
        x[row] = x[row] / A[row,row]

    return x