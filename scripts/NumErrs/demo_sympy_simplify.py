from sympy import simplify
from sympy.abc import x

f = (x-1)*(x+1)*(x**2+1) + 1

print(f, ' -> ', simplify(f))