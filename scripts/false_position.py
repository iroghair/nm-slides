
import numpy as np

def false_position_method(func, x1, x2, tol=1e-6, max_iter=1000):
    if func(x1) * func(x2) > 0:
        print("No root found in the given interval")
        return
    
    print(f"Iteration {0}: y = {round(func(x1),2)}, x = {round(x1,2)}")
    print(f"Iteration {1}: y = {round(func(x2),2)}, x = {round(x2,2)}")
    for i in range(max_iter):
        x_mid = x1 - (func(x1) * (x2 - x1)) / (func(x2) - func(x1))
        print(f"Iteration {i+2}: y = {round(func(x_mid),2)}, x = {round(x_mid,2)}")

        if abs(func(x_mid)) < tol:
            print(f"Root found: x = {x_mid}")
            return
        elif func(x_mid) * func(x1) < 0:
            x2 = x_mid
        else:
            x1 = x_mid
    print(f"Root not found after {max_iter} iterations")

if __name__ == "__main__":
    f = lambda x: np.sin(x*2-0.5)*.6+2/5*x
    false_position_method(f, -1.5, 4, 1e-2, 10)
