
# ans (AC)
def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        return self.dfs(root.left, root.right)

  def dfs(self, l, r):
      if l and r:
          return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
      if l is None and r is None:
          return True
      return False


# attempt (AC) after couple mistakes
def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        queue = [[root, 0]]
        level = []
        cur_depth = 0
        
        while queue:
            node, depth = queue.pop(0)
            val = node.val if node else None
            
            if depth != cur_depth:
                # eval previous level
                rev = list(reversed(level))
                if rev != level:
                    return False
                
                # create new level
                cur_depth = depth
                level = [val]
            else:
                level.append(val)
            
            if node:
                queue.append([node.left, depth+1])
                queue.append([node.right, depth+1])
        
        return True
