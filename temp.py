import numpy as np
from scipy.linalg import lu


def forwardSub(L, b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]
    return y


def backwardSub(U, y):
    n = len(y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i+1:n] * x[i+1:n])) / U[i, i]
    return x

import numpy as np
from scipy.linalg import lu

# Example usage
A = np.random.rand(5, 5)  # Get random matrix
P, L, U = lu(A)           # Get L, U and P
b = np.random.rand(5)     # Random b vector
d = P @ b                 # Permute b vector
y = forwardSub(L, d)      # Can also do y=L\d
x = backwardSub(U, y)     # Can also do x=U\y
rnorm = np.linalg.norm(A @ x - b)  # Residual

# Comparing results with numpy solver
x_numpy = np.linalg.solve(A, b)

print("Computed x:")
print(x)
print("\nNumpy's x:")
print(x_numpy)
print("\nResidual:")
print(rnorm)
