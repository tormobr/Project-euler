import time
from itertools import permutations


def solve():
    res = []
    perms = permutations("0123456789")
    divs = [2,3,5,7,11,13,17]
    for i in perms:
        i = "".join(i)
        if test(i, divs):
            print(res)
            res.append(int(i))
    return sum(res)


def test(n, divs):
    for i in range(0, len(divs)):
        if int(n[i+1:i+4]) % divs[i] != 0:
            return False
    return True
    
divs = [2,3,5,7,11,13,17]
time.sleep(10)
print(solve())
