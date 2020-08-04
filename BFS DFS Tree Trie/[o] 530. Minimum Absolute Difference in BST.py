
# attempt (AC)
class Solution:
    def traverse(self, node, vals):
        if not node: return
        vals.append(node.val)
        self.traverse(node.left, vals)
        self.traverse(node.right, vals)
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root: return 0
        vals = []
        self.traverse(root, vals)
        vals.sort()
        print(vals)
        mn = float('inf')
        for i in range(1, len(vals)):
            mn = min(mn, vals[i]-vals[i-1])
        return mn
