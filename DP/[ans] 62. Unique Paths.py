
# solution
def uniquePaths(self, m: int, n: int) -> int:
	matrix = [[1 for i in range(m)] for j in range(n)]
	
	for x in range(1, m):
		for y in range(1, n):
			matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]
	
	return matrix[n - 1][m - 1]

