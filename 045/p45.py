import time

def solve():
    tris = gen_tri() 
    pent = gen_pent(1000000)
    hexx = gen_hex(1000000)
    while True:
        tri = next(tris)
        if tri in pent and tri in hexx:
            return tri
    return tri

def gen_tri():
    n = 286
    while True:
        yield n*(n+1)/2
        n += 1

def gen_hex(n):
    return set([i*(2*i-1) for i in range(n)])

def gen_pent(n):
    return set([i*(3*i-1)/2 for i in range(n)])

print(solve())
