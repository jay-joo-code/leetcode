
# attempt (AC)
class Solution:
    def sum_grandchildren(self, node):
        if not node: return 0
        total = 0
        if node.right:
            if node.right.right:
                total += node.right.right.val
            if node.right.left:
                total += node.right.left.val
        
        if node.left:
            if node.left.right:
                total += node.left.right.val
            if node.left.left:
                total += node.left.left.val
        
        return total
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root: return 0
        
        curr = 0
        if root and root.val % 2 == 0:
            curr = self.sum_grandchildren(root)
        
        return curr + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
