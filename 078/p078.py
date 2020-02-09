import time
import numpy as np

def solve(n):
    
    res = [0 for i in range(n)]
    res[0] = 1
    for i in range(1, n-1):
        if i % 100 == 0:
            print(i)
        for j in range(i, n):
            res[j] += res[j-i]
        res[i] += 1
        if res[i] % 1000000 == 0:
            return i+1, res[i]

    return res



print("result: ", solve(60000))
