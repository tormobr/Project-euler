import time

def gen_pents(num):
    return [n*(3*n-1)/2 for n in range(1, num)]
        


def solve(n):
    pents = gen_pents(n+1)
    pent_set = set(pents)
    i = 0
    while True:
        for j in range(i):
            D = pents[i] - pents[j]
            P = pents[i] + pents[j]
            if D in pent_set and P in pent_set:
                return D
        i += 1
    return res
print(solve(3000))
