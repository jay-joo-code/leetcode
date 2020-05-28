
# attempt (TLE)
def minWindow(self, s, t):        
	chars = {}
	for char in t:
		if char not in chars:
			chars[char] = [None]
		else:
			chars[char].append(None)
	
	seen = 0
	res = ''
	res_length = float('inf')
	
	for i in range(len(s)):
		char = s[i]
		if char in t:
			arr = chars[char]
			
			if None in arr:
				arr[arr.index(None)] = i
			else:
				arr[arr.index(min(arr))] = i
		
		min_idx, max_idx = float('inf'), float('-inf')
		found_all = True
		for indexes in chars.values():
			if None in indexes:
				found_all = False
				break
				
			for idx in indexes:
				min_idx = min(idx, min_idx)
				max_idx = max(idx, max_idx)
		
		if found_all:
			length = max_idx - min_idx + 1

			if length < res_length:
				res = s[min_idx:max_idx+1]
				res_length = length
	
	return res
		
# attempt (incorrect)
def minWindow(self, s: str, t: str) -> str:
	# does not consider repeated chars
	maxpos = {}
	for char in t:
		maxpos[char] = -1
	res = ''
	res_length = float('inf')
	
	for i in range(len(s)):
		if s[i] in t:
			maxpos[s[i]] = i
			
			if -1 not in maxpos.values():
				order = sorted(maxpos, key=lambda k: maxpos[k])
				length = maxpos[order[-1]] - maxpos[order[0]] + 1
				
				if length < res_length:
					res = s[maxpos[order[0]]:maxpos[order[-1]]+1]
					res_length = length
	
	return res

# solution (accepted)
def minWindow(self, s, t):
	"""
	:type s: str
	:type t: str
	:rtype: str
	"""
	if len(s) < len(t):
		return ""
	
	hashmap = collections.Counter(t)
	counter = len(t)
	min_window = ""
	start, end = 0, 0
	
	
	for end in range(len(s)):
		if hashmap[s[end]] > 0:
			counter -= 1
		hashmap[s[end]] -= 1
		
		while counter == 0:
			length = end - start + 1
			
			if not min_window or len(min_window) > length:
				min_window = s[start:end+1]
			
			hashmap[s[start]] += 1

			if hashmap[s[start]] > 0:
				counter += 1
			
			start += 1
	return min_window


