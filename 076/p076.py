import time

def solve(n):
    res = [1 if i == 0 else 0 for i in range(n)];
    for i in range(1, n-1):
        for j in range(i, n):
            res[j] += res[j - i]
    return res[-1]

print(solve(101))
