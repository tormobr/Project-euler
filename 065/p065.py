
def solve():
    d, n = 1, 2
    for i in range(2, 101):
        tmp = d;
        c =  2*(i // 3) if i % 3 == 0 else 1
        d = n
        n = c * d + tmp
    return sum([int(x) for x in str(n)])

print(solve())
