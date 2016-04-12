
n = int(input().strip())
grid = []
grid_i = 0

for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)


print(grid[0])

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if ((grid[i][j] > grid[i-1][j]) & (grid[i][j] > grid[i][j-1]) &
            (grid[i][j] > grid[i+1][j]) & (grid[i][j] > grid[i][j+1])):
            new_str = ''.join([grid[i][:j], "X", grid[i][j+1:]])
            grid[i] = new_str
    print(grid[i])

if n != 1:
    print(grid[n-1])
