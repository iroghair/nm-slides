= [ 6, 4, 0]

# Import necessary libraries
import numpy as np
from scipy.optimize import linprog

# Define goal function (f)
f = np.array([-5, -4, -6])

# Define boundary functions (A and b)
A = np.array([[1, -1, 1],
              [3, 2, 4],
              [3, 2, 0]])
b = np.array([20, 42, 30])

# Set lower bounds (lb)
lb = np.zeros(3)

# Use linprog function to solve for optimal solution
res = linprog(f, A_ub=A, b_ub=b, bounds=(lb, None))

# Print results
print(res.x) # optimal solution for x
print(res.fun) # optimal value for f (fval)