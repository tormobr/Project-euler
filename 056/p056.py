

def solve():
    res = 0
    for i in range(100):
        for j in range(100):
            digs = str(i**j)
            summ = sum([int(n) for n in digs])
            if summ > res:
                res = summ
    return res


print(solve())
