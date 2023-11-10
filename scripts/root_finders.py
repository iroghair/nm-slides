
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    history = [x0, x1]
    
    for _ in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        history.append(x2)
        
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    return x1, history


def false_position(f, x0, x1, tol=1e-6, max_iter=100):
    if f(x0) * f(x1) > 0:
        raise ValueError("f(x0) and f(x1) must have different signs.")
    
    history = []

    for _ in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        history.append(x2)
        
        if abs(f(x2)) < tol:
            break
        
        if f(x2) * f(x0) < 0:
            x1 = x2
        else:
            x0 = x2

    return x2, history

def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have different signs.")

    history = []

    for _ in range(max_iter):
        c = (a + b) / 2
        history.append(c)
        
        if abs(f(c)) < tol:
            break

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c, history

x0, x1 = 0, 2
tol = 1e-15
f = lambda x: x**2 -4*x + 2

fnames = "secant", "false position", "bisection"
functions = secant_method, false_position, bisection 
for name, func in zip(fnames, functions):
    _, h = func(f, x0, x1, tol)
    print("%s %i"%(name, len(h)))