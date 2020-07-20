
# attempt (AC) after mistakes
def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        start, end = None, None
        
        for i in range(len(nums)):
            if nums[i] != arr[i]:
                if start is None:
                    start = i
                    
                end = i
        
        if start is None or end is None:
            return 0
        
        return end - start + 1