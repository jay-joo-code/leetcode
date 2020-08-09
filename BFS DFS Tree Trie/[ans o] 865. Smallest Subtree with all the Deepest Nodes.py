
# solution (AC)
def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deep(root):
            if not root: return 0, None
            l, r = deep(root.left), deep(root.right)
            
            # if left depth > right depth: 
            # return left depth + 1, left node
            if l[0] > r[0]: return l[0] + 1, l[1]
            
            # same but for right
            elif l[0] < r[0]: return r[0] + 1, r[1]
            
            # left and right have same depth
            # return depth + 1, self
            else: return l[0] + 1, root
        return deep(root)[1]

# attempt (AC)
class Solution:
    def dfs(self, root, depth):
        if not root: return [0, None]
        
        if not root.right and not root.left:
            return [depth, root]
        
        left, right = self.dfs(root.left, depth+1), self.dfs(root.right, depth+1)
        
        if left[0] == right[0]:
            return [left[0], root]
        
        if left[0] > right[0]:
            return left
        else:
            return right
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, 0)[1]
