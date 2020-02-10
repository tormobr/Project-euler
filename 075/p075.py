from collections import defaultdict
import math

def solve(n):
    d = defaultdict(int)
    res = 0 
    trips = gen_trips(n)
    for a,b,c in trips:
        tmp = a+b+c
        tmp0 = tmp
        while tmp < n:
            d[tmp] += 1
            tmp += tmp0
    for k, v in d.items():
        if v == 1:
            res += 1
    return res


def gen_trips(lim):
    res = set()
    for m in range(2, int(math.sqrt(lim))):
        for n in range(1, m):
            if (n + m) % 2 == 1 and math.gcd(n,m) == 1:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                res.add((a,b,c))
    return res

print(solve(1500000))
