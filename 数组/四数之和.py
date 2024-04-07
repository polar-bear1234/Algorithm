"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
class Solution:
    def fourAdd(self, nums, target):
        nums = sorted(nums, reverse=False)
        result = []
        for i in range(len(nums)):
            if nums[i] > target > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] > target > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    addSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if addSum > target:
                        right -= 1
                    elif addSum < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        right -= 1
        return result


