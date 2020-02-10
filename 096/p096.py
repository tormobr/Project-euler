
import time
import numpy as np
from matplotlib import pyplot as plt

class Solver:
    def __init__(self):
        self.grid = None
        self.solutions = []
        self.found = False

    def read_file(self, filename):
        with open("input.txt") as fd:
            grids = []
            rows = []
            for line in fd:
                if "Grid" in line:
                    grids.append(rows.copy())
                    rows = []
                    continue
                rows.append([int(c) for c in line.strip()])
            grids.append(np.array(rows.copy()))
        return grids

    def solve(self, x, y):
        if self.found:
            return
        if x == 8 and y == 8 and self.grid[y,x] != 0:
            return
        if self.grid[y,x] != 0:
            self.solve(*self.get_new_xy(x,y))
            return 

        options = []
        for i in range(1,10):
            if self.horizontal(i,x,y) and self.vertical(i,x,y) and self.box(i,x,y):
                options.append(i)
        if options:
            for o in options:
                self.grid[y,x] = o
                if not 0 in self.grid:
                    self.solutions.append(np.copy(self.grid)) 
                    self.found = True
                    return
                if y == 8 and x == 8:
                    return
                self.solve(*self.get_new_xy(x,y))
        self.grid[y,x] = 0

    def get_new_xy(self, x, y):
        if x == 8:
            return (0,y+1)
        return (x+1, y)




    def horizontal(self, val, x,y):
        if val in self.grid[y]:
            return False
        return True

    def vertical(self, val, x,y):
        for i in range(len(self.grid[x])):
            if val == self.grid[i,x]:
                return False
        return True

    def box(self, val, x,y):
        x_cor = (x // 3) * 3
        y_cor = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if val == self.grid[y_cor+i, x_cor+j]:
                    return False
        return True
                
    def __repr__(self):
        return self.pretty_print(self.grid)

    def pretty_print(self, arr):
        ret = "\n\n"
        for i,y in enumerate(arr):
            for j,x in enumerate(y):
                ret += str(x) + " "
                if ((j+1) % 3) == 0 and j != 8:
                    ret += "|"
            if ((i+1) % 3) == 0 and i != 8:
                ret += "\n-------------------"
            ret += "\n"
        return ret


if __name__ == "__main__":
    s = Solver()
    grids = s.read_file("input.txt")
    #print(grids)
    for i,g in enumerate(grids[1:]):
        #print(g)
        s.found = False
        s.grid = np.copy(np.array(g))
        s.solve(0,0)
        print(i, "numsols:", len(s.solutions))
    res = 0
    for grid in s.solutions:
        res += int("".join(list(map(str,grid[0][0:3]))))
    print("result: ", res)

