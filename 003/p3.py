import math 

def biggest_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n
res = biggest_factor(600851475143)
print(res)
