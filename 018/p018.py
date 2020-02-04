
import time

def solve():
    data = read_file()
    return rec(data, 0, 0)

def rec(data, level, i):
    if level == len(data)-1:
        return data[level][i]

    left = rec(data, level+1, i)
    right = rec(data, level+1, i+1)
    return data[level][i] + max(left, right)
        


def read_file():
    ret = []
    with open("input.txt") as fd:
        for line in fd:
            ret.append(list(map(int, line.split())))
    return ret


print(solve())
