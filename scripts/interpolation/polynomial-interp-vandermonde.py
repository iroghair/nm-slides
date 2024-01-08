import numpy as np
x = np.array([0, 1, 2])
y = np.array([1.0000, 3.6667, 2.6667])
V = np.vander(x, increasing=True)
print(V)
a = np.linalg.solve(V, y)
print(a)
