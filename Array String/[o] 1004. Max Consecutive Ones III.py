
# attempt (accepted)
def longestOnes(self, A: List[int], k: int) -> int:
	if 0 not in A:
			return len(A)
	
	mx = float('-inf')
	start = 0
	zero_idx = A.index(0)
	count = { 0: 0, 1: 0 }
	
	for i in range(len(A)):
			count[A[i]] += 1
			
			if count[0] > k:
					for j in range(start, zero_idx+1):
							count[A[j]] -= 1
					start = zero_idx + 1
					if 0 in A[start:]:
							zero_idx = A.index(0, start)
			
			mx = max(mx, i - start + 1)
	
	return mx
