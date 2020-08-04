
# attempt (AC)
# very slow, high space
class Solution:
    def dfs(self, node, vals):
        if not node: return
        
        vals.append(node.val)
        self.dfs(node.left, vals)
        self.dfs(node.right, vals)
    
    def add(self, node, dict):
        if not node: return None
        
        node.val = dict[node.val]
        node.left = self.add(node.left, dict)
        node.right = self.add(node.right, dict)
        return node
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        if not root.right and not root.left:
            return root
        
        vals = []
        self.dfs(root, vals)
        vals.sort(reverse=True)
        first = vals.pop(0)
        dict = {}
        dict[first] = first
        prev = first
        
        for val in vals:
            prev += val
            dict[val] = prev
            
        return self.add(root, dict)

# solution (AC)
# better
def convertBST(self, root):
        def dfs(node, val):
            # return cumu sum of this node.
            if not node:
                return val
            val = dfs(node.right,val)
            node.val += val
            return dfs(node.left, node.val)

        dfs(root,0)
        return root