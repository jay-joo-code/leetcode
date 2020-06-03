
# attempt (accepted) after multiple mistakes
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
	if len(intervals) == 0:
			return 0
	
	# sort by int at index 1 (key point)
	intervals.sort(key=lambda arr: arr[1])
	
	i = 1
	count = 0
	
	while i < len(intervals):
			if intervals[i][0] < intervals[i-1][1]:
					count += 1
					intervals.pop(i)
			else:
					i += 1
					
	return count
