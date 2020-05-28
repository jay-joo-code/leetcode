
# attempt (accepted), after many mistakes
def findAnagrams(self, s: str, p: str) -> List[int]:
	chars = {}
	target = {}
	for char in p:
		chars[char] = 0
		
		if char not in target:
			target[char] = 1
		else:
			target[char] += 1

	res = []
	
	for i in range(len(s)):
		if s[i] in p:
			chars[s[i]] += 1
		
		if i > len(p)-1 and s[i-len(p)] in chars:
			chars[s[i-len(p)]] = max(chars[s[i-len(p)]]-1, 0)
		
		if i >= len(p)-1 and chars == target:
			res.append(i-len(p)+1)
			
	return res
