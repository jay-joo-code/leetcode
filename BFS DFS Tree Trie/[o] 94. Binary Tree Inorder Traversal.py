
# attempt (AC) after a couple mistakes
def inorderTraversal(self, root: TreeNode) -> List[int]:        
        
  def dfs(root, res):
      if not root: return res
      
      dfs(root.left, res)
      res.append(root.val)
      dfs(root.right, res)
      
      return res
  
  return dfs(root, [])
