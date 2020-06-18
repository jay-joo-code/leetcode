
# attempt (AC)
def kthSmallest(self, root: TreeNode, k: int) -> int:
        elts = []
        
        def traverse(root):
            if not root: return
            
            elts.append(root.val)
            traverse(root.right)
            traverse(root.left)
            return
        
        traverse(root)
        elts.sort()
        return elts[k-1]
