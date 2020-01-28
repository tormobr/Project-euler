from collections import defaultdict
import time
import math

def solve():
    primes = gen_primes()
    SEEN = set([2,3,5,7])
    #for i in range(4): next(primes)
    n = 5
    res = []
    while True:
        n = next(primes)
        SEEN.add(n)
        if len(res) == 11:
            break
        s = str(n) 
        for i in range(1, len(s)):
            right = s[i:]
            left = s[:-i]
            left = int(left)
            right = int(right)
            if not left in SEEN or not right in SEEN:
                break
        else:
            res.append(n)
        n += 1
    return (res, sum(res))
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

print(solve())
