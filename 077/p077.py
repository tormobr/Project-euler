import time
import math

def solve():
    n = 10000
    primes = sieve(n)
    res = [0 for i in range(n)];
    res[0] = 1

    for i in range(len(primes)):
        for j in range(i, n):
            if j - primes[i] >= 0:
                res[j] += res[j - primes[i]]
        if res[i] > 5000:
            return res[i], i

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



print(solve())
