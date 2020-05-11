from typing import List

# solution
# if accumulated sum of A matches accum sum of index
# is valid chunk
def maxChunksToSorted(A: List[int]) -> int:
	index_sum = 0
	A_sum = 0
	count = 0
	for i in range(len(A)):
		index_sum += i
		A_sum += A[i]
		if index_sum == A_sum:
			count += 1
	
	return count