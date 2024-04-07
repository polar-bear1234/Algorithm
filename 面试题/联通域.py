"""二阶矩阵，0，1 多个1相连，联通矩阵"""


def function(nums):
    if not nums:
        return 0
    count = 0
    row = len(nums)
    col = len(nums[0])
    orients = [[0,1],[0,-1],[1,0],[-1,0]]

    def dfs(i, j):
        nums[i][j] = 0
        for x, y in orients:
            next_i = i + x
            next_j = j + y
            if 0 <= next_i < row and 0 <= next_j < col and nums[next_i][next_j] == 1:
                dfs(next_i, next_j)

    for i in range(row):
        for j in range(col):
            if nums[i][j] == 1:
                dfs(i, j)
                count += 1
    return count


matrix = [[1,1,1,0,0,1],
          [0,0,1,1,0,1],
          [1,1,0,0,1,1],
          [0,1,0,0,1,1]]

result = function(matrix)
print(result)
