
# attempt (AC)
class Solution:
    def dfs(self, node, prev) -> int:
        mx = 0
        for val in prev:
            mx = max(mx, abs(val-node.val))

        left = 0
        if node.left:
            left = self.dfs(node.left, prev+[node.val])
            
        right = 0
        if node.right:
            right = self.dfs(node.right, prev+[node.val])
        return max(mx, left, right)
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.dfs(root, [root.val])
