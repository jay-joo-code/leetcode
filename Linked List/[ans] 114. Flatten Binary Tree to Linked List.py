
# attempt (wrong)
def right_most(node):
        if node.right is None:
            return node
        
        return right_most(node.right)
        
        right_most_node = right_most(root.left)
        right_most_node.right = root.right
        root.right = None
        
        def inorder(node, current):
            if not node:
                return current
            
            current.right = node
            current.left = None
            
            current_after_left = inorder(node.left, node)
            current_after_right = inorder(node.right, current_after_left.right)
            return current_after_right
        
        inorder(root.left, root)

# solution 1 (AC)
def flatten(self, root: TreeNode) -> None:        
    '''
    1. flatten left subtree
    2. find left subtree's tail
    3. set root's left to None, root's right to root'left, tail's right to root.right
    4. flatten the original right subtree
    '''
    if not root:
        return 
    
    # flatten left child 
    self.flatten(root.left)
    
    # flatten right child
    self.flatten(root.right)
    
    # insert left child to the middle of 
    # root and right child
    tail = root.left
    if tail:
        while tail and tail.right:
            tail = tail.right
        tail.right = root.right
        root.right = root.left
        root.left = None

# solution 2 (AC)