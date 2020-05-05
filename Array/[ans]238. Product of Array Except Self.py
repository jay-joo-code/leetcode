from typing import List
from collections import deque

# attempt 1 (derived from solution)
# time: O(n^2) space: O(n^2)
def productExceptSelf(nums: List[int]) -> List[int]:
	left = []
	right = deque([])
	
	for i in range(len(nums)):
		if i == 0:
			left.append(1)
			right.append(1)
		else:
			j = len(nums) - i - 1
			left.append(nums[i-1] * left[i-1])
			right.appendleft(nums[j+1] * right[0])

	return [left[k] * right[k] for k in range(len(nums))]

# attempt 2 (derived from Discuss section)
def productExceptSelfTwo(nums: List[int]) -> List[int]:
	res = []
	prev = 1
	for i in range(len(nums)):
		res.append(prev)
		prev *= nums[i]
	
	prev = 1
	for j in range(len(nums) - 1, -1, -1):
		res[j] = res[j] * prev
		prev *= nums[j]

	return res