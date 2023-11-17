def fibonacci_recursive(N):
    """
    Prints out the Nth Fibonacci number to the screen.
    SYNTAX: fibonacci_recursive(N)
    """
    if N > 2:
        Nminus1 = fibonacci_recursive(N-1)
        Nminus2 = fibonacci_recursive(N-2)
        out = Nminus1 + Nminus2
    elif N == 1 or N == 2:
        out = 1
    else:
        raise ValueError('Input argument was invalid')
    return out

print(fibonacci_recursive(5))