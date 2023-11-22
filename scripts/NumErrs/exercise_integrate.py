from sympy import exp, sinh, integrate, symbols, simplify

x = symbols('x', positive=True)
f = ((exp(x)- exp(-x))/sinh(x))
print(f)
p = integrate(f.simplify(), (x, 0, 10))
print(p)

