
import time

def solve():
    data = read_file()
    for i, line in enumerate(data[::-1]):
        for j, elem in enumerate(data[i]):
            print(elem)




    #return rec(data, 0, 0)

def rec(data, level, i):
    print(level, i)
    if level == len(data)-1:
        return data[level][i]

    left = rec(data, level+1, i)
    right = rec(data, level+1, i+1)
    return data[level][i] + max(left, right)

def read_file():
    return [[int(x) for x in line.split()] for line in open("input.txt")]

print(solve())
