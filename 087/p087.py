import time
import math
from itertools import product
def solve(n):
    s = [p**2 for p in primes if p**2 < n]
    c = [p**3 for p in primes if p**3 < n]
    t = [p**4 for p in primes if p**4 < n]
    res = set()
    for a, b, c in product(s,c,t):
        if a + b + c < n:
            res.add(a+b+c)
    return len(res)

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

n = 50*10**6
primes = sieve(math.floor(math.sqrt(n)))
prime_set = set(primes)
print(solve(n))
