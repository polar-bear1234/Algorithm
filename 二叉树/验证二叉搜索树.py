class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(self, root: TreeNode) -> bool:
    # 验证二叉搜索树
    if not root:
        return True
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right:
            if node.right.val <= node.val:
                return False
            stack.append(node.right)
        if node.left:
            if node.left.val >= node.val:
                return False
            stack.append(node.left)
    return True