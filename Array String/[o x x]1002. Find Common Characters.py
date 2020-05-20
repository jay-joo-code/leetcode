from typing import List

# attempt 2 (accepted)
def commonChars(A: List[str]) -> List[str]:
	res = []
        for char in A[0]:
            contains_all = True
            for i in range(1, len(A)):
                if char in A[i]:
                    A[i] = A[i].replace(char, '', 1)
                else:
                    contains_all = False
            
            if contains_all:
                res.append(char)
        
        return res

# solution 1
def commonCharsSol(A: List[str]) -> List[str]:
	result = []

	# uses set to get unique chars of A[0]
	for c in set(A[0]): # loop chars in the first string
		minCharCount = A[0].count(c)
		stringsWithChar = 1
		for i in range(1,len(A)): # loop other strings in A
			if c in A[i]:
				minCharCount = min(minCharCount, A[i].count(c))
				stringsWithChar += 1
			else:
				break
		if stringsWithChar == len(A): 
			for i in range(minCharCount):
				result.append(c)
				
	return result

res = commonChars(['aaaaaa', 'aaa'])
print(res)