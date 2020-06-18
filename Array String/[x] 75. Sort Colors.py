
# attempt (AC)
def sortColors(self, nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  i = 0
  
  while i < len(nums):
      if nums[i] == 2:
          nums.pop(i)
          nums.append(5)
      elif nums[i] == 0:
          nums.pop(i)
          nums.insert(0, 3)
      else:
          i += 1
  
  for j in range(len(nums)):
      if nums[j] == 3:
          nums[j] = 0
      elif nums[j] == 5:
          nums[j] = 2
