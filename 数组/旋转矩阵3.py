"""旋转90度"""
import torch

def rotate(matrix):
    dim = len(matrix)
    new_matrix = [[0] * dim for _ in range(dim)]
    for row in range(dim):
        for col in range(dim):
            new_matrix[col][dim - row - 1] = matrix[row][col]
    return new_matrix


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
result = rotate(matrix)
print(torch.tensor(matrix))
print(torch.tensor(result))