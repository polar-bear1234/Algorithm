"""
题目：
    给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
    回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
    回文串不一定是字典当中的单词。
输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
"""


def canPermutePalindrome(s):
    hash_map = {}
    for char in s:
        if char not in hash_map:
            hash_map[char] = 1
        else:
            if hash_map[char] == 1:
                hash_map[char] -= 1
            else:
                hash_map[char] += 1
    return list(hash_map.values()).count(1) == 1 or list(hash_map.values()).count(1) == 0
