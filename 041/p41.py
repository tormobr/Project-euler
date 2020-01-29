import math
from collections import defaultdict

def solve():
    primes = gen_primes()
    maxx = 0
    for i in range(987654321):
        p = next(primes)
        print("testing: ",maxx)
        if is_pan(p):
            maxx = p

def is_pan(n):
    return sorted(str(n)) == [str(i) for i in range(1,len(str(n))+1)]

def gen_primes():
    D = defaultdict(lambda: [])
    q = 2
    while True:
        if q not in D:
            if q > 10:
                yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]
        
        q += 1


print("results: ", solve())
