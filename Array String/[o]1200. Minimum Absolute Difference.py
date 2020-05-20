from typing import List

# attempt 1: correct
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
	if (len(arr) == 0 or len(arr) == 1): return []
	
	arr.sort()
	res = [[arr[0], arr[1]]]
	min = arr[1] - arr[0]
	
	for i in range(2, len(arr)):
		diff = arr[i] - arr[i-1]
		
		if (diff < min):
			res = []
			min = diff
			res.append([arr[i-1], arr[i]])
		
		elif (diff == min):
			res.append([arr[i-1], arr[i]])
	
	return res