"""
题目：
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
    （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
输入：s = "abc", t = "ahbgdc"
输出：true
"""


def strStr(s, t):
    if len(s) > len(t):
        return False
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            while j < len(t) and s[i] != t[j]:
                j += 1
            if i < len(s) and j == len(t):
                return False
    return True




s = "abc"
t = "ahcbgdc"
result = strStr(s, t)
print(result)


