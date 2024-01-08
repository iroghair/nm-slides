import numpy as np
from scipy.integrate import trapezoid, quad
import matplotlib.pyplot as plt

def rieman_left(func,a,b,npts=101):
    rsum = 0
    x = np.linspace(a,b,npts)
    y = func(x)
    for i,f in enumerate(y[:-1]):
        dx = x[i+1]-x[i]
        assert dx > 0, "x values should be monotonically increasing"
        rsum += f*dx
    return rsum

def rieman_right(func,a,b,npts=101):
    rsum = 0
    x = np.linspace(a,b,npts)
    y = func(x)
    for i,f in enumerate(y[1:]):
        dx = x[i+1]-x[i]
        assert dx > 0, "x values should be monotonically increasing"
        rsum += f*dx
    return rsum

def midpoint(func,a,b,npts=101):
    rsum = 0
    x = np.linspace(a,b,npts)
    x = np.array([(x[i]+x[i+1])/2 for i,_ in enumerate(x[:-1])])
    y = func(x)
    for i,f in enumerate(y[1:]):
        dx = x[i+1]-x[i]
        assert dx > 0, "x values should be monotonically increasing"
        rsum += f*dx
    return rsum
    
def trapezoidnm(func,a,b,npts=101):
    rsum = 0
    x = np.linspace(a,b,npts)
    y = func(x)
    for i,(f1,f2) in enumerate(zip(y[:-1],y[1:])):
        dx = x[i+1]-x[i]
        assert dx > 0, "x values should be monotonically increasing"
        rsum += (f1+f2)/2*dx
    return rsum

def simpson(func,a,b,npts=101):
    if npts%2 == 0:
        npts+=1
    x = np.linspace(a,b,npts)
    y = func(x)
    dx = x[1]-x[0]
    rsum = y[0] + y[-1]
    rsum += 4*sum(y[1:-1:2]) + 2*sum(y[2:-2:2])
    return rsum * dx/3

def test(fun,method,a,b,np=101):
     sol1 = quad(fun,a,b)[0]
     sol2 = method(fun,a,b,np)

     print(f'Quad yields: {sol1:1.3f}, {method.__name__} yields: {sol2:1.3f}, difference: {sol1-sol2:1.5e}')

def convergence_test():
    npts = [5,10,20,40,80,120,240,500,750,1000,2000,4000]
    methods = [rieman_right,rieman_left,midpoint,trapezoidnm,simpson]

    fun = lambda x: x**2 - 4*x + 6 + np.sin(5*x)
    real = quad(fun,0,10)[0]

    int_values_per_method = []
    for method in methods:
        int_values_per_method.append(np.array([method(fun,0,10,n) for n in npts]))
    
    for method,values in zip(methods,int_values_per_method):
        plt.loglog(npts,np.abs(values-real),label=f'{method.__name__}')

    plt.legend()
    plt.show()

if __name__ == '__main__':
        f1 = lambda x: x**2 -4*x +2
        a,b = 0,10
        test(f1,rieman_left,a,b)
        test(f1,rieman_right,a,b)
        test(f1,midpoint,a,b)
        test(f1,trapezoidnm,a,b)
        test(f1,simpson,a,b)

        convergence_test()