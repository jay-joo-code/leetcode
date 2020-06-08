
# solution (AC)
def numTrees(self, n):
	res = [0] * (n+1)
	res[0] = 1
	
	# 1 -> n
	for i in range(1, n+1):
			# iterate potential roots 1 -> i
			for r in range(1, i+1):
					res[i] += res[j-1] * res[i-j]
	return res[n]
