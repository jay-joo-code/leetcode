
# attempt 1: recursion without DP
# 1008 ms
# t: O(2^n)
def fib(self, N: int) -> int:
        if N == 0:
            return 0

        if N == 1:
            return 1
        
        return self.fib(N - 1) + self.fib(N - 2)

# attempt 2: memoization
# 32 ms
# t: O(n)
def fib(self, N: int) -> int:
	memo = [None] * (N + 1)
	
	def compute(n: int) -> int:
		if memo[n]:
			return memo[n]
		
		if n == 0:
			memo[n] = 0
			return 0
		
		if n == 1:
			memo[n] = 1
			return 1
		
		res = compute(n - 2) + compute(n - 1)
		memo[n] = res
		return res
	
	return compute(N)