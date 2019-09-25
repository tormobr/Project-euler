
def solve(n, grid): 
    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] = grid[i][j-1] + grid[i-1][j] 

n = 20
grid = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    grid[0][i] = i+2
    grid[i][0] = i+2
solve(n, grid)


for row in grid:
    print(row)


