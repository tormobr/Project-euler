import time

def solve():
    n = 125874
    while True:
        nums = [n*i for i in range(2,7)]
        if contains_same(nums):
            return n
        n += 1
       
def contains_same(l):
    return len(set([tuple(sorted(str(n))) for n in l])) == 1

print(solve())
