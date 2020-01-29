def solve():
    res = 0
    for i in range(1,10000):
        pan = ""
        j = 1
        print(i)
        while len(pan) < 9:
            pan += str(i * j)
            j += 1
        if is_pandigital(pan) and int(pan) > res:
            res = int(pan)
    return res

def is_pandigital(n):
    return sorted(str(n)) == [str(i) for i in range(1,10)]

print(solve())
