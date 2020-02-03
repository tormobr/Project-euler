import sys
import time
from itertools import permutations
from itertools import cycle

def solve(data):
    combs = permutations([i for i in range(ord("a"), ord("z"))], 3)  
    for c in combs:
        current = [data[i] ^ c[i%3] for i in range(len(data))]
        if check(current):
            return sum(current)

def check(a):
    filt = list(filter(lambda s: s in range(64,123) or s == 32, a))
    return len(filt) > len(a) * 0.9
            

    
def read_file(filename):
    return [int(x) for x in open(filename).read().split(",")]
    

data = read_file("input.txt")
print(solve(data))
