import math
import time

def solve():
    mov_length = 1
    n, num, p = 1, 1, 0
    while True:
        for i in range(2):
            n += mov_length
            p += 1 if is_prime(n) else 0

        num += 2
        mov_length += 1
        if p/num <= .1:
            return mov_length

def is_prime(n):
    if n in [1,2]:
        return False
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

print(solve())
