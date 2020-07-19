
# attempt (AC)
def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            
            if grid[row][col] == '1':
                grid[row][col] = None

                dfs(row+1, col) 
                dfs(row-1, col)  
                dfs(row, col-1) 
                dfs(row, col+1)
            return
            
        
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count