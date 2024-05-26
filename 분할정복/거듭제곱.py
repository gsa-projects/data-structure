import time
from contextlib import contextmanager

@contextmanager
def timeit():
    start = time.time()
    yield
    end = time.time()
    print(f'{end - start}s')

def slow_power(x, n):
    ret = 1
    for _ in range(n):
        ret *= x
    return ret

def fast_power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return fast_power(x*x, n // 2)
    else:
        return x * fast_power(x*x, (n - 1) // 2)
    
with timeit():
    slow_power(2, 100000)

with timeit():
    fast_power(2, 100000)