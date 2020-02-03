

def solve():
    fracs = gen_frac(1000)
    res = 0
    for (n, d) in fracs:
        if len(str(n)) > len(str(d)):
            res += 1
    return res
     

def gen_frac(x):
    ret =[(1, 1)]
    for i in range(x):
        n, d = ret[i]
        ret.append((n+(2*d), n+d))
    return ret 
print(solve())
