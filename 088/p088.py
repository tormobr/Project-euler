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
    for i in range(2, n*2):
        print("current i :", i)
        facs = [(i,)]
        get_factors_rec(i, i, [], facs)
        for f in facs:
            add_k_val(f, i, n)

    return sum(set([v for k,v in d.items()]))

def add_k_val(f, prod, n):
    ones = prod - sum(f)
    k = ones + len(f)
    if ones < 1 and len(f) == 1 or k > n:
        return
    if (d[k] == 0 or prod < d[k]):
        d[k] = prod

def get_factors_rec(number, parent_value, parent_factors, all_factors):
    new_value = parent_value
    for i in reversed(range(2, number)):
        if number % i == 0:
            if new_value > i:
                new_value = i
                
            if number // i <= parent_value and i <= parent_value and number // i <= i:
                all_factors.append((*parent_factors, i, number // i))
                new_value = number // i
                
            if i <= parent_value:
                get_factors_rec(number // i, new_value, parent_factors[:] + [i], all_factors)

d = defaultdict(int)
factors = defaultdict(lambda: [])
print("ret: ",solve(12000))
