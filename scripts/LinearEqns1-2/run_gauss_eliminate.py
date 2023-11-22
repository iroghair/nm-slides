from gaussjordan import gaussian_eliminate_draft as ge
from gaussjordan import backsubstitution_draft as bs
import numpy as np

A = np.array([[1, 1, 1], [2, 1, 3], [3, 1, 6]]) 
b = np.array([4, 7, 5]) 

Aprime,bprime = ge(A,b)
x = bs(Aprime,bprime)
print(Aprime)
print(bprime)
print(x)