import numpy as np
from itertools import combinations
import time
import math

def solve():

    n = 1000000
    primes = sieve(n)
    prime_set = set(primes)
    for p in primes:
        print(p)
        for i in range(1, len(str(p))-1):
            hax = replace(p, i)
            for row in hax:
                count = 0
                for elem in row:
                    if elem in prime_set and len(str(elem)) == len(str(p)): 
                        count += 1
                        if count == 8:
                            return (sorted(row), p)


def replace(p, n):
    ret = []
    combs = set(combinations([i for i in range(len(str(p)))], n))
    for c in combs:
        for i in range(10):
            strp = str(p)
            for k in range(len(c)):
                strp = strp[:c[k]] +str(i) + strp[c[k]+1:]
            ret.append(int(strp))
    return np.array(ret).reshape((len(ret)//10, 10))



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


print(replace(9999, 2))
print(solve())

