
# attempt (AC) after many mistakes
class Solution:
    def dfs(self, root, to_delete):
        if not root: return [None, []]
        
        left = self.dfs(root.left, to_delete)
        right = self.dfs(root.right, to_delete)
        
        root.left = left[0]
        root.right = right[0]
        
        if root.val in to_delete:
            return [None, [left[0], right[0]] + left[1] + right[1]]
        else:
            return [root, left[1] + right[1]]
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = self.dfs(root, to_delete)
        ret = [res[0]] if res[0] else []
        for node in res[1]:
            if node:
                ret += [node]

        return ret
