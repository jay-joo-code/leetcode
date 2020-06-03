
# attempte (accepted)
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
	mx = max(nums[:k])
	res = [mx]
	
	for i in range(k, len(nums)):
			# update mx
			if nums[i] > mx:
					mx = nums[i]
			elif nums[i-k] == mx:
					mx = max(nums[i-k+1:i+1])
			
			res.append(mx)
	
	return res