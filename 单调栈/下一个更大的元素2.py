"""
题目：
    给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
    数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
    这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
"""


def functions(nums):
    stack = []
    result = [-1] * (len(nums) * 2)
    for I in range(len(nums) * 2):
        i = I % len(nums)
        while len(stack) > 0 and nums[i] > nums[stack[-1] % len(nums)]:
            result[stack[-1]] = nums[i]
            stack.pop()
        stack.append(I)
    return result[:len(nums)]


nums = [1,2,1]
result = functions(nums)
print(result)
