"""
寻找数组里最长连续子数组的长度。
要求：时间复杂度不超过O(n)
例如：
    输入：nums = [100, 2, 200, 1, 3, 5, 4]
    输出：5（解释1,2,3,4,5)
"""
def function(nums):
    if not nums:
        return 0
    max_length = 0
    nums_set = set(nums)
    for num in nums:
        if (num - 1) not in nums_set:
            current_num = num
            current_length = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


def function2(nums):
    hash_set = set(nums)
    max_length = 0
    for num in nums:
        if num - 1 not in hash_set:
            current_num = num
            current_length = 1
            while current_num + 1 in hash_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


nums = [100, 2, 200, 1, 3, 5, 4]
result = function(nums)
print(result)