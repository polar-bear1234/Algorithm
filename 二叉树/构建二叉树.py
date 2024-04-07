class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


from collections import deque

nodes = [3, 9, 20, None, None, 15, 7]
class Solution:
	def structureTree(self, nodes):
		if not nodes:
			return None
		root = TreeNode(nodes[0])
		queue = deque([root])
		i = 0
		while queue and i < len(nodes):
			node = queue.popleft()
			if nodes[i]:
				node.left = TreeNode(nodes[i])
				queue.append(node.left)
			i += 1
			if i < len(nodes) and nodes[i]:
				node.right = TreeNode(nodes[i])
				queue.append(node.left)
			i += 1
		return root

	def strucTree2(self, nums):
		'''
		递归构建搜索二叉树
		nums: 升序数组
		'''
		if not nums:
			return None
		n = len(nums) // 2
		root = TreeNode(nums[n])
		root.left = self.strucTree2(nums[:n])
		root.right = self.strucTree2(nums[n+1:])
		return root


nums = [1,2,3,4,5,6]
g = Solution()
tree = g.strucTree2(nums)
print(tree.val, tree.left.val,tree.left.left.val, tree.left.right.val, tree.right.val)
print(tree.right.left.val, tree.right.right)





























