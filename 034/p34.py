import math


def solve():
    return sum([i for i in range(3, 40586) if i == fac(i)])

def fac(x):
    return sum([math.factorial(int(x)) for x in str(x)])

print(solve())
