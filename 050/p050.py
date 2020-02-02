import time
import math

def solve():

    n = 1000000
    primes = sieve(n)
    prime_set = set(primes)
    res = (0,0)
    last = len(primes)

    for i in range(n):
        for j in range(i + res[1], last):
            current = sum(primes[i:j])
            if current > n:
                last = j + 1
                break
            res = (current, j - i) if current in prime_set else res
    return res

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
