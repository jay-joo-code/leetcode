
# attempt (AC)
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
  if not t1 and not t2:
      return None    
  
  if not t1:
      return TreeNode(t2.val, self.mergeTrees(None, t2.left), self.mergeTrees(None, t2.right))    
  
  if not t2:
      return TreeNode(t1.val, self.mergeTrees(t1.left, None), self.mergeTrees(t1.right, None))    
  
  
  return TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right))
