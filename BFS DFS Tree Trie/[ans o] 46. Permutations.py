
# solution (AC)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return # backtracking
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# attempt (AC) very fast
class Solution:
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        
        for n in nums:
            new_nums = nums[:]
            new_nums.remove(n)
            self.dfs(new_nums, path+[n], res)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

