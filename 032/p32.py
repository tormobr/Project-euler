
def check(a,b):
    digits = [int(c) for c in str(a) + str(b) + str(a*b)]
    if len(digits) != 9: return False
    return set(digits) == set([1,2,3,4,5,6,7,8,9])

def eval(upper):
    res = []
    for i in range(upper):
        upper_j = 9999
        start_j = 1000
        if i > 1000:
            upper_j = 9
            start_j = 1
        if i > 100:
            upper_j = 99
            start_j = 10
        if i > 10:
            upper_j = 999
            start_j = 100
        for j in range(start_j, upper_j):
            if check(i,j):
                print(i,j,i*j)
                res.append(i*j)
    print(sum(set(res)))

upper = 9999
eval(upper)
