from collections import deque
"""
BFS模版：
https://leetcode.cn/problems/01-matrix/solutions/203364/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-2/

queue = deque()
while queue:
    cur = queue.popleft()
    for node in node_list:
        if node not in set():
            queue.append(node)

level = 0
while queue:
    size = len(queue)
    for i in range(size):
        cur = queue.popleft()
        for node in node_list:
            if node not in set()
                queue.append(node)
    level += 1
"""

from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        row, col = len(matrix), len(matrix[0])
        queue = deque()
        visited = [[0]*col for _ in range(row)]   # 标识哪些操作过了，哪些没有操作过，操作过的全部为1
        res = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                if matrix[x][y] == 1:
                    res[x][y] = step      # 按照层叠加
                for dx, dy in dirs:
                    next_i, next_j = x + dx, y + dy
                    if next_i < 0 or next_i >= row or next_j < 0 or next_j >= col or visited[next_i][next_j] == 1:
                        continue
                    queue.append((next_i, next_j))
                    visited[next_i][next_j] = 1
            step += 1
        return res

mat = [[0,0,0],[0,1,0],[1,1,1]]
g = Solution()
result = g.updateMatrix(mat)
print(result)