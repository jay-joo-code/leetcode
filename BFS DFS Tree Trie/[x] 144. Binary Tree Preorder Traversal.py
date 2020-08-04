
# attempt (AC) after mistakes
def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        
        return res
