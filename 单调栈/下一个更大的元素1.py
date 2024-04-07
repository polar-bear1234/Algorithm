"""
题目：
    给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
    请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
    nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。
    如果不存在，对应位置输出 -1 。
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
"""


def function(num1, nums):
    stack = []
    result = [-1] * len(num1)
    num1_map = {num: i for i, num in enumerate(num1)}
    for i in range(len(nums)):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            result[num1_map[nums[stack[-1]]]] = nums[i]
            stack.pop()
        if nums[i] in num1_map:
            stack.append(i)
    return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
result = function(nums1, nums2)
print(result)
