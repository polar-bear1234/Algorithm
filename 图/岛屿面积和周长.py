# 岛屿最大面积


def maxLand(grid):
    row = len(grid)
    col = len(grid[0])
    maxS = 0
    orients = [(0, 1), (0,-1), (1,0), (-1,0)]

    def dfs(i, j, ares):
        grid[i][j] = 0
        for x, y in orients:
            next_i, next_j = i + x, j + y
            if 0 <= next_i < row and 0 <= next_j < col and grid[next_i][next_j] == 1:
                ares = dfs(next_i, next_j, ares+1)
        return ares

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                ares = 1
                ares = dfs(i, j, ares)
                maxS = max(maxS, ares)
    return maxS


def landLen(grid):
    row, col = len(grid), len(grid[0])
    grid.append([0] * len(grid[0]))
    num = 0
    c = 0
    for i in range(row):
        grid[row].append(0)
        for j in range(col):
            if grid[i][j] == 1:
                num += 1
            if grid[i][j] == 1 and grid[i+1][j] == 1:
                c -= 2
            if grid[i][j] == 1 and grid[i][j+1] == 1:
                c -= 2
    return num * 4 + c


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

result = maxLand(grid)
print(result)