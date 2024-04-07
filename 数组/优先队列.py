"""
题目:
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回 滑动窗口中的最大值 。
    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        q = deque()
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] < i - k + 1:
                q.popleft()
            if i >= k - 1:
                result.append(nums[q[0]])
        return result

    def func(self, nums, k):
        result = []
        queue = deque()
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            while queue[0] < i - k + 1:
                queue.popleft()
            if i > k - 1:
                result.append(nums[queue[0]])
        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
f = Solution()
print(f.maxSlidingWindow(nums, k))


















