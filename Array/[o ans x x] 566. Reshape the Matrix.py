from typing import List
from collections import deque

def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    # validation
    if len(nums) * len(nums[0]) != r * c: return nums
    
    traversed = deque()
    for row in nums:
        for num in row:
            traversed.append(num)
    
    res = []
    for ri in range(r):
        res.append([])
        for ci in range(c):
            res[ri].append(traversed.popleft())
    
    return res