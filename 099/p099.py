import math

def solve():
    data = read_file()
    return max([(math.log(b)*e, i+1) for i, (b, e) in enumerate(data)])

def read_file():
    return [list(map(int, line.strip().split(","))) for line in open("input.txt")]

print(solve())


