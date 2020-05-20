from typing import List

# attempt 1: accepted, considered optimal by community
# two pointers keep track of next index to place odd and even numbers, respectively
def sortArrayByParityII(A: List[int]) -> List[int]:
	res = [None] * len(A)
	evenI, oddI = 0, 1
	
	for n in A:
		if (n % 2 == 0):
			res[evenI] = n
			evenI += 2
		else:
			res[oddI] = n
			oddI += 2
	return res

