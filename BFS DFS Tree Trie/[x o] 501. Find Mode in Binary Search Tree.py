
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

# attempt (AC)
class Solution:
    def dfs(self, node, counter):
        if not node: return
        
        if node.val in counter:
            counter[node.val] += 1
        else:
            counter[node.val] = 1
        
        self.dfs(node.left, counter)
        self.dfs(node.right, counter)
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        counter = {}
        self.dfs(root, counter)
        mx = max(counter.values())
        return [k for k, v in counter.items() if v == mx]
