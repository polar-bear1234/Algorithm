"""
题目：
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
    满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
    请你返回所有和为 0 且不重复的三元组。
    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]
"""
def three_sum(nums):
    result = []
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            return result
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ > 0:
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while right > left and nums[right] == nums[right - 1]:
                    right -= 1
                while right > left and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                right -= 1
    return result


nums = [1, -1, -1, 0]    # [[-2,-1,3],[-2,0,2],[-1,0,1]]
print(three_sum(nums))

