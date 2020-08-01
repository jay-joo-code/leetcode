
# attempt (AC) after many mistakes
class Solution:
    def dfs(self, root, target, path):
        if not root:
            return False
        
        if not root.right and not root.left:
            # root is leaf node
            path += [root.val]
            print(path)
            if path and target == sum(path):
                return True
            else:
                return False
        
        left, right = False, False
        
        if root.left:
            left = self.dfs(root.left, target, path[:] + [root.val])
        
        if root.right:
            right = self.dfs(root.right, target, path[:] + [root.val])
        
        return left or right 
    
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        return self.dfs(root, target, [])
