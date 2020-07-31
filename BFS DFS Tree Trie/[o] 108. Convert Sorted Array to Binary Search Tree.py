
# attempt (AC)
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        center = len(nums) // 2
        root = TreeNode(nums[center])
        root.right = self.sortedArrayToBST(nums[center+1:])
        root.left = self.sortedArrayToBST(nums[:center])
        return root
