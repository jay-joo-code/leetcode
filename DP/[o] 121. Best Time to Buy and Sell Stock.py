
# attempt (AC)
def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        
        mn = prices[0]
        dp = [0] * len(prices)
        
        for i in range(1, len(prices)):
            if prices[i] < mn:
                mn = prices[i]
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-1], prices[i]-mn)
        
        return dp[-1]
