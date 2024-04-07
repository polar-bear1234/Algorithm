"""
题目：
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
"""
from collections import deque


class Solution:
    def numIslands_DFS(self, grid):
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(i, j):
            grid[i][j] = "0"
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                    dfs(tmp_i, tmp_j)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


class Solution2:
    def __init__(self):
        self.orients = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def numIslands_BFS(self, grid):
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if visited[i][j] == False and grid[i][j] == "1":
                    res += 1
                    self.bfs(grid, i, j, visited)
        return res

    def bfs(self, grid, i, j, visited):
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for k in range(len(self.orients)):
                next_i = x + self.orients[k][0]
                next_j = y + self.orients[k][1]
                if next_i < 0 or next_i > len(grid) or next_j < 0 or next_j > len(grid[0]):
                    continue
                if visited[next_i][next_j]:
                    continue
                if grid[next_i][next_j] == '0':
                    continue
                queue.append((next_i, next_j))
                visited[next_i][next_j] = True





