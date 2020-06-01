
# solution (accepted)
def maxProduct(self, A):
	# prefix product, suffix product. find max of the two
	B = A[::-1]
	for i in range(1, len(A)):
			A[i] *= A[i - 1] or 1
			B[i] *= B[i - 1] or 1
	return max(A + B)

# solution (accepted) better
def maxProduct(self, nums: List[int]) -> int:
	# variation of candane's algorithm
	res, mx, mn = -float('inf'), 1, 1
	for n in nums:
			if n < 0: mx, mn = mn, mx
			mx = max(mx * n, n)
			mn = min(mn * n, n)
			res = max(res, mx)
	return res
