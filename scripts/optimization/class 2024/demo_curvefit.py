from class2024 import generate_random_data
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def model(xdata,a,b,c,d):
    y = a*xdata**3 + b*xdata**2 + c*xdata + d
    return y

def model2(xdata,a0, a1, a2):
    return a0*np.exp(a1*xdata) + a2

x,y = generate_random_data()
a0 = [1,2,3]

a_fit,_ = curve_fit(model2,x,y,p0=a0)
print(a_fit)   

y_model = model2(x,*a_fit)
plt.plot(x,y,'x')
plt.plot(x,y_model,'-')
plt.show()