"""
题目：
    给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
"""

class Solution:
    def __init__(self):
        self.result = []
        self.path = [0]

    def dfs(self, graph, root):
        if root == len(graph) - 1:
            self.result.append(self.path[:])
        for node in graph[root]:
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop()

    def main(self, graph):
        if not graph:
            return 0
        self.dfs(graph, 0)
        return self.result


graph = [[1,2],[3],[3],[]]
g = Solution()
result = g.main(graph)
print(result)
