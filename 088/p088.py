from sympy import divisors, isprime
import sys
sys.setrecursionlimit(10**6)
import math

import time
from collections import defaultdict
from operator import mul
from itertools import combinations_with_replacement as cwr
from itertools import combinations
from itertools import product
from functools import reduce

# this is a comment

def solve(n):
    d = defaultdict(int)
    for i in range(2, n*2):
        print("current i :", i)
        facs = factorize(i)
        for f in facs:
            summ = sum(f)
            ones = i - summ
            if ones < 1 and len(f) == 1:
                continue
            k = ones +len(f)
            if (d[k] == 0 or i < d[k]) and k <= n:
                d[k] = i

    vals = set()
    for k, v in d.items():
        if k <= n:
            vals.add(v)
    return sum(vals), len(d)
    
def factorize(n):
    res = []
    ret = set()
    for p in primes:
        while n % p == 0:
            res.append(p)
            n //= p

    partitions = partition(res)
    for p in partitions:
        current = []
        for elem in p:
            current.append(reduce(mul, elem))
        ret.add(tuple(current))
    return ret


def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        yield [[ first ]] + smaller


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
    

factors = defaultdict(lambda: [])
primes = sieve(100000)
prime_set = set(primes)
#parts = partition([2,2,3])
#for p in parts:
    #print(p)
#print(factorize(12))
#print("ret: ",factorize(4))
print("ret: ",solve(12000))
