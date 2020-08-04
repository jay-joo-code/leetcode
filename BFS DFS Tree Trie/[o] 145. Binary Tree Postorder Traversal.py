
# attempt (AC)
def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            
        res.reverse()
        return res
