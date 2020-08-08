
# solution (AC)
def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False

# attempt (AC)
class Solution:
    def dfs(self, root, k, targets):
        if not root: return False
        
        for t in targets:
            if t == root.val:
                return True
            
        targets += [k-root.val]
        return self.dfs(root.left, k, targets) or self.dfs(root.right, k, targets)
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.dfs(root, k, [])