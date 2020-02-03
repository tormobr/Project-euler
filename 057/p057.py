

def solve():
    fracs = gen_frac(1000)
    return len([(n,d) for (n,d) in fracs if len(str(n)) > len(str(d))])
     

def gen_frac(x):
    ret =[(1, 1)]
    for i in range(x-1):
        n, d = ret[i]
        ret.append((n+(2*d), n+d))
    return ret 
print(solve())
