import math

def solve():
    res = 0
    for i in range(3, 1000000, 2):
        if not is_prime(i):
            continue
        s = str(i)
        for k in range(len(s)-1):
            s = s[1:] + s[0]
            if not is_prime(int(s)):
                break
        else:
            res += 1


    return res+1

def is_prime(x):
    for i in range(math.floor(math.sqrt(x))+1, 1, -1):
        if x % i == 0:
            return False
    return True


print(solve())
