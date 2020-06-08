
# solution (AC)
def mctFromLeafValues(self, arr: List[int]) -> int:
			memo = {}
			def dfs(i,j):
					if i + 1 == j: return 0 # tree of size 1
					if (i,j) not in memo:
							ans = float('inf')
							# k i+1 -> j-1
							for k in range(i+1,j):
									left = dfs(i,k) # i to exclusive-k, which return=0 when i+1=k
									right = dfs(k,j) # k to exclusive-j, which return=0 when k+1=j
									root = max(arr[i:k]) * max(arr[k:j])
									total = left + right + root
									ans = min(ans, total)
							memo[(i,j)] = ans
					return memo[(i,j)]
					
			return dfs(0, len(arr))
