import time

def solve():
    res = 0
    for i in range(1, 40):
        for j in range(1, 10000):
            if len(str(j**i)) == i:
                res += 1
    return res


print(solve())
