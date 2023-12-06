import numpy as np

def MyFnc1(x):
    return (3*x**2 + 3*x + 4)**(1/3)

def MyFnc2(x):
    return (x**3 - 3*x**2 - 4) / 3

def DirectIterationMethod(g, x, eps):
    itmax = 100
    it = 0
    y = g(x)
    print(f"i: {0}, x: {x:.6e}")
    while (abs(y - x) > eps) and (it < itmax):
        it += 1
        x = y
        y = g(x)
        print(f"i: {it}, x: {x:.6e}")

if __name__ == "__main__":
    DirectIterationMethod(MyFnc1, 2.5, 1e-3)
    DirectIterationMethod(MyFnc2, 2.5, 1e-3)