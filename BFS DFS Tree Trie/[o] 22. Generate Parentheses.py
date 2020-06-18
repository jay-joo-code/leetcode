
# attempt (AC) 1 mistake though :(
def generateParenthesis(self, n: int) -> List[str]:
  res = []
  def dfs(open, close, curr):
      if open == n and close == n:
          res.append(curr)
          return

      if open == n:
          return dfs(open, close+1, curr+')')

      if open > close:
          dfs(open, close+1, curr+')')

      dfs(open+1, close, curr+'(')
      return
  dfs(0, 0, '')
  return res
