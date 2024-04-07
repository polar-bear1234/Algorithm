"""
题目：
    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
    你可以按 任何顺序 返回答案。
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
def function(n, k):
    result = []
    path = []
    startIndex = 1
    backtracing(n, k, startIndex, path, result)
    return result


def backtracing(n, k, startIndex, path, result):
    if len(path) == k:
        result.append(path[:])
        return
    for i in range(startIndex, n+1):
        path.append(i)
        backtracing(n, k, i+1, path, result)
        path.pop()
