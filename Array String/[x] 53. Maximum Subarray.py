'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

[-2,1] < [1]

[4,-1,2] = 5 
[4,-1,2,1] = 5 + 1 = 6t

[2, -1, 3]

[-1, 3]

[[2, 1, 4],
[0, -1, 0],
[0, 0, 3]]

칸데인 알고리즘?


[-2,1,-3,4,-1,2,1,-5,4]
[-2,-1,-4,0


acc -2   0  1 -2 0 4
res MIN  -2  1 1 1


'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_nums = [0] * len(nums)
        maxsum = 0
        
        #for i in range(nums):
        #    max_nums[i] = max(max_nums[i-1] + nums[i], nums[i])
        acc = 0
        res = MIN_VALUE
        for num in nums:
        	acc += num
        	res = max(acc, res)
        	acc = max(0, acc)
                    
        return r