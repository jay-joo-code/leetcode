
# attempt (AC)
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        
        sm = 0
        if L <= root.val <= R:
            sm += root.val
        
        left = 0
        if root.val >= L:
            left = self.rangeSumBST(root.left, L, R)
            
        right = 0
        if root.val <= R:
            right = self.rangeSumBST(root.right, L , R)
        
        return sm + left + right
