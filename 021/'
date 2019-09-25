
def d(n):
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res += i
    return res


result = 0
for i in range(1, 10000):
    if i == d(d(i)) and d(i) != i:
        result += i

print(result)

