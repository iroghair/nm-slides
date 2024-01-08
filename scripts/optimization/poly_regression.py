import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_random_data(N=101,p=[1,1/3,1.5,3.5],draw=False):
    # Generate linear space of control points
    # N -  Number of data points
    # p -  Coefficients of polynomial
    x = np.linspace(0, 1, N)  # Points (independent variable)

    # Generate 'measurement values' with errors following a normal distribution
    # Initialize randomizer
    pd = norm(loc=0, scale=0.1)
    # Add scatter data to the polynomial
    y = np.polyval(p,x) + pd.rvs(size=N)

    # Plot the generated data
    if draw:
        plt.plot(x, y, 'x')
        plt.show()      
    return x,y

def fit_using_polyfit(x,y,n=2,draw=False):
    p = np.polyfit(x,y,n)
    if draw:
        plt.plot(x, y, 'x')
        plt.plot(x, np.polyval(p,x), '-')
        plt.title('Fit using polyfit')
        plt.show()     
    return p

def fit_using_lstsqr(x,y,n=2,draw=False):
    xmat = np.vander(x,n+1)
    sol = np.linalg.lstsq(xmat,y,rcond=None)
    A = sol[0]
    yhat = xmat@A
    if draw:
        plt.plot(x,y,'x')
        plt.plot(x,yhat,'-')
        plt.title('Fit using lstsq')
        plt.show()
    return A,yhat

if __name__ == '__main__':
    x,yhat = generate_random_data()
    ahat = fit_using_polyfit(x,yhat,n=3,draw=False)
    print(f'Coefficients using polyfit: {ahat}')
    ahat = fit_using_lstsqr(x,yhat,3,draw=False)
    print(f'Coefficients using lstsq: {ahat}')