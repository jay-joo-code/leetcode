
# attempt (accepted) after many mistakes
def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
	intervals.sort(key=lambda arr : arr[0])

	i = 0
	while i < len(intervals)-1:
			if intervals[i][1] >= intervals[i+1][0]:
					intervals[i][1] = max(intervals.pop(i+1)[1], intervals[i][1])
			else:
					i += 1
					
	return intervals

