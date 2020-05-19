
# attempt after viewing youtube solution
# https://www.youtube.com/watch?v=zdDeV5v_iUE
def trap(self, A: List[int]) -> int:
	left, right = [0], [0]
	
	for i in range(1, len(A)):
		left.append(max(A[i - 1], left[i - 1]))
		right.insert(0, max(A[len(A) - i], right[0]))
	
	res = 0
	for j in range(len(A)):
		res += max(min(right[j], left[j]) - A[j], 0)
	
	return res