# attempt 1: wrong
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
	max_area = 0
	
	def area(grid, x, y):
		if y >= len(grid) or x >= len(grid[y]) or grid[y][x] == 0:
			return 0
		
		grid[y][x] = 0
		return 1 + area(grid, x - 1, y) + area(grid, x + 1, y) + area (grid, x, y - 1) + area(grid, x, y + 1)
	
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == 1:
				max_area = max(max_area, area(grid, x, y))
	
	return max_area

# solution: dfs
class Solution:
	def maxAreaOfIsland(self, grid):
		"""
        :type grid: List[List[int]]
        :rtype: int
        """
        # t: O(rc) s: O(1)
		max_area = 0
		for r in range(len(grid)):
			for c in range(len(grid[r])):
				if grid[r][c] == 1:
					max_area = max(max_area, self.explore(grid, r, c))
		return max_area
    
	def explore(self, grid, r, c):
		if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])):
			return 0
		if grid[r][c] == 0:
			return 0
		# mark as visited
		grid[r][c] = 0
		return 1 + self.explore(grid, r - 1, c) + self.explore(grid, r, c - 1) \
			+ self.explore(grid, r + 1, c) + self.explore(grid, r, c + 1) 