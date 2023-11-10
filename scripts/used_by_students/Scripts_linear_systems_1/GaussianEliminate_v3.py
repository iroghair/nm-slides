# Import necessary libraries
import numpy as np

# Define GaussianEliminate function
def GaussianEliminate_v3(A,b):
    
    # Find length of b (N)
    N = len(b)
    
    # Loop through each column
    for column in range(N-1):
        
        # Find maximum element below pivot row in this column
        # Using numpy.argmax() to find index of max element
        index = np.argmax(abs(A[column:,column]))
        
        # Get actual column in A by adding column index to argmax index
        index = index + column
        
        # Store current row in temp using numpy.copy()
        temp = np.copy(A[column,:])
        
        # Swap values in A using numpy.copy()
        A[column,:] = np.copy(A[index,:])
        
        # Swap values in b using numpy.copy()
        b[column] = np.copy(b[index])
        
        # Loop through each row below the pivot
        for row in range(column+1,N):
            
            # Calculate d (row's value divided by pivot value)
            d = A[row,column] / A[column,column]
            
            # Subtract d times pivot row from current row for all elements
            A[row,:] = A[row,:] - (d * A[column,:])
            
            # Subtract d times pivot b value from current b value
            b[row] = b[row] - (d * b[column])
    
    # Perform backward substitution
    x = backwardSub(A,b)
    
    # Return solution vector
    return x

# Define SWAP function
def SWAP(x, r1, r2):
    
    # Store current row in temp
    temp = np.copy(x[r1])
    
    # Swap pivot row and desired row using numpy.copy()
    x[r1] = np.copy(x[r2])
    x[r2] = temp
    
    # Return swapped vector
    return x

# Define backwardSub function
def backwardSub(A,b):
    
    # Find length of b (N)
    N = len(b)
    
    # Initialize solution vector with zeros using numpy.zeros()
    x = np.zeros(N)
    
    # Loop through rows starting from last row
    for row in reversed(range(N)):
        
        # Initialize sum variable as 0 
        sum = 0
        
        # Loop through columns from current row to last column
        for column in range(row,N):
            
            # Add product of A values and corresponding x values to sum
            sum = sum + (A[row,column] * x[column])
        
        # Subtract sum from b value and divide by corresponding A value
        x[row] = (b[row] - sum) / A[row,row]
    
    # Return solution vector
    return x