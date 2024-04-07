"""
题目：
    节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
示例1:
    输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
    输出：true
示例2:
    输入：
    n = 5,
    graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]],
    start = 0,
    target = 4
    输出 true
提示：
    节点数量n在[0, 1e5]范围内。
    节点编号大于等于 0 小于 n。
    图中可能存在自环和平行边。
"""
from collections import defaultdict, deque


def findPath_bfs(n, graph, start, target):
    dic = defaultdict(list)
    for u, v in graph:
        dic[u].append(v)
    print(dic)
    vic = set()                # 集合
    queue = deque()
    queue.append(start)
    while queue:
        pos = queue.popleft()
        if pos == target:
            return True
        for nxt in dic[pos]:
            if nxt not in vic:   # 如果某一个节点已经操作过，那就不重复操作，continue
                vic.add(nxt)
                queue.append(nxt)
    return False


def findPath_dfs(n, graph, start, target):
    '''深度优先搜索'''
    pass



if __name__ == "__main__":

    n = 3
    graph = [[0, 1], [0, 2], [1, 2], [1, 2]]
    start = 0
    target = 2
    result = findPath_bfs(n, graph, start, target)
    print(result)



