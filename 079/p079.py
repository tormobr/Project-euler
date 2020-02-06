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
        
def DFS(D, k, path):
    path.append(k)
    for k2 in D[k]:
        if k2 not in path:
            DFS(D, k2, path.copy())
    print(path, len(path))


def read_file():
    return [int(x) for x in open("input.txt")]


print(solve())
