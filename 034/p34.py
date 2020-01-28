import math


def solve():
    return sum([i for i in range(40586) if i == fac(i)])-3

def fac(x):
    return sum([math.factorial(int(x)) for x in str(x)])

print(solve())
