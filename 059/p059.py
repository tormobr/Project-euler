import time
from itertools import permutations
from itertools import cycle

def solve(data):
    combs = permutations([i for i in range(97, 123)], 3)  
    for c in combs:
        res = []
        cyc = cycle(c)
        for x in data:
            k = next(cyc)
            res.append(x ^ k)
            #print(x, k, res[-1])
        if check(res):
            return sum(res)
        #time.sleep(.1)

def check(a):
    count = 0
    ret = ""
    for s in a:
        ret += chr(s)
    print(ret)
    return ret.count(" ") > 200

    
def read_file(filename):
    return [int(x) for x in open(filename).read().split(",")]
    

data = read_file("input.txt")
print(solve(data))
