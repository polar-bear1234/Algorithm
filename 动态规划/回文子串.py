"""
0. 能构建的最长的回文串
    输入:s = "abccccdd"
    输出:7
1. 求回文子串的数量
    输入：s = "abc"
    输出：3
2. 求最长回文子串长度（可不连续）
    输入：s = "bbbab"
    输出：4
3. 输出最长回文子串
"""


class Solution:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.count = 0
        self.maxLen = 0
        self.maxStr = ""

    def longestPalindrome(self):
        hash_map = {}
        for s_ in self.s:
            if s_ not in hash_map:
                hash_map[s_] = 1
            else:
                hash_map[s_] -= 1
                if hash_map[s_] == 0:
                    del hash_map[s_]
        Sum = sum(list(hash_map.values()))
        nums = Sum - 1 if Sum >= 1 else 0
        return len(self.s) - nums

    def subStrCount(self):
        dp = [[False] * self.n for _ in range(self.n)]
        for i in range(self.n-1, -1, -1):
            for j in range(i, self.n):
                if self.s[i] == self.s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        self.count += 1
                    else:
                        if dp[i+1][j-1] == True:
                            dp[i][j] = True
                            self.count += 1
        return self.count

    def subStrMaxLen(self):
        dp = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            dp[i][i] = 1
        for i in range(self.n-1, -1, -1):
            for j in range(i+1, self.n):
                if self.s[i] == self.s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

    def subString(self):
        dp = [[False] * self.n for _ in range(self.n)]
        start = 0
        maxLen = 0
        for i in range(self.n-1, -1, -1):
            for j in range(i, self.n):
                if self.s[i] == self.s[j]:
                    if j - 1 <= 1:
                        dp[i][j] = True
                        if maxLen <= j - i:
                            start = i
                            maxLen = j - i
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                            if maxLen <= j - i:
                                start = i
                                maxLen = j - i
        return self.s[start: start + maxLen + 1]


if __name__ == "__main__":
    s1 = 'abccccdd'
    s2 = 'abc'
    s3 = 'bbbab'
    s4 = 'babad'
    g = Solution(s=s2)
    print(g.subStrCount())




