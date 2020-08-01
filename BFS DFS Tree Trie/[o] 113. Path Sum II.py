
# attempt (AC)
class Solution:
    def dfs(self, node, target, path, res):
        if not node: return
        
        if not node.left and not node.right:
            path += [node.val]
            if sum(path) == target:
                res.append(path)
                return
        
        self.dfs(node.left, target, path+[node.val], res)
        self.dfs(node.right, target, path+[node.val], res)
        
    
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        
        res = []
        self.dfs(root, target, [], res)
        return res
