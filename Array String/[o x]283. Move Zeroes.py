from typing import List

# attempt 1
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    checked = 0
    i = 0
    while checked < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else: 
            i += 1
        checked += 1

nums = [0, 0, 0, 1]
moveZeroes(nums)
print(nums)