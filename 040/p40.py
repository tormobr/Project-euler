

def solve():
    d = "0"
    i = 1
    while len(d) <= 1000000:
        d += str(i)
        i += 1
    i = 1

    res = 1
    while i <= 1000000:
        res *= int(d[i])
        i *= 10
    return res

print(solve())
