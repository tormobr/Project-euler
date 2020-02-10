import heapq
from copy import deepcopy
from collections import defaultdict
import time

def solve():
    d = create_dict()
    return dijkstra(d)


def dijkstra(d):
    dist = defaultdict(int) 
    SEEN = set()
    q = [(0,(0,0))]
    while q:
        val, current  = heapq.heappop(q)
        SEEN.add(current)
        for k,v in d[current].items():
            new_val = val + d[current][k]
            if dist[k] == 0 or dist[k] > new_val:
                dist[k] = new_val
            if k not in SEEN:
                heapq.heappush(q, (new_val, k))
    return dist[(n-1, m-1)] + data[0][0]

    

def create_dict():
    d = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        for j in range(m):
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0 <= i+dy < n and 0 <= j+dx < m:
                    d[(i,j)][(i+dy, j+dx)] = data[i+dy][j+dx]
    return d

def read_file():
    return [list(map(int, line.split(","))) for line in open("input.txt").read().strip().split("\n")]


s = time.time()
data = read_file()
n = len(data)
m = len(data[0])
res = deepcopy(data)

print(solve())
print("runtime: ", time.time()-s)
