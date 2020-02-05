import time
from itertools import permutations

def solve():
    res = 0
    nums = [n for n in range(1,11)]
    perms = permutations(nums, 5)
    for p in perms:
        x = [k for k in range(1,11) if k not in p]
        perms2 = permutations(x)         
        for p2 in perms2:
            hax = check(p, p2)
            if hax[0]:
                
                if len(hax[2]) == 16:
                    print(p, p2, hax[2][::-1])
                    res = int(hax[2][::-1])
                    time.sleep(1)

    return res

def check(p, p2):
    res = []
    digit = ""
    for i in range(len(p)):
        res.append(p[i]+p[(i+1)%5]+p2[i])
        digit += str(p[i]) + str(p[(i+1)%5]) + str(p2[i])
    return len(set(res)) == 1, res, digit


print(solve())
