
# attempt (AC) slow
def singleNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = [nums[i]]
            else:
                if nums[i] in nums[i-1]:
                    nums[i-1].remove(nums[i])
                else:
                    nums[i-1].append(nums[i])
                    
                nums[i] = nums[i-1]
        
        return nums[-1][0]
