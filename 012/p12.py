

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

def facotrize(n, primes):
    tmp = n
    i = 0
    res = 1
    while primes[i]**2 < n:
        expo = 1
        while tmp % primes[i] == 0:
            expo += 1
            tmp /= primes[i]
        i += 1
        res *= expo
    return res



primes = sieve(200000)

i = 0
check = 0
while facotrize(check, primes) < 500:
    i += 1 
    check += i
print("result number: ", check)
print("number of factors: ", facotrize(check, primes))

