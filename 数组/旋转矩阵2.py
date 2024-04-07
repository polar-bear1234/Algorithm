"""
题目：
    给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
输入: 3
输出: [ [ 1, 2, 3 ],
       [ 8, 9, 4 ],
       [ 7, 6, 5 ] ]
"""

import torch


def function(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n-1, 0, n-1
    while left <= right and top <= bottom:
        for col in range(left, right):    # [0, 2): 0,1
            matrix[top][col] = num
            num += 1
        for col in range(top, bottom):  # [0, 1): 0,1
            matrix[col][right] = num
            num += 1
        for col in range(right, left, -1):  # [2, 0): 2,1
            matrix[bottom][col] = num
            num += 1
        for col in range(bottom, top, -1):    # [2,0): 2,1,
            matrix[col][left] = num
            num += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    if n % 2 == 1:
        matrix[n//2][n//2] = n*n
    return matrix


n = 4
result = function(n)
print(torch.tensor(result))






