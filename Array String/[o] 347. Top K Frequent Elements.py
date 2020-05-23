
# attempt (accepted)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
	count = {}
	
	for num in nums:
		if num in count:
			count[num] += 1
		else:
			count[num] = 1
	
	order = sorted(count, key=lambda k:count[k], reverse=True)
	
	return order[:k]
