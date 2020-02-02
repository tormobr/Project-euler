import time
import math

def solve():
    primes = sieve(1000000)
    prime_set = set(primes)
    i = 7
    counter = 0
    while True:
        if i not in prime_set:
            for l in range(1, math.floor(math.sqrt(i/2))+1):
                if i - (2*l**2) in prime_set:
                    break

            else:
                return i
        i += 2


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
