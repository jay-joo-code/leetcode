
# attempt (AC)
class Solution:
    def dfs(self, node, target):
        if not node: return True
        
        return node.val == target and self.dfs(node.left, target) and self.dfs(node.right, target)
    
    def isUnivalTree(self, root: TreeNode, target=None) -> bool:
        if not root: return True
        
        return self.dfs(root, root.val)
