from collections import deque

def mem_queue(nums, k):
	q = deque()
	result = []
	for i in range(len(nums)):
		while q and nums[i] < nums[q[-1]]:
			q.pop()
		q.append(i)
		while q and q[0] < i - k + 1:
			q.popleft()
		if i >= k - 1:
			result.append(nums[q[0]])
	return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(mem_queue(nums, k))