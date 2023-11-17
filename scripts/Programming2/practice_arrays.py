import numpy as np
import time

def f(x):
    return x**2 + 2*x - 4

x = np.linspace(0,20,10_000_000)

y = []
start = time.time()
for val in x:
    y.append(f(val))

print(f'Execution time is: {time.time() - start}')

start2 = time.time()
y = f(x)
print(f'Execution time NumPy is: {time.time() - start2}')

import matplotlib.pyplot as plt

x = np.linspace(0,10)
y = x**2 - 4*x
plt.plot(x,y)
plt.show()