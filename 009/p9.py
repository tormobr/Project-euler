
for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        res = a*a + b*b
        if res == c*c:
            print(a*b*c)

