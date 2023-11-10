import numpy as np
from numpy.linalg import inv

np.set_printoptions(precision=3)

def broyden(F, x0, tol=1e-6, max_iter=100):
    x = np.array(x0)
    B = np.eye(x.size)
    print(B)
    for i in range(max_iter):
        Fx = F(x)
        if np.linalg.norm(Fx) < tol:
            print(f"Converged after {i} iterations.")
            return x
        x_new = x - inv(B)@Fx
        delta_x = x_new - x
        delta_Fx = F(x_new) - Fx
        B += np.outer((delta_Fx - B@delta_x)/(delta_x@delta_x), delta_x)
        x = x_new
        print(B)
    print("Max iterations reached.")
    return x

if __name__ == "__main__":
    f = lambda x: np.array([x[0]**2 + x[1]**2 - 4, x[0]**2 - x[1] + 1])
    sol = broyden(f, np.array([1.0,1.0]), 1e-6, 20)