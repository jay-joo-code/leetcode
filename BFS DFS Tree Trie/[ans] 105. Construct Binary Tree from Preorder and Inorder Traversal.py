
# ans (AC)
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None

        root_idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        
        return root