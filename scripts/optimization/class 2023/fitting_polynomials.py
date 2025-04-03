# fitting-polynomials.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_measurement_data(N=101,p=[1,1/3,1.5,3.5],draw=False):
    x = np.linspace(0, 1, N)
    
    pd = norm(loc=0,scale=0.1)
    y = np.polyval(p,x) + pd.rvs(size=N)

    if draw:    
        plt.plot(x,y,'x')
        plt.show()
    return x,y

def fit_using_polyfit(x,y,draw=False):
    p = np.polyfit(x,y,3)
    if draw:
        plt.plot(x,y,'x')
        plt.plot(x,np.polyval(p,x))
        plt.show()
    return p

def fit_using_lstsq(x,y,N=2,draw=False):
    xmat = np.vander(x,N+1)
    # print(xmat)
    p = np.linalg.lstsq(xmat,y,rcond=False)[0]
    if draw:
        plt.plot(x,y,'x')
        plt.plot(x,np.polyval(p,x))
        plt.show()
    return p 
   
if __name__ == '__main__':
    x,y = generate_measurement_data()
    p = fit_using_polyfit(x,y,draw=True)
    print(f'Coefficients using polyfit: {p}')
    fit_using_lstsq(x,y,N=3)