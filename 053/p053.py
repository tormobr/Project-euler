import math

def solve():
    res = 0
    res = [nCr(i,j) for i in range(1,101) for j in range(1,i+1)]
    return len(list(filter(lambda x: x > 1000000, res)))

def nCr(n, r):
    top = (math.factorial(n))
    bottom = math.factorial(r) * math.factorial(n - r)
    return top / bottom


print(solve())
