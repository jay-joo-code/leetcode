/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
	const res = { count: 0 }
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
			// iterate over all elts in grid
            dfs(grid, r, c, res)
        }
    }
    return res.count
};

const dfs = (grid, r, c, res, area = { count: 0 }) => {
	if (!grid[r] || !grid[r][c]) return;	// out of bounds
	
    res.count = Math.max(res.count, area.count += grid[r][c])
	
	// prevent double count by setting seen elt to 0
	grid[r][c] = 0;
	
	// recursion
    dfs(grid, r, c - 1, res, area)
    dfs(grid, r, c + 1, res, area)
    dfs(grid, r - 1, c, res, area)
    dfs(grid, r + 1, c, res, area)
};
