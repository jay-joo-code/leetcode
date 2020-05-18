
# solution
# https://www.youtube.com/watch?v=EIf9zFqufbU
def countSubstrings(self, s: str) -> int:
	matrix = [[None] * len(s) for _ in range(len(s))]
	count = 0
	
	for i in range(len(s)):
		matrix[i][i] = 1
		count += 1
	
	for col in range(1, len(s)):
		for row in range(col):
			if abs(row-col) == 1 and s[row] == s[col]:
				matrix[row][col] = 1
				count += 1
			elif abs(row-col) > 1 and s[row] == s[col] and matrix[row+1][col-1] == 1:
				matrix[row][col] = 1
				count += 1

	return count