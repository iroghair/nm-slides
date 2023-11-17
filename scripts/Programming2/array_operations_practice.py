import time
import numpy as np

def f(x):
    return x**2+2*x-4

long_data = np.linspace(0,20,10_000_000)

start = time.time()
y1 = f(long_data)
print(f"The vectorized approach took {time.time()-start} seconds")

y2 = np.zeros_like(long_data)
start = time.time()

for i in range(len(long_data)):
    y2[i] = f(long_data[i])

print(f"The iterated approach took {time.time()-start} seconds")