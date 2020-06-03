
# attempt (TLE)
def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        count = 0
        
        for start in range(len(A)):
            ints = set()
            for end in range(start, len(A)):
                ints.add(A[end])
                
                if len(ints) == K:
                    count += 1
                elif len(ints) > K:
                    break
        
        return count

# solution (accepted)
# still not fully understood
# try seeing in python visualiser
def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
	freq = {}
	start = 0
	start_k = 0
	res = 0
	for i, x in enumerate(A):
			freq[x] = freq.get(x, 0) + 1
			if len(freq) > K:
					# remove the distinct at start_k, move start_k, move start
					freq.pop(A[start_k])
					start_k += 1
					start = start_k
			if len(freq) == K:
					# update start_k and res (Notice: K >= 1)
					while freq[A[start_k]] > 1:
							freq[A[start_k]] -= 1
							start_k += 1
					res += start_k - start + 1
	return res
