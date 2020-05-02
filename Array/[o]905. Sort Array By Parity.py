from typing import List

# [o] attempt 1
def sortArrayByParity(nums: List[int]) -> List[int]:
	res = []
	
	for num in nums:
		if (num % 2 == 0):
			res.insert(0, num)
		else:
			res.append(num)
	return res

# solution 1: use built in sort
def sortArrayByParitySort(nums: List[int]) -> List[int]:
	nums.sort(key=lambda num : num % 2)
	return nums

# solution 2: quicksort (in-place sort)
def sortArrayByParityQuickSort(nums: List[int]) -> List[int]:
	i, j = 0, len(nums) - 1

	while i < j:
		if nums[i] % 2 > nums[j] % 2:
			nums[i], nums[j] = nums[j], nums[i]
		if nums[i] % 2 == 0: i++
		if nums[j] % 2 == 1: j++
	return nums
