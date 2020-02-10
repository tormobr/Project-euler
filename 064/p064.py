import math

def solve():
    return sum(1 for i in range(10000) if get_period(i) % 2 != 0)

def get_period(n):
    if math.sqrt(n).is_integer():
        return 0
    m = 0
    d = 1
    a0 = int(math.sqrt(n))
    a = a0
    res = 0
    while a != 2 * a0:
        m = d * a - m
        d = (n - m**2) / d
        a = int((a0 + m) / d)
        print("a:", a,"  m:", m,"  d:", d)
        res += 1
    return res
print(solve())
