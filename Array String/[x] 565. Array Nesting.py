from typing import List

# atempt 1: simulation
# works for smaller inputs
# but time limit exceeded for larger inputs
# bc t: O(n^2)
def arrayNesting(nums: List[int]) -> int:
	maxlen = 0
	
	for i in range(len(nums)):
		set = [nums[i]]
		
		for j in range(1, len(nums)):
			if nums[set[-1]] not in set:
				set.append(nums[set[-1]])
		maxlen = max(maxlen, len(set))
	
	return maxlen

# solution: very similar, but mark elements that have already been simluated
# works bc cycles of numbers cannot overlap
def arrayNestingSol(nums):
	maxlen = 0
	seen = [0] * len(nums)
	
	for i in range(len(nums)):
		if not seen[i]:
			set = [nums[i]]
			seen[i] = 1
			
			for j in range(1, len(nums)):
				if nums[set[-1]] not in set:
					set.append(nums[set[-1]])
					seen[set[-1]] = 1
			maxlen = max(maxlen, len(set))
	
	return maxlen