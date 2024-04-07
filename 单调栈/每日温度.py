"""
题目：
    请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
    如果气温在这之后都不会升高，请在该位置用 0 来代替。
输入：temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
输出： [1, 1, 4, 2, 1, 1, 0, 0]。
"""


def temperature_cal(temp):
    stack = []
    result = [0] * len(temp)
    for i in range(len(temp)):
        while len(stack) > 0 and temp[i] > temp[stack[-1]]:
            result[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
output = [1, 1, 4, 2, 1, 1, 0, 0]
result = temperature_cal(temperatures)
print("标准答案：", output)
print("我的输出：", result)
