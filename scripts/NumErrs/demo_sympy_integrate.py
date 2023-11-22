from sympy import simplify, integrate, diff
from sympy.abc import x

f = 1/(x**3+1)
print(f'Original: {f}')
my_f_int = integrate(f, x)
print(f'Integrated: {my_f_int}')
my_f_diff = diff(my_f_int, x)
print(f'Differentiated: {my_f_diff}')
my_f_diff_simplified = simplify(my_f_diff)
print(f'Simplified: {my_f_diff_simplified}')