"""
定义构造三叉搜索树规则如下： nums = [100, 200, 300, 400, 600, 700, 800]
    每个节点都存有一个数，当插入一个新的数时，从根节点向下寻找，直到找到一个合适的空节点插入。
    查找的规则是：
        1. 如果数小于节点的数减去500，则将数插入节点的左子树
        2. 如果数大于节点的数加上500，则将数插入节点的右子树
        3. 否则，将数插入节点的中子树
给你一系列数，请按以上规则，按顺序将数插入树中，构建出一棵三叉搜索树，最后输出树的高度。
"""
class TreeNode:
    def __init__(self, val=0, left=None, mid=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.mid = mid

class Solution:
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val - 500:
            root.left = self.insert(root.left, val)
        elif val > root.val + 500:
            root.right = self.insert(root.right, val)
        else:
            root.mid = self.insert(root.mid, val)
        return root

    def strucTree(self, nums):
        root = None
        for num in nums:
            root = self.insert(root, num)
        return root

    def cal_height(self, root):
        if not root:
            return 0
        left = self.cal_height(root.left)
        mid = self.cal_height(root.mid)
        right = self.cal_height(root.right)
        return max(left, mid, right) + 1


nums = [100, 200, 300, 400, 600, 700, 800]
nums2 = [800, 200, 600, 1500, 100]
g = Solution()
tree = g.strucTree(nums2)
print(tree.val, tree.left.val, tree.mid.val, tree.right.val)
print(tree.left.mid.val)
height = g.cal_height(tree)
print('height is:', height)