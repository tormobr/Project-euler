from itertools import permutations
from collections import defaultdict
import time


def solve():
    nums = gen(1000, 9999)
    d = create_dict(nums)
    for k in d.keys():
        rec(d.copy(), k, [])


def rec(d, k, path):
    print(k)
    childs = d[k]
    path.append(k)
    if len(path) == 6:
        print("possibly:", path)
        if match(k[1], path[0][1]):
            if len(set([t for t,v in path])) == 6:
                print(str(k)[2:], str(path[0])[:2])
                print("found the shit!!!!", path, sum([v for t,v in path]))
                time.sleep(10)
    elif len(path) > 6:
        return
    for c in childs:
        rec(d, c, path.copy())
    

def match(a, b):
    return a % 100 == b // 100

def gen(s, e):
    i = 1
    ret = []
    for i in range(19,141):
        ret += [(3, int(i*(i+1)/2)),
        (4, int(i**2)),
        (5, int(i*((3*i)-1)/2)),
        (6, int(i*((2*i)-1))),
        (7, int(i*((5*i)-3)/2)),
        (8, int(i*((3*i)-2)))]
        i += 1
    return list(filter(lambda x: len(str(x[1])) == 4, ret))

def create_dict(a):
    d = defaultdict(lambda: [])
    for t, v in a:
        for t1, v1 in a:
            if str(v)[2:] == str(v1)[:2] and t != t1:
                d[(t,v)].append((t1, v1))
    return d

print(solve())
