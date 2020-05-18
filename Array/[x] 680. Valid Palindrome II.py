

# solution
def validPalindrome(self, s: str) -> bool:
	# two pointers
	left, right = 0, len(s)-1
	
	while left < right:
		if s[left] != s[right]:
			s1 = s[left:right]
			s2 = s[left+1:right+1]
			return s1 == s1[::-1] or s2 == s2[::-1]
		left += 1
		right -= 1
	
	return True