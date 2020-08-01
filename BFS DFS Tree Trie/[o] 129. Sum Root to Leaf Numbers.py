
# attempt (AC)
def sumNumbers(self, root: TreeNode, accum=0) -> int:
        if not root: return 0
        
        if not root.right and not root.left:
            # leaf node
            return accum*10+root.val
        
        return self.sumNumbers(root.left, accum*10+root.val) + self.sumNumbers(root.right, accum*10+root.val)
