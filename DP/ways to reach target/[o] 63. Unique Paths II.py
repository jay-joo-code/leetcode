
# attempt (accepted) after 2 minor mistakes
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] != 1:
            paths[0][0] = 1
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    continue
                
                if row-1 >= 0:
                    paths[row][col] += paths[row-1][col]
                if col-1 >= 0:
                    paths[row][col] += paths[row][col-1]
                
        return paths[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
