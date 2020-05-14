
# attempt after refering to solutions (accepted)
def frequencySort(self, s: str) -> str:
	count = {}
	
	for char in s:
		if char in count: count[char] += 1
		else: count[char] = 1
	
	char_order = sorted(count, key=lambda k:count[k], reverse=True)
	res = ''
	for char in char_order:
		res += char * count[char]
	return res
