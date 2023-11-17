def my_function(*args):
    print(args)

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

def mystery(a,b):
    assert b >= 1 and isinstance(b,int), "You should give an integer value for b >= 1"
    if b == 1:
        return a
    else:
        return a + mystery(a,b-1)
    
from math import exp
f = lambda x: x**2 + exp(x) 

from math import inf 

print(inf- inf)