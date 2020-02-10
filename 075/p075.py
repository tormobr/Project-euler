from collections import defaultdict
import math
from itertools import product

def solve(n):
    d = gen_trips(n)
    return sum(1 for v in d.values() if v == 1)

def gen_trips(lim):
    d = defaultdict(int)
    for m in range(int(math.sqrt(lim))):
        for n in range(1, m):
            if (n + m) % 2 != 1 or math.gcd(n,m) != 1:
                continue
            x = tmp = (m**2 - n**2) + (2*m*n) +(m**2 + n**2)
            while x < lim:
                d[x] += 1
                x += tmp
    return d

print(solve(1500000))
