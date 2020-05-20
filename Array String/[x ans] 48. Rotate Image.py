from typing import List

# attempt 1: wrong
def rotate(A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A.reverse()
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j], A[j][i] = A[j][i], A[i][j]

