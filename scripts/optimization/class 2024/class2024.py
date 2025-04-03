import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_random_data(N=101, p=[1, 1/3, 1.5, 3.5], draw=False):
    x = np.linspace(0,1,N)
    pd = norm(loc=0,scale=0.1)
    y = np.polyval(p, x) + pd.rvs(size=N)

    if draw:
        plt.plot(x,y,'x')
        plt.show()
    return x,y

def fit_using_polyfit(x,y,n=2,draw=False):
    p = np.polyfit(x,y,n)
    if draw:
        plt.plot(x,y,'x')
        plt.plot(x, np.polyval(p,x), '-')
        plt.show()
    return p

def fit_linear_model(x,y,draw=False):
    assert x.shape == y.shape, "x and y must have the same shape"
    n = x.shape[0]
    sx2 = np.sum(x**2)
    sx = np.sum(x)
    sxy = np.sum(x*y)
    sy = np.sum(y)

    A = np.array([[sx2, sx], [sx, n]])
    b = np.array([sxy, sy])

    p,q = np.linalg.solve(A,b)

    if draw:
        plt.plot(x,y,'x')
        plt.plot(x,p*x+q,'-')
        plt.show()
    return p,q

if __name__ == "__main__":
    x,y = generate_random_data(draw=False)
    print(x,y)
    a,b = fit_linear_model(x,y,True)
    print(a,b)
    p = fit_using_polyfit(x,y,2,True)
    print(x)