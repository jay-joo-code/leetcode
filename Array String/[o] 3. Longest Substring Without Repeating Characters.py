

# attempt (accepted)
def lengthOfLongestSubstring(self, s: str) -> int:
	maxcount = 0
	prev = []
	
	for char in s:
		if char in prev:
			prev = prev[prev.index(char)+1:]

		prev.append(char)
		maxcount = max(maxcount, len(prev))
	
	return maxcount