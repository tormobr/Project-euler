
def eval(n):
    maxes = [[i, i*i] for i in range(3,n+1,2)]
    total = [x-j*(i-1) for i, x in maxes for j in range(4)]
    total.append(1)
    print(total, sum(total))

eval(1001)

