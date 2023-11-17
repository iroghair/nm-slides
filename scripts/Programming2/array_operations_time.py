import numpy as np
import time

start = time.time()
x = np.linspace(0,2*np.pi,100_000_000)
y = np.exp(-x) * (2+np.sin(2*np.pi*x))
total_time = time.time() - start

print(f'{total_time = }')