
# attempt (accepted)
def climbStairs(self, n: int) -> int:
	if not n:
			return 0
	if n == 1:
			return 1
	if n == 2:
			return 2
	
	dp = [1, 2] + [0] * (n-2)
	
	for i in range(2, len(dp)):
			dp[i] = dp[i-2] + dp[i-1]
	
	return dp[-1]
