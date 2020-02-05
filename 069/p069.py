import time
from operator import mul

def solve():
    res = 1
    for p in primes:
        if res*p > 1000000:
            return res
        res *= p

def sieve(n):
    primes = []
    bitmap = [1 for i in range(n+1)]
    x = 2
    while x *x <= n:
        if bitmap[x]:
            for i in range(x*2, n+1, x):
                bitmap[i] = 0
        x += 1

    for i in range(2, n):
        if bitmap[i]:
            primes.append(i)
    return primes

s = time.time()
primes = sieve(1000000)
prime_set = set(primes)
print(solve())
print("runtime: ", time.time()-s)
