import math

def solve():
    res = 0
    maxx = 0
    for num in range(1000):
        print(num)
        sols = []
        for i in range(1,num):
            for j in range(i, num):
                k = num-(i+j)
                if math.sqrt(i**2 + j**2) == math.sqrt(k**2) and k != 0:
                    if set((i,j,k)) not in sols:
                        sols.append(set((i,j,k)))
        print(num, len(sols), res)
        if len(sols) > maxx:
            print("solutions:", sols, "lenght: ", len(sols))
            maxx = len(sols)
            res = num
    return res

print("result: ", solve())
