
# attempt (AC) after mistakes
# misunderstood question at first
def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        noflip = self.flipEquiv(root1.right, root2.right) and self.flipEquiv(root1.left, root2.left)
        return root1.val == root2.val and (flip or noflip)
