from sympy import symbols, trigsimp, tan

x = symbols('x')
expr = 2*tan(x)/(1 + tan(x)**2)
simplified_expr = trigsimp(expr)
print(simplified_expr)