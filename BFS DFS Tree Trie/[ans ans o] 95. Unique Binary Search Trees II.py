
# solution (AC)
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n+1)
        
    def dfs(self, start, end):
        if start == end:
            return []
        result = []
        for i in range(start, end):
            left_perms = self.dfs(start, i) or [None]
            right_perms = self.dfs(i+1, end) or [None]
            
            for l in left_perms:
                for r in right_perms:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result

# attempt (AC)
class Solution:
    def possible_roots(self, start, end):
        if start == end: return [None]
        
        res = []
        for val in range(start, end):
            left_roots, right_roots = self.possible_roots(start, val), self.possible_roots(val+1, end)
            for left in left_roots:
                for right in right_roots:
                    root = TreeNode(val)
                    root.left, root.right = left, right
                    res.append(root)
        
        return res
    
    def generateTrees(self, n):
        if n == 0: return []
        
        return self.possible_roots(1, n+1)
