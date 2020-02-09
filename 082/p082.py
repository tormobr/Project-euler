from copy import deepcopy
from collections import defaultdict
import time

def solve():
    return dynamic()

def dynamic():
    for j in range(w-1, -1, -1):
        for i in range(h+1):
            res[i][j] = calculate_col(i, j)
    return min([res[i][0] for i in range(h+1)])

def calculate_col(i, j):
    winner = data[i][j] + res[i][j+1]
    current = data[i][j]
    for i2 in range(i-1, -1, -1):
        current += data[i2][j]
        if current + res[i2][j+1] < winner:
            winner = current + res[i2][j+1]
        elif current > winner:
            break

    current = data[i][j]
    for i2 in range(i+1, h+1):
        current += data[i2][j]
        if current + res[i2][j+1] < winner:
            winner = current + res[i2][j+1]
        elif current > winner:
            break
    return winner
         
def read_file():
    return [list(map(int, line.split(","))) for line in open("input.txt").read().strip().split("\n")]


data = read_file()
h = len(data) -1
w = len(data[0]) -1
res = deepcopy(data)

s = time.time()
print(solve())
print("runtime: ", time.time()-s)
