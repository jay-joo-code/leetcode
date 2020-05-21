
# attempt (accepted)
def twoSum(self, nums: List[int], target: int) -> List[int]:
	for i in range(len(nums)):
		searching = target - nums[i]
		
		if searching in nums[i+1:]:
			j = nums[i+1:].index(searching) + i+1
			return [i, j]