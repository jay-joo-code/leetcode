
# attempt (AC) after mistakes
class Solution:
    def right_most(self, node):
        if not node: return None
        
        if node.right:
            return self.right_most(node.right)
        else:
            return node
        
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        
        if root.val == key:
            if not root.right:
                return root.left
            
            if not root.left:
                return root.right
            
            right_most = self.right_most(root.left)
            right_most.right = root.right
            return root.left
            
        else:
            root.right = self.deleteNode(root.right, key)
            root.left = self.deleteNode(root.left, key)
            return root

# attempt (AC) after 1 mistake
class Solution:
    def right_most(self, node):
        if not node: return None
        
        if not node.right:
            return node
        
        return self.right_most(node.right)
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        
        if root.val == key:
            if not root.left or not root.right:
                return root.left or root.right
            
            right_most_node = self.right_most(root.left)
            right_most_node.right = root.right
            return root.left
        
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root