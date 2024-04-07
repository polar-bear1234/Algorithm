"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，
请你构造并返回这颗二叉树
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def strucTree(self, inorder, postorder):
        '''中序+后序'''
        if not inorder or not postorder:
            return None
        mid_val = postorder.pop()
        ind = inorder.index(mid_val)
        root = TreeNode(mid_val)
        root.left = self.strucTree(inorder[:ind], postorder[:ind])
        root.right = self.strucTree(inorder[ind+1:], postorder[ind:])
        return root

    def buildTree(self, preorder, inorder):
        '''前序+中序'''
        if not preorder or not inorder:
            return None
        mid_node = preorder.pop(0)
        ind = inorder.index(mid_node)
        root = TreeNode(mid_node)
        root.left = self.buildTree(preorder[:ind], inorder[:ind])
        root.right = self.buildTree(preorder[ind:], inorder[ind + 1:])
        return root
