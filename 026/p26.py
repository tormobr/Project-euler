import time

def get_cycle(x):
    remainders = []
    new = 1 % x
    while new not in remainders:
        remainders.append(new)
        new = (new*10) % x
    return (x, len(remainders))

def solve(d):
    return max([get_cycle(i) for i in range(2,d)], key=lambda x: x[1])

d = 1000
print("results: ", solve(d))
