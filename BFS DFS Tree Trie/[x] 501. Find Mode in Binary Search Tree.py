
# attempt (AC) after mistakes
class Solution:
    def dfs(self, node, dict):
        if not node: return
        
        if node.val in dict:
            dict[node.val] += 1
        else:
            dict[node.val] = 1
        
        self.dfs(node.left, dict)
        self.dfs(node.right, dict)
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        dict = {}
        self.dfs(root, dict)
        mx = max(dict.values())
        return [k for k, v in dict.items() if v == mx]
