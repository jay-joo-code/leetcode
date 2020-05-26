
# attempt (accepted) multiple mistakes until accepted
def longestPalindrome(self, s: str) -> str:        
	longest = ''
	
	for i in range(len(s)):
		width = 1
		while i-width >= 0 and i+width < len(s):
			if s[i-width] == s[i+width]:
				width += 1
			else:
				break
		
		if len(longest) < (width-1) * 2 + 1:
			longest = s[i-width+1:i+width]
		
		width = 0
		while i-width >= 0 and i+width+1 < len(s):
			if s[i-width] == s[i+width+1]:
				width += 1
			else:
				break

		if len(longest) < (width) * 2:
			longest = s[i-width+1:i+width+1]
	
	return longest

# solution (accepted)
def longestPalindrome(self, s: str) -> str:
	res = ""
	for i in range(len(s)):
		# odd case, like "aba"
		tmp = self.helper(s, i, i)
		if len(tmp) > len(res):
			res = tmp
		# even case, like "abba"
		tmp = self.helper(s, i, i+1)
		if len(tmp) > len(res):
			res = tmp
	return res

# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
	while l >= 0 and r < len(s) and s[l] == s[r]:
		l -= 1; r += 1
	return s[l+1:r]