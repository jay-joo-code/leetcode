
# attempt (accepted)
def minPathSum(self, grid: List[List[int]]) -> int:
        
	for row in range(len(grid)):
			for col in range(len(grid[row])):
					if row == 0:
							if col > 0:
									grid[row][col] += grid[row][col-1]
					elif col == 0:
							if row > 0:
									grid[row][col] += grid[row-1][col]
					else:
							grid[row][col] += min(grid[row][col-1], grid[row-1][col])
	
	return grid[len(grid)-1][len(grid[0])-1]

