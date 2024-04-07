class Solution:
    """
        如果左括号数量不大于 n，可以放一个左括号。
        如果右括号数量小于左括号的数量，我们可以放一个右括号
    """
    def generateParenthesis(self, n):
        result = []
        path = []
        left, right = 0, 0
        self.backtracing(n, result, path, left, right)
        return result

    def backtracing(self, n, result, path, left, right):
        if len(path) == n * 2:
            result.append(''.join(path))
            return
        if left < n:
            path.append('(')
            self.backtracing(n, result, path, left+1, right)
            path.pop()
        if right < left:
            path.append(')')
            self.backtracing(n, result, path, left, right+1)
            path.pop()


n = 4
g = Solution()
result = g.generateParenthesis(n)
print(result)