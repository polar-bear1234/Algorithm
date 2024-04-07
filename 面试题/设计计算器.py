# 基本计算器  单调栈
def calculate(s: str) -> int:
    stack = []
    operator_stack = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():   # 处理连续的数字字符，构建完整的数字
                num = num * 10 + int(s[i])
                i += 1
            stack.append(num)
        elif s[i] in operators:
            while operator_stack and operators[s[i]] <= operators[operator_stack[-1]]:   # 处理操作符
                apply_operator(stack, operator_stack)
            operator_stack.append(s[i])
            i += 1
        else:
            i += 1
    while operator_stack:
        apply_operator(stack, operator_stack)
    return stack[-1]


def apply_operator(stack, operator_stack):
    operator = operator_stack.pop()
    right = stack.pop()
    left = stack.pop()
    if operator == '+':
        stack.append(left + right)
    elif operator == '-':
        stack.append(left - right)
    elif operator == '*':
        stack.append(left * right)
    elif operator == '/':
        stack.append(int(left / right))


def calculate(s):
    ans = 0
    num = 0
    sign = 1
    stack = []
    for c in s:
        if 0 <= int(c) <= 9:
            num = num * 10 + int(c)
        elif c == '+' or c == '-':
            ans += num * sign
            num = 0
            sign = 1 if c == '+' else -1
        elif c == '(':
            stack.append(ans)
            stack.append(sign)
            ans = 0
            sign = 1
        elif c == ')':
            ans += num * sign
            num = 0
            ans *= stack.pop()
            ans += stack.pop()
    ans += num * sign
    return ans


# # 示例用法
# expression = '2 + 3*2'
# print(calculate(expression))  # 输出：8
