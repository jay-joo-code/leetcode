

# attempt (AC)
def numSquares(self, n: int) -> int:
        squares = []
        
        for i in range(2, n):
            square = i*i
            if square <= n:
                squares.append(square)
            else:
                break
                
        dp = [0, 1] + [None] * (n-1)
        
        for i in range(1, n+1):
            if i in squares:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + 1
                for square in squares:
                    if square < i:
                        dp[i] = min(dp[i], dp[i-square]+dp[square])
                        
        
        return dp[-1]