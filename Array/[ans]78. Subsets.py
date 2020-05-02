from typing import List

# method 1: recursion
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            output += [combination + [num] for combination in output]
        
        return output

# method 2: backtracking
# still don't really understand solution
class Solution2:
    # nums: [1, 2, 3]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            # range(0, 3): [0, 1, 2]
            # iterate over nums indexes
            for i in range(first, len(nums)):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        # range(4): [0, 1, 2, 3]
        for k in range(len(nums) + 1):
            backtrack()
        return output