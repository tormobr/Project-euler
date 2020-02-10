import math

def solve():
    res = 0
    for i in range(1, 101):
        if not math.sqrt(i).is_integer():
            res += get_digits(i, 99)
    return res


def get_digits(n, digs):
    n = n * (10**(2*digs))
    prev = 0
    nextt = 1 * (10**digs)
    while prev != nextt:
        prev = nextt
        nextt = (prev + (n // prev)) >> 1
    print(len(str(nextt)))
    return sum([int(c) for c in str(nextt)])


print(solve())
