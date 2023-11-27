from scipy.optimize import root_scalar

a = root_scalar(lambda x: -3*x**2 - 5*x + 2, method='brentq', bracket=[0, 3], xtol=1e-15)
print(a)