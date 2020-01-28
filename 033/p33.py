import math

def solve():
    res = []
    for i in range(11,100, 1):
        for j in range(i, 100, 1):
            if i % 10 == 0 or j % 10 == 0 or i == j:
                continue
            if str(i)[0] == str(i)[1]:
                continue
            if str(j)[0] == str(j)[1]:
                continue
            if str(i)[0] in str(j):
                k,l = check_second(i,j)
                if i/j == k/l:
                    res.append((i,j))
            if str(i)[1] in str(j):
                k,l = check_first(i,j)
                if i/j == k/l:
                    res.append((i,j))
    return res


def check_first(i,j):
    str_i = str(i)
    str_j = str(j)

    k = str_i[0]
    l = str_j.replace(str_i[1], "")
    return (int(k), int(l))

def check_second(i,j):
    str_i = str(i)
    str_j = str(j)

    k = str_i[1]
    l = str_j.replace(str_i[0], "")
    return (int(k), int(l))

res = solve()
print(res)
num = 1
den = 1
for i,j in res:
    num *= i
    den *= j
gcd = math.gcd(num, den)
print(den/gcd)
