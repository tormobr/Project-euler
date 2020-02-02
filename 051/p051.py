import numpy as np
from itertools import combinations
import time
import math

def solve():
    n = 1000000
    primes = sieve(n)
    prime_set = set(primes)
    for p in primes:
        for i in range(1, len(str(p))-1):
            hax = replace(p, i)
            for row in hax:
                row = list(filter(lambda x: len(str(x)) == len(str(p)), row))
                if len(set(row) & prime_set) == 8:
                    return row[0]


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


s = time.time()
print(solve())
print("runtime", time.time()-s)

