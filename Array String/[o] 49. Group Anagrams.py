
# attempt (accepted) slow
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	combs = []
	res = []
	
	for str in strs:
		comb = {}
		for char in str:
			if char not in comb:
				comb[char] = 1
			else:
				comb[char] += 1
		
		if comb in combs:
			idx = combs.index(comb)
			res[idx].append(str)
		else:
			combs.append(comb)
			res.append([str])
	
	return res

# solution (accepted) much faster
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	d = {}
	for str in strs:
		key = tuple(sorted(str))
		d[key] = d.get(key, []) + [str]
	return d.values()

