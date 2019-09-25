import numpy as np

def is_perfect(n):
    return sum([x for x in range(1, n) if n % x == 0]) > n

def find_abundant(n):

    return [i for i in range(1, n) if is_perfect(i) == 1]

def calculate(n):
    boolean_map = np.zeros((n))
    abundant = find_abundant(n)
    for a in abundant:
        for b in abundant:
            if a + b < n: boolean_map[a+b] = 1
            else: break

    return sum([i for i,n in enumerate(boolean_map) if not n])

print(calculate(28123))
