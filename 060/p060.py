import numpy as np
import math 
import time

# meh not so pretty..
def solve():
    limit = 1150
    for i,p in enumerate(primes):
        for j, p2 in enumerate(primes[i+1:limit]):
            if not test((p,p2)): continue
            for k, p3 in enumerate(primes[j+1:limit]):
                if not (test((p,p3)) and test((p2,p3))): continue
                for z, p4 in enumerate(primes[k+1:limit]):
                    if not (test((p4, p3)) and test((p4,p2)) and test((p4,p))): continue
                    for p5 in primes[z+1:limit]:
                        ps = [p, p2, p3, p4, p5]
                        if test((p5,p)) and test((p5,p2)) and test((p5,p3)) and test((p5,p4)):
                            return sum(ps), ps


def test(perm):
    a = int(str(perm[0]) + str(perm[1]))
    b = int(str(perm[1]) + str(perm[0]))
    return a in prime_set and b in prime_set


def sieve(n):
    primes = []
    #bitmap = [1 for i in range(n+1)]
    bitmap = np.ones((n+1))
    x = 2
    while x *x <= n:
        if bitmap[x]:
            bitmap[x*2:n+1:x] = 0
        x += 1

    for i in range(2, n):
        if bitmap[i]:
            primes.append(i)
    return primes

s = time.time()
primes = sieve(90000000)
prime_set = set(primes)
print(solve())
print("runtime:", time.time()-s)
