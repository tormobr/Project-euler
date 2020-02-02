

def solve():
    res = 0
    for i in range(10000):
        current = i
        for k in range(49):
            current = current + int(str(current)[::-1])
            print(current)
            if is_palin(current):
                break
        else:
            res += 1
    return res

def is_palin(n):
    return str(n) == str(n)[::-1]
    


print(solve())
