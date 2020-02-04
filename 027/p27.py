

def solve():
    primes = sieve(10000000)
    prime_set = set(primes)
    res = (0,0,0)
    for a in range(-1000, 1001):
        print(a)
        for b in range(-1000, 1001):
            reps = 0
            while True:
                if abs(f(reps, a, b)) in prime_set:
                    reps += 1
                else:
                    break
            if reps > res[0]:
                res = (reps, a ,b)
    return res



def sieve(n):
    primes = []
    bitmap = [1 for i in range(n+1)]
    x = 2
    while x *x <= n:
        if bitmap[x]:
            for i in range(x*2, n+1, x):
                bitmap[i] = 0
        x += 1

    for i in range(2, n):
        if bitmap[i]:
            primes.append(i)
    return primes


def f(n, a, b):
    return n**2 + a*n + b

print(solve())
