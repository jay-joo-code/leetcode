
# attempt (accepted)
# several minor mistakes 
def minRemoveToMakeValid(self, s: str) -> str:
	open = 0
	
	for char in s:
		if char == '(':
			open += 1
		elif char == ')':
			if open > 0:
				open -= 1
			else:
				s = s.replace(')', '', 1)
	
	if open == 0:
		return s
	elif open > 0:
		res = ''
		for i in range(len(s)-1, -1, -1):
			if s[i] != '(' or open == 0:
				res = s[i] + res
			else:
				open -= 1
				
		return res