
# attempt (AC)
class BSTIterator:
    
    def traverse(self, node):
        if not node: return
        
        self.traverse(node.right)
        self.vals.append(node.val)
        self.traverse(node.left)

    def __init__(self, root: TreeNode):
        self.vals = []
        self.traverse(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.vals.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.vals) >= 1
