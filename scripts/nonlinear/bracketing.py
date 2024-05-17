import numpy as np

def bracket(func,iv,gr=0.2,max_it=100):
    if not callable(func):
        print("The function func should be a callable function.")
        return
    if len(iv) != 2 or iv[0]==iv[1]:
        print("The interval iv should be a list or array of size 2 with unique values.")
        return
    
    # Make sure that the interval is ordered and of type float
    iv = np.sort(np.array(iv,dtype=np.float64))
    feval = func(iv)
    it = 0

    while np.prod(feval) > 0:
        # Find interval range
        interval_size = np.diff(iv)[0]
        
        # Determine which value is closer to 0
        if np.abs(feval[0]) < np.abs(feval[1]):
            # Expand interval range
            iv[0] -= gr*interval_size
        else:
            # Expand interval range
            iv[1] += gr*interval_size

        print(iv)
        # Apply new boundaries
        feval = func(iv)
        if (it := it+1) >= max_it:
            print(f"Maximum iterations reached, no bracket found on interval {iv}")
            return False,iv
 
    print(f"Bracketing interval found: {iv}")
    return True,iv

def my_fun(x):
    return x**2 + 4*x +2

def bisection(func, a, b, tol, maxIter):
    if func(a) * func(b) > 0:
        print('Error: f(a) and f(b) must have different signs.')
        return None

    iter = 0
    while (b - a) / 2 > tol:
        iter += 1
        if iter >= maxIter:
            print('Maximum iterations reached')
            return None

        c = (a + b) / 2
        print(f'Iteration {iter}: Current estimate: {c}')

        if func(c) == 0:
            return c

        if np.sign(func(c)) != np.sign(func(a)):
            b = c
        else:
            a = c

    return (a + b) / 2


if __name__ == "__main__":
    print("hello world!")
    is_found,interval = bracket(my_fun,[3,4],0.1)