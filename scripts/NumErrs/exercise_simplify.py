from sympy import tan, simplify, trigsimp
from sympy.abc import x

expr = 2*tan(x)/(1 + tan(x)**2)
simplified_expr = simplify(expr)
print(simplified_expr)