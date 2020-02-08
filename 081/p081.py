
import time

def solve():
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
h = len(data) -1
w = len(data[0]) -1
print(solve())
