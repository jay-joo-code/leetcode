
# attempt (AC)
def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mx_idx = 0
        mx = nums[0]
        for i in range(len(nums)):
            if nums[i] > mx:
                mx_idx = i
                mx = nums[i]
        
        root = TreeNode(mx)
        root.left = self.constructMaximumBinaryTree(nums[:mx_idx])
        root.right = self.constructMaximumBinaryTree(nums[mx_idx+1:])
        return root
