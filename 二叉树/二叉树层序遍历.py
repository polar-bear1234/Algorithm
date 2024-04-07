"""
题目：
    给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build_tree_from_list(self, nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

    def levelOrder(self, root):
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            tmp = []
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(tmp)
        return result


root = [3, 9, 20, None, None, 15, 7]


function = Solution()
new_root = function.build_tree_from_list(root)
print(new_root.val, new_root.left.val, new_root.right.val)
print(new_root.right.left.val, new_root.right.right.val)