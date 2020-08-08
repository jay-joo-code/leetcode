
# ans (AC)
def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def update_diameter(node):
            if not node: return 0
            
            left, right = update_diameter(node.left), update_diameter(node.right)
            self.diameter = max(self.diameter, left+right)
            return 1 + max(left, right)
        
        update_diameter(root)
        return self.diameter

# attempt (AC)
class Solution:
    def dfs(self, node):
        if not node: 
            return 0
        if not node.left and not node.right:
            return 1
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.dia = max(self.dia, left + right)
        
        return max(left, right) + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dia = 0
        self.dfs(root)
        return self.dia
