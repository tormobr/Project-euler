

def func_even(n):
    return n/2

def func_odd(n):
    return (3*n) + 1


def collatz(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = func_even(n)
        else:
            n = func_odd(n)
        iterations += 1
    return iterations

best = (0, 0)
for i in range(1, 1000000):
    test = (i, collatz(i))
    if test[1] > best[1]:
        best = test

print(best)


