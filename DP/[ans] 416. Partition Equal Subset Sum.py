
# solution (accepted)
def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        def dfs(nums, index, sum, total, state):
            current = str(index) + '-' + str(sum)
            if current in state:
                return state[current]
            
            if sum * 2 == total:
                return True
            
            if sum >= total or index >= len(nums):
                return False
            
            result = dfs(nums, index + 1, sum, total, state) or dfs(nums, index+1, sum+nums[index], total, state)
            state[current] = result
            return result
        
        state = defaultdict(str)
        return dfs(nums, 0, 0, sum(nums), state)
