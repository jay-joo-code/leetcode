
# attempt (AC)
def levelOrder(self, root: TreeNode) -> List[List[int]]:
  if not root: return []
  
  queue = collections.deque([[root, 0]])
  res = []
  
  while queue:
      curr = queue.popleft()
      if curr[0].left:
          queue.append([curr[0].left, curr[1]+1])
      if curr[0].right:
          queue.append([curr[0].right, curr[1]+1])
      
      if len(res) == curr[1]:
          res.append([])
      
      res[curr[1]].append(curr[0].val)
  
  return res
