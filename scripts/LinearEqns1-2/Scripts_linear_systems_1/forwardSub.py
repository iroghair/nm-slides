import numpy as np

def forwardSub(A,b):
    
    # Check the matrix - should be square
    N,M = A.shape
    if(N!=M):
        print('Matrix A in forwardSub should be square')
        return
    
    # Assign b to x
    x = b
    
    # Perform forward substitution
    for row in range(N):
        for j in range(row):
            x[row] = x[row] - A[row,j] * x[j]
        x[row] = x[row] / A[row,row]
        
    return x