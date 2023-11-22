import numpy as np
# Single precision

# Double precision
A = np.array([[1.2969, 0.8648], [0.2161,0.1441]], dtype=np.float64)
x = np.array([0.8642, 0.1440], dtype=np.float64)
y = np.linalg.solve(A, x)
print(f"y64 = {y}")

# Single precision
A = np.array([[1.2969, 0.8648], [0.2161,0.1441]], dtype=np.float32)
x = np.array([0.8642, 0.1440], dtype=np.float32)
y = np.linalg.solve(A, x)
print(f"y32 = {y}")

if np.linalg.cond(A)>10: 
    raise("Ill conditioned error")