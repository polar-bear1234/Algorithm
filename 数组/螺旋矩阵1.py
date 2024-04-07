"""
题目：
    给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""

import torch


def function(matrix):
    if not matrix:
        return []
    result = []
    m = len(matrix)
    n = len(matrix[0])
    left, right, top, bottom = 0, n-1, 0, m-1
    while True:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        if top > bottom:
            break
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        if right < left:
            break
        for i in range(right, left-1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1
        if bottom < top:
            break
        for i in range(bottom, top-1, -1):
            result.append(matrix[i][left])
        left += 1
        if left > right:
            break
    return result


matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[6, 9, 7]]
# print("答案:", [1,2,3,4,8,12,11,10,9,5,6,7])
result = function(matrix)
print("输出:", result)
