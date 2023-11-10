import numpy as np

def newton_raphson(f, f_prime, initial_guess, tolerance=1e-7, max_iterations=100):
    x = initial_guess
    iterations = 0
    
    while iterations < max_iterations:
        print("\\coordinate (c%i) at (%.2f,%.2f);"%(iterations, x, f(x)))
        print("\\coordinate (c%ix) at (%.2f,0.0);"%(iterations, x))
        x_new = x - f(x) / f_prime(x)
        
        if abs(x_new - x) < tolerance:
            return x_new, iterations
        
        x = x_new
        iterations += 1
    
    raise Exception("Newton-Raphson method did not converge")

# Example usage with the function f(x) = x^2 - 2 and f'(x) = 2x
def fw(x):
    return np.log(x+2) + x * np.exp(-x - x**2)

def fw_prime(x):
    return 1/(x+2) + np.exp(-x - x**2) + x*(-1 -2*x)*np.exp(-x - x**2)

def fd(x):
    return (x - 5) / 2 + np.sin(x - 3) + 1 + np.exp(-x - 1) * np.exp(-x - 7)

def fd_prime(x):
    return 1/2 + np.cos(x - 3) + 0 + (-np.exp(-x - 1)) * np.exp(-x - 7) + np.exp(-x - 1)*(-np.exp(-x - 7))

initial_guess = 2
tolerance = 1e-7
max_iterations = 5

root, iterations = newton_raphson(fd, fd_prime, initial_guess, tolerance, max_iterations)

print(f"Root found: {root}, iterations: {iterations}")
