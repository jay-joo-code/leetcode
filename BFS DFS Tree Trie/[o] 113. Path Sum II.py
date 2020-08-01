
# attempt (AC) after mistakes
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


# attempt (AC)
class Solution:
    def dfs(self, node, target, path):
        if not node: return False
        
        if not node.right and not node.left:
            path += [node.val]
            if sum(path) == target:
                return True
            return False
        
        return self.dfs(node.left, target, path+[node.val]) or self.dfs(node.right, target, path+[node.val])
    
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        return self.dfs(root, target, [])
