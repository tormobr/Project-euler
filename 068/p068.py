import time
from itertools import permutations

def solve():
    res = 0
    perms = permutations([1,2,3,4,5])
    for p in perms:
        perms2 = permutations([6,7,8,9, 10])
        for p2 in perms2:
            hax = check(p, p2)
            if hax[0]:
                res = int(hax[2])

    return res

def check(p, p2):
    res = []
    digit = ""
    for i in range(len(p)):
        res.append(p[i]+p[(i+1)%5]+p2[i])
        digit += str(p2[i])+ str(p[(i+1)%5]) + str(p[i])
    return len(set(res)) == 1, res, digit

s = time.time()
print(solve())
print("runtime: ", time.time()-s)
