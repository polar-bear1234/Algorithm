"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
输入：s = "()[]{}"
输出：true
"""


def isValid(str_):
    stack = []
    for s in str_:
        if s == "[":
            stack.append("]")
        elif s == "{":
            stack.append("}")
        elif s == "(":
            stack.append(")")
        elif stack and s in ["]", "}", ")"]:
            cur = stack.pop()
            if cur == s:
                continue
            else:
                return False
        elif not stack and s in ["]", "}", ")"]:
            return False
    return True if not stack else False


s = ")"
print(isValid(s))
