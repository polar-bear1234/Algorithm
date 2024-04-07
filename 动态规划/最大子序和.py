"""
题目：
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
"""


def maxSum(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    result = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        result = max(dp[i], result)
    return result


nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSum(nums)
print(result)
