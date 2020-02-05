import math

def solve():
    return sum([1 for i in range(1000000) if chain_len(i) == 60])
        
def chain_len(n):
    print(n)
    SEEN = set()
    SEEN.add(n)
    c = 1
    nex = sum([math.factorial(int(d)) for d in str(n)])
    while nex not in SEEN:
        SEEN.add(nex)
        nex = sum([math.factorial(int(d)) for d in str(nex)])
        c += 1 
    return c

print(solve())
