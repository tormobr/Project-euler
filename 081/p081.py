from collections import defaultdict
import time

def solve():
    return dynamic()

def create_dict():
    d = defaultdict(lambda: [])
    for i in range(h):
        for j in range(w):
            d[(i,j)].append((i+1, j))
            d[(i,j)].append((i, j+1))
    return d

def dynamic():
    for i in range(h-1, -1, -1):
        data[h][i] += data[h][i+1]
        data[i][w] += data[i+1][w]

    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            data[i][j] += min(data[i+1][j], data[i][j+1])
    return data[0][0]

def read_file():
    return [list(map(int, line.split(","))) for line in open("input.txt").read().strip().split("\n")]


data = read_file()
dist = defaultdict(int)
h = len(data) -1
w = len(data[0]) -1
print(solve())
