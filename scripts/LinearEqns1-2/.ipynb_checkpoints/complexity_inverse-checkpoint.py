import numpy as np
import matplotlib.pyplot as plt
import time

# Generate random matrices of various sizes 's'. 
# Invert the matrices and store the time required 
# for the inversion. Plot the times vs 's'
s = np.array([10, 20, 50, 100, 200, 500, 1000, 2000,5000,6000,10000])
t_inv = []
for n in s:
    print(f'Working on size {n}')
    A = np.random.rand(n, n)
    start_time = time.time()
    Ainv = np.linalg.inv(A)
    t_inv.append(time.time() - start_time)

plt.loglog(s, t_inv, 'x-')
plt.xlabel('N')
plt.ylabel('Time [s]')
plt.show()