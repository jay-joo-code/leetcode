
# attempt (AC)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        
        first_higher = len(preorder)
        for i in range(len(preorder)):
            if preorder[i] > preorder[0]:
                first_higher = i
                break

        root = TreeNode(preorder[0])      
        root.left = self.bstFromPreorder(preorder[1:first_higher])
        root.right = self.bstFromPreorder(preorder[first_higher:len(preorder)])
        
        return root
