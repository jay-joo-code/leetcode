
# attempt (accepted) referred to solutions
def coinChange(self, coins: List[int], amount: int) -> int:
	dp = [0] + [float('inf')] * (amount)
	
	for coin in coins:
			if coin < len(dp):
					dp[coin] = 1
	
	for i in range(1, amount+1):
			for j in range(len(coins)):
					if coins[j] <= i:
							dp[i] = min(dp[i], dp[i-coins[j]] + 1)
	
	if dp[amount] == float('inf'):
			return -1
	
	return dp[amount]
