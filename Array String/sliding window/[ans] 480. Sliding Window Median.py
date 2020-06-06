
# solution (accepted)
def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
	window = nums[:k-1]
	res = []
	
	for i in range(k-1, len(nums)):
			window.append(nums[i])
			window.sort()
			
			if k % 2:   # k is odd
					res.append(window[k // 2])
			else:
					res.append((window[k // 2] + window[k // 2 - 1]) / 2)
			
			window.remove(nums[i-k+1])
	
	return res
