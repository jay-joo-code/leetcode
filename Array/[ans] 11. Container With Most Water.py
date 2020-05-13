

# attempt after looking at ans
def maxArea(self, A: List[int]) -> int:
        i, j = 0, len(A) - 1
        max_area = 0
        
        while i < j:
            max_area = max(max_area, min(A[i], A[j]) * (j - i))
            if A[i] < A[j]: i += 1
            else: j -= 1
        
        return max_area