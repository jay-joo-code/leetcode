
# attempt (AC)
class Solution:
    def get_leafs(self, node, leafs):
        if not node: return
        
        if not node.right and not node.left:
            leafs.append(node.val)
            return
        
        self.get_leafs(node.left, leafs)
        self.get_leafs(node.right, leafs)
        return
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1_leafs, root2_leafs = [], []
        
        self.get_leafs(root1, root1_leafs)
        self.get_leafs(root2, root2_leafs)
        
        return root1_leafs == root2_leafs
