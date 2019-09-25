
def brute(n):
    primes = [2]
    check = 3
    num = 1
    while num < n:
        for p in primes:
            if check % p == 0:
                break
        else:
            primes.append(check)
            num += 1
        check += 1
    return primes
    
print(brute(10001)[-1])

# more sexy way using the sieve of erathoererers
def sieve(n):
    bitmap = [1 for i in range(n+1)]
    x = 2
    while x *x <= n:
        if bitmap[x]:
            for i in range(x*2, n+1, x):
                bitmap[i] = 0
        x += 1

    for i in range(2, n):
        if bitmap[i]:
            print(i)

# sieve(100000)
