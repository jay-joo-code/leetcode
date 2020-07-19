
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