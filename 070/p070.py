

def solve():
    res = (100000000,0)
    for i in range(2, 10000000):
        if i % 10000 == 0:
            print(i)
        rel = phi(i)
        if sorted(str(rel)) == sorted(str(i)):
            if i/rel < res[0]:
                res = i/rel, i
                print("some goog new shit", i/rel)
    return res



def phi(n):
    ret = n
    facs = factorize(n)
    if facs:
        for f in facs:
            ret *= 1-(1/f)
    return int(ret)

def factorize(n):
    res = []
    for p in primes:
        while n % p == 0 and n != p:
            n /= p
            res.append(p)
        if n in prime_set:
            res.append(n)
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


primes = sieve(10000000)
prime_set = set(primes)
print(solve())
