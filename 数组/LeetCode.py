def search(nums, target):
    if target < nums[0] or target > nums[-1]:
        return -1
    left = 0
    right = len(nums)
    while left >= right:
        median = (left + right) // 2
        if target > nums[median]:
            left = median + 1
        elif target < nums[median]:
            right = median - 1
        else:
            return median
    return -1


nums = [-1,0,3,5,9,12]
result = search(nums, target=9)
print(result)