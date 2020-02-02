

def solve():
    res = 0
    for i in range(100):
        for j in range(100):
            summ = sum([int(n) for n in str(i**j)])
            if summ > res:
                res = summ
    return res


print(solve())
