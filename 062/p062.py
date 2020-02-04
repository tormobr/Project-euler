
import time
from itertools import permutations

def solve():
    cubes = gen_cube(10000)
    for k, v in cubes.items():
        
        for k1, v1 in cubes.items():
            if sorted(str(k)) == sorted(str(k1)):
                cubes[k].append(k1)
                if len(cubes[k]) == 5:
                    return cubes[k], min(cubes[k])

def gen_cube(n):
    return {i**3:[] for i in range(1, n)}

print("result: ",solve())
