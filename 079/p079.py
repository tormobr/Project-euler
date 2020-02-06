from collections import defaultdict

def solve():
    data = read_file()
    D = defaultdict(lambda: set())
    for x in data:
        for i, d1 in enumerate(str(x)):
            for d2 in str(x)[i+1:]:
                D[d1].add(d2)

    for k, v in D.items():
        DFS(D.copy(), k, [])
    
    return BFS(D.copy())
    
        
def DFS(D, k, path):
    path.append(k)
    for k2 in D[k]:
        DFS(D, k2, path.copy())
    if len(path) == len(D):
        print(path, len(path))

def BFS(D):
    for k in D.copy().keys():
        q = []
        q.append((k,[]))
        while q:
            current, path = q.pop(0)
            path.append(current)
            if len(path) == len(D):
                return (path, len(path))

            for k2 in D[current]:
                q.append((k2, path.copy()))


def read_file():
    return [int(x) for x in open("input.txt")]


print(solve())
