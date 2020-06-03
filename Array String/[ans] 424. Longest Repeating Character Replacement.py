
# solution (accepted)
def characterReplacement(self, s: str, k: int) -> int:
	count = {}
	mx = float('-inf')
	start = res = 0
	
	for end in range(len(s)):
			# add char to count
			count[s[end]] = count.get(s[end], 0) + 1
			
			# update mx
			mx = max(mx, count[s[end]])
			
			# if number of chars that need replacement in current window
			# is greater than k
			if end - start + 1 - mx > k:
					count[s[start]] -= 1
					start += 1
			
			res = max(res, end - start + 1)
	
	return res
