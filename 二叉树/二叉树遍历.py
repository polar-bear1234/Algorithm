"""
1. 定义二叉树
2. 构建二叉树
3. 遍历二叉树（前序、中序、后序）【递归/迭代】、（层序）
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build_binaryTree_from_list(self, nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

    def layer_traversal(self, root):
        root = self.build_binaryTree_from_list(root)
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result

    def pre_traversal(self, root):
        '''前序遍历-递归'''
        result = []
        def traversal(root, result):
            if not root:
                return
            result.append(root.val)
            if root.left:
                traversal(root.left, result)
            if root.right:
                traversal(root.right, result)
        traversal(root, result)
        return result

    def pre_traversal_(self, root):
        '''前序遍历-迭代'''
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result

    def med_traversal(self, root):
        '''中序遍历-递归'''
        result = []
        def traversal(root, result):
            if not root:
                return
            if root.left:
                traversal(root.left, result)
            result.append(root.val)
            if root.right:
                traversal(root.right, result)
        traversal(root, result)
        return result

    def med_traversal_(self, root):
        '''中序遍历-迭代'''
        result = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node.val)
            cur = node.right
        return result

    def post_traversal(self, root):
        '''后序遍历-递归'''
        result = []
        def traversal(root, result):
            if not root:
                return
            if root.left:
                traversal(root.left, result)
            if root.right:
                traversal(root.right, result)
            result.append(root.val)
        traversal(root, result)
        return result

    def post_traversal_(self, root):
        '''后续遍历-迭代'''
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result[::-1]

    def recursive_traversal(self, nums):
        root = self.build_binaryTree_from_list(nums)
        # result = self.pre_traversal(root)
        # result = self.pre_traversal_(root)
        # result = self.med_traversal(root)
        # result = self.med_traversal_(root)
        result = self.post_traversal_(root)
        return result


if __name__ == "__main__":
    nums1 = [3, 9, 20, None, None, 15, 7]
    nums2 = [1, None, 2, 3]
    solu = Solution()
    # root = solu.build_binaryTree_from_list(nums1)
    # print(root.val,
    #       root.left.val, root.right.val,
    #       root.left.left.val, root.left.right.val,
    #       root.right.left.val, root.right.right.val
    #     )
    # result = solu.layer_traversal(root)
    result = solu.recursive_traversal(nums1)
    print("Origin root list is:", nums1)
    print("Traversal list is:", result)
