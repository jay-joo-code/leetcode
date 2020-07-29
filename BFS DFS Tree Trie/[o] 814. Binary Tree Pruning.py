
# attempt (AC)
def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        
        root.right = self.pruneTree(root.right)
        root.left = self.pruneTree(root.left)
        
        if root.val == 0 and not root.left and not root.right:
            return None
        
        return root