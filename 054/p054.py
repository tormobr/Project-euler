import time
from collections import defaultdict


letters = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def solve():
    hands = read_file("poker.txt")
    for h1,h2 in hands:
        print(get_hand(h1))
        print(get_hand(h2))
        time.sleep(1)


def read_file(file_name):
    ret = []
    for line in open(file_name):
        line = line.strip()
        if line:
            line = line.split()
            ret.append((line[:5], line[5:]))
    return ret

def get_hand(hand):
    nums = []
    cols = []
    for s in hand:
        n, c = letters[s[0]], s[1]
        nums.append(n)
        cols.append(c)
    for i in range(1,10):
        print(funcs[i](nums, cols))

def royal_flush(nums, cols):
    return sorted(nums) == [10,11,12,13,14] and len(set(cols)) == 1

def straight_flush(nums, cols):
    return flush(nums, cols) and straight(nums, cols)

def four(nums, cols):
    return len(set(nums)) == 2


def full(nums, cols):
    if nums.count(nums[0]) == 2 or nums.count(nums[0]) == 3:
        return len(set(nums)) == 2
    return False

def flush(nums, cols):
    return len(set(cols)) == 1
    pass 

def straight(nums, cols):
    for i in range(len(nums)-1):
        if nums[i+1] != nums[i]+1:
            return False
    return True, sorted(nums)[-1]

def three(nums, cols):
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
    return 3 in count.values()
        

def pairs2(nums, cols):
    count = defaultdict(int)
    res = []
    for n in nums:
        count[n] += 1
    leader = 0
    if 2 not in count.values():
        return False
    for k, v in count.items():
        if v == 2:
            res.append(k)
    if len(res) == 2:
        return True, max(res)
                
    

def pair(nums, cols):
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
    leader = 0
    if 2 not in count.values():
        return False
    for k, v in count.items():
        if v == 2 and k > leader:
            leader = k
    return True, leader

def high(nums, cols, n): 
    nums = sorted(nums)[::-1][n:]
    print(nums)
    return nums[0]

funcs = {
    1: royal_flush,
    2: straight_flush,
    3: four,
    4: full,
    5: flush,
    6: straight,
    7: three,
    8: pairs2,
    9: pair
}

print(solve())
