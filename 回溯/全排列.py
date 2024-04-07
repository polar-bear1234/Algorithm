"""
题目：
    1. 无重复数
    2. 有重复数，给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution:
    def function_without(self, nums):
        result = []
        path = []
        used = [False] * len(nums)
        self.backtracing(nums, used, path, result)
        return result

    def backtracing(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracing(nums, used, path, result)
            used[i] = False
            path.pop()

class Solution2:
    def function_with(self, nums):
        result = []
        path = []
        used = [False] * len(nums)
        nums.sort()
        self.backtracing(nums, used, path, result)
        return result

    def backtracing(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1] and used[i-1] == False) or used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracing(nums, used, path, result)
            used[i] = False
            path.pop()


nums1 = [1,2,3]
nums2 = [1,2,2]
g1 = Solution()
g2 = Solution2()
result1 = g1.function_without(nums1)
result2 = g2.function_with(nums2)
print(result1)
print(result2)

