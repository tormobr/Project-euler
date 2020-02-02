import time
import math

def solve():
    primes = sieve(1000000)
    prime_set = set(primes)
    i = 650
    streak = 0
    while True:
        streak += 1 if factorize(i, primes, prime_set) == 4 else -streak
        if streak == 4:
            return i - 3
        i += 1


def factorize(n, primes, prime_set):
    res = []
    for p in primes:
        while n % p == 0 and n != p:
            n /= p
            res.append(p)
        if n in prime_set:
            res.append(n)
            return len(set(res))

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
