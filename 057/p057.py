

def solve():
    fracs = gen_frac(1000)
    res = 0
    for (n, d) in fracs:
        if len(str(n)) > len(str(d)):
            res += 1
    return res
     

def gen_frac(x):
    ret = []
    n = 1
    d = 1
    for i in range(x):
        print(n, d)
        new_n = n + (2*d)
        new_d = n + d
        n, d = new_n, new_d
        ret.append((n, d))
    return ret 
print(solve())
