
# attempt (accepted) better than solution tbh
def findLength(self, A: List[int], B: List[int]) -> int:
	dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
	max_len = 0
	for i in range(len(A)):
			for j in range(len(B)):
					if A[i] == B[j]:
							prev_len = 0
							if i-1 >= 0 and j-1 >=0:
									prev_len = dp[i - 1][j - 1]
							val = prev_len + 1
							dp[i][j] = val
							max_len = max(max_len, val)
	return max_len

# solution
def findLength(self, A, B):
	dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i - 1] == B[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
	return max(max(row) for row in dp)
