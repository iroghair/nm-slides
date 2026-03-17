from poly_regression import generate_random_data
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

# Define the model function
def curve_fit_model_1(xdata, a0, a1, a2, a3):
    return a0*xdata**3 + a1*xdata**2 + a2*xdata + a3

def curve_fit_model_2(xdata, a0, a1, a2):
    return a0*np.exp(a1*xdata) + a2

if __name__ == '__main__':
    x,y = generate_random_data()
    plt.plot(x,y,'x')
    # Initial guess of coefficients
    a0 = [1, 2, 1, 3]
    
    # Perform fitting, store resulting coeffs in a_fit
    a_fit, _ = curve_fit(curve_fit_model_1, x, y, p0=a0)
    
    # Run the model once more, with fitted coefficients
    y_model = curve_fit_model_1(x, *a_fit)
    plt.plot(x, y_model, '-',label='Polynomial model')

    # Initial guess of coefficients
    a0 = [1,1,1]
    
    # Perform fitting, store resulting coeffs in a_fit
    a_fit, _ = curve_fit(curve_fit_model_2, x, y, p0=a0)
    
    # Run the model once more, with fitted coefficients
    y_model = curve_fit_model_2(x, *a_fit)
    plt.plot(x, y_model, '-',label='Exponential model')
    plt.legend()
    plt.show()