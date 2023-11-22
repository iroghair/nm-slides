import time

from functools import cache

@cache
def fib(n):
    if n<1: return 0
    if n==1: return 1
    return fib(n-1) + fib(n-2)

start = time.time()
print(fib(50))
print(time.time()-start)