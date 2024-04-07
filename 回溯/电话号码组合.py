"""
题目：
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution:
    def __init__(self):
        self.letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.result = []
        self.st = ""

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        ind = 0
        self.backtracing(digits, ind)
        return self.result

    def backtracing(self, digits, ind):
        if ind == len(digits):
            self.result.append(self.st)
            return
        digit = int(digits[ind])
        letter = self.letters[digit]
        for char in letter:
            self.st += char
            self.backtracing(digits, ind+1)
            self.st = self.st[:-1]


digits = "23"
g = Solution()
result = g.letterCombinations(digits)
print(result)
