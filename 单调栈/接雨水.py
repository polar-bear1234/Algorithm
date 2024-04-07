"""
题目：
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6

输入：height = [4,2,0,3,2,5]
输出：9
"""


def functions(height):
    stack = []
    result = [0] * len(height)
    for i in range(len(height)):
        while len(stack) > 0 and height[i] >= height[stack[-1]]:
            result[stack[-1]] = height[i]
            stack.pop()
        stack.append(i)
    return result


def rain(height):
    sum_ = 0
    stack = [0]
    for i in range(1, len(height)):
        if height[i] < height[stack[-1]]:
            stack.append(i)
        elif height[i] == height[stack[-1]]:
            # stack.pop()
            stack.append(i)
        else:
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if len(stack) > 0:
                    h = min(height[i], height[stack[-1]])
                    w = i - stack[-1] - 1
                    sum_ += (h - height[mid]) * w
            stack.append(i)
    return sum_


height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
# result1 = functions(height1)
# result2 = functions(height2)
# print(result1)
# print(result2)
sum1 = rain(height1)
# sum2 = rain(height2)
print(sum1)
# print(sum2)
