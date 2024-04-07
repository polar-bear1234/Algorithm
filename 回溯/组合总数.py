"""
题目：
    找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
    只使用数字1到9
    每个数字 最多使用一次
    返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
输入: k = 3, n = 7
输出: [[1,2,4]]

1. 参数与返回值
2. 退出条件
3. 单层递归逻辑
4. 剪枝

回溯算法： 通过递归嵌套N个for循环，本质还是暴力搜索，所有回溯算法解决的问题都可以抽象成一个树形结构
"""
 
def function(k, n):
    result = []
    path = []
    startIndex = 1
    Sum = 0
    backtracing(k, n, path, Sum, result, startIndex)
    return result


def backtracing(k, n, path, Sum, result, startIndex):
    if len(path) == k:
        if Sum == n:
            if sorted(path) not in result:
                result.append(sorted(path[:]))
        return
    for i in range(startIndex, n-(k-len(path))+2):
        path.append(i)
        Sum += i
        backtracing(k, n, path, Sum, result, i+1)
        Sum -= i
        path.pop()

k = 3
n = 7
result = function(k, n)
print(result)