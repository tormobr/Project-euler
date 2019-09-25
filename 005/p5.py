

# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def hax(n):
    factors = []
    res = 1
    for i in range(2, n):
        if(is_prime(i)):
            x = i
            while x*i <= n:
                x *= i
            res *= x

    return res

print(hax(20))
