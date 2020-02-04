import sys
from itertools import permutations
from collections import defaultdict
import time


def solve():
    nums = gen()
    d = create_dict(nums)
    for k in d.keys():
        search(d.copy(), k, [])

def search(d, k, path):
    path.append(k)
    if len(path) == 6:
        if path[0] in d[k] and len(set([t for t,v in path])) == 6:
            print("result: ",path, sum([v for t,v in path]))
            sys.exit(0)
    else:
        for c in d[k]:
            search(d, c, path.copy())

def match(a, b):
    return a % 100 == b // 100

def gen():
    ret = []
    for i in range(150):
        ret += f(i)
    ret = list(filter(lambda x: 999 < x[1] < 10000, ret))
    return list(map(lambda x: (x[0], int(x[1])), ret))

def create_dict(a):
    d = defaultdict(lambda: [])
    for t, v in a:
        for t1, v1 in a:
            if match(v, v1) and t != t1:
                d[(t,v)].append((t1, v1))
    return d

def f(n):
    return [(3, n*(n+1)/2),
            (4, n**2),
            (5, n*((3*n)-1)/2),
            (6, n*((2*n)-1)),
            (7, n*((5*n)-3)/2),
            (8, n*((3*n)-2))]


print(solve())
