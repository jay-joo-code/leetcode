
# attempt (AC)
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        for r in range(len(matrix)):
            if matrix[r][0] > target:
                break
                
            for c in range(len(matrix[0])):
                if matrix[r][c] > target:
                    break
                
                elif matrix[r][c] == target:
                    return True
                
        return False
