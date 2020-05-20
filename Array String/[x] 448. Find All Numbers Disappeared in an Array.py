
# solution 1: with extra space
def findDisappearedNumbers(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	marked = set(nums)
	return [i for i in range(1, len(nums)+1) if i not in marked]

# solution 2: without extra space
def findDisappearedNumbersTwo(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	# mark numbers that exist 
	# by setting the numbers in the corresponding index as negative
	# indexes that contain numbers that are positive 
	# are not included in numbs
	# and are therefore the answers
	nums = [0] + nums

	for i in range(len(nums)):
		index = abs(nums[i])
		nums[index] = -abs(nums[index])
	
	return [i for i in range(len(nums)) if nums[i] > 0]