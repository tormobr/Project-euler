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
