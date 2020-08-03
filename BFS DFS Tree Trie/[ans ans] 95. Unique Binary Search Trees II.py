
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

