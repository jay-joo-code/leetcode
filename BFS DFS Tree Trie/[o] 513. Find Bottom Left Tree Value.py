
# attempt (AC)
def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        last = root.val
        
        while queue:
            node = queue.pop(0)
            if node:
                last = node.val
                queue.append(node.right)
                queue.append(node.left)
        
        return last
