
# attempt 1 (failed)
def subarraySum(self, nums: List[int], k: int) -> int:
	# doesn't consider negative elements in nums
	acc = 0
	count = 0
	
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			acc += nums[j]
			
			if acc == k:
				count += 1
				acc = 0
				break
				
			elif acc > k:
				acc = 0
				break
	
	return count

# attempt 2 (failed)
def subarraySum(self, nums: List[int], k: int) -> int:
	# uses matrix as DP to store previous sums
	# still exceeds time limit
	count = 0
	matrix = [[None] * len(nums) for _ in range(len(nums))]
	
	for i in range(len(nums)):
		if nums[i] == k: count += 1
		matrix[i][i] = nums[i]
	
	for row in range(len(nums)-1):
		for col in range(row+1, len(nums)):
			if row == 0:
				matrix[row][col] = matrix[row][col-1] + nums[col]
			else:
				matrix[row][col] = matrix[row-1][col] - nums[row-1]
			
			if matrix[row][col] == k:
				count += 1
	
	return count

# solution
def subarraySum(self, nums: List[int], k: int) -> int:
	count = 0
	sum = 0
	sums = { 0: 1 }
	
	for num in nums:
		sum += num
		if sum-k in sums:
			count += sums[sum-k]
			
		if sum in sums:
			sums[sum] += 1
		else: 
			sums[sum] = 1
	
	return count