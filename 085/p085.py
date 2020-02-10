

def solve(n):
    ret = min([(abs(f(i,j) - n), i, j) for i in range(2000) for j in range(2000)])
    return ret[1]*ret[2], ret

def f(n, m):
    return (((n+1)*n)/2) * (((m+1)*m)/2)

print(solve(2000000))
