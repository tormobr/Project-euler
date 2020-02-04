import time

def solve():
    return sum([1 for i in range(1,30) for j in range(1,10) if len(str(j**i)) == i])

print(solve())
