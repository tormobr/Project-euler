
import time

def solve():
    data = read_file()
    for i in range(len(data)-1, 0, -1):
        for j in range(len(data[i])-1):
            data[i-1][j] += max(data[i][j], data[i][j+1])
    return data[0][0]


def read_file():
    return [[int(x) for x in line.split()] for line in open("input.txt")]

print(solve())
