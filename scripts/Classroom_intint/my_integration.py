# my_integration.py
import numpy as np
from scipy.integrate import quad


def left_endpoint(func,a,b,npts=101):
    x = np.linspace(a,b,npts,endpoint=True)
    dx = x[1] - x[0]
    f = func(x)
    int_value = np.sum(f[0:-1]*dx)
    return int_value

def right_endpoint(func,a,b,npts=101):
    x = np.linspace(a,b,npts,endpoint=True)
    dx = x[1] - x[0]
    f = func(x+dx)
    int_value = np.sum(f[0:-1]*dx)
    return int_value

def midpoint(func,a,b,npts=101):
    x = np.linspace(a,b,npts,endpoint=True)
    dx = x[1] - x[0]
    xmid = (x[:-1]+x[1:])/2
    f = func(xmid)
    int_value = np.sum(f*dx)
    return int_value

def trapezoid(func,a,b,npts=101):
    x = np.linspace(a,b,npts,endpoint=True)
    dx = x[1] - x[0]
    f = func(x)
    fmid = (f[1:] + f[:-1])/2
    int_value = np.sum(fmid*dx)
    return int_value


def testint(func,method,a,b,npts=101):
    I_exact = quad(func,a,b)[0]
    I = method(func,a,b,npts)

    print(f'Quad yields: {I_exact:1.3}, {method.__name__} yields: {I:1.3}, difference: {I_exact - I:1.3}')

if __name__ == '__main__':
    f = lambda x: x**2 - 4*x + 6 + np.sin(5*x)
    a, b = 0, 10
    testint(f, left_endpoint, a, b, 1000)
    testint(f, right_endpoint, a, b, 1000)
    testint(f, midpoint, a, b, 1000)
    testint(f, trapezoid, a, b, 1000)