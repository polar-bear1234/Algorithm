"""
字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
"""


def oneEditAway(first, second):
    if first == second:
        return True
    if abs(len(first) - len(second)) == 1 and max(len(first), len(second)) == 1:
        return True
    if abs(len(first) - len(second)) > 1:
        return False
    if len(first) > len(second):
        large, little = first, second
    else:
        left, right = second, first
    count = 0
    i = 0
    j = 0
    while i < len(left):
        if left[i] == right[j]:
            i += 1
            j += 1
        else:
            i += 1
            count += 1
            if count > 1:
                return False
    return True


first = ""
second = "a"
print(oneEditAway(first, second))