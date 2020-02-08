

def solve():
    return sum([chain(i) for i in range(1, 10000000)])

def chain(n):
    while True:
        if n == 89:
            return True
        elif n == 1:
            return False
        n = sum([int(x)**2 for x in str(n)])


print(solve())
