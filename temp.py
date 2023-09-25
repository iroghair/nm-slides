import numpy as np
from scipy.integrate import quad
def func(x):
    return np.exp(-x**2)
I, err = quad(func, 0, 10)
print(I)