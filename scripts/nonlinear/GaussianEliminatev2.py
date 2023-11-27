import numpy as np
np.set_printoptions(3)

def SWAP(A, c, index):
    A[[c, index]] = A[[index, c]]
    return A

def gaussian_eliminate(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    N = len(b)

    for c in range(N-1):  
        index = np.argmax(np.abs(A[c:N, c])) + c
        A[[c, index]] = A[[index, c]]
        b[[c, index]] = b[[index, c]]
        d = A[c+1:N, c] / A[c, c]
        for i in range(c+1, N):
            A[i, :] -= d[i-c-1] * A[c, :]
            b[i] -= d[i-c-1] * b[c]

    return back_substitution(A, b)

def back_substitution(A, b):
    x = np.copy(b)
    N = len(b)

    for row in range(N-1, -1, -1):
        x[row] -= np.sum(A[row, row+1:] * x[row+1:])
        x[row] /= A[row, row]

    return x

# Test the function
A = [[2, -3, 4], [6, -8, 2], [4, -11, 12]]
b = [3, 5, 7]
x = gaussian_eliminate(A, b)
print(x)
