import sys
from itertools import permutations
from collections import defaultdict
import time


def solve():
    nums = gen()
    d = create_dict(nums)
    for k in d.keys():
        rec(d.copy(), k, [])

def rec(d, k, path):
    path.append(k)
    if len(path) == 6:
        if path[0] in d[k] and len(set([t for t,v in path])) == 6:
            print("result: ",path, sum([v for t,v in path]))
            sys.exit(0)
    else:
        for c in d[k]:
            rec(d, c, path.copy())

def match(a, b):
    return a % 100 == b // 100


def gen():
    ret = []
    for i in range(19,144):
        ret += [(3, i*(i+1)/2),
            (4, i**2),
            (5, i*((3*i)-1)/2),
            (6, i*((2*i)-1)),
            (7, i*((5*i)-3)/2),
            (8, i*((3*i)-2))]
    return list(map(lambda x: (x[0], int(x[1])), ret))

def create_dict(a):
    d = defaultdict(lambda: [])
    for t, v in a:
        for t1, v1 in a:
            if match(v, v1) and t != t1:
                d[(t,v)].append((t1, v1))
    return d

print(solve())
