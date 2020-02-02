from itertools import permutations
import time
import math

def solve():
    primes = sieve(1000000)
    prime_set = set(primes)
    
    for i in range(1000, 9999):
        perms = permutations(str(i))
        tmp = []
        for p in perms:
            p = int("".join(p))
            if p >= 1000:
                if p in prime_set and p not in tmp:
                    tmp.append(p) 
                if len(tmp) == 3:
                    tmp = sorted(tmp)
                    if tmp[1] - tmp[0] == tmp[2] - tmp[1]:
                        return "".join(str(n) for n in tmp)
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
