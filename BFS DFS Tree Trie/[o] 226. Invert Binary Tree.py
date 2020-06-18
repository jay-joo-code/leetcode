
# attempt (AC) very easy
def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
