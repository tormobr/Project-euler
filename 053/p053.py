import math
from itertools import combinations

def solve():
    res = 0
    for i in range(1, 101):
        for j in range(1, i+1):
            if nCr(i,j) > 1000000:
                res += 1
    return res
            
def nCr(n, r):
    top = (math.factorial(n))
    bottom = math.factorial(r) * math.factorial(n - r)
    return top / bottom


print(nCr(5,3))
print(solve())
