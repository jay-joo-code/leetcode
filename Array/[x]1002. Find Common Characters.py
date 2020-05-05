from typing import List

# solution 1
def commonChars(A: List[str]) -> List[str]:
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