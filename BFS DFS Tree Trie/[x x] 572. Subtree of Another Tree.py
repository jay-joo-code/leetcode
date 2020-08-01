

# solution (accepted)
# cancer code style
def isSubtree(self, s, t):
	def isMatch(s, t):
			if (s is None and t is not None) or (s is not None and t is None):
					return False
			
			if s is None and t is None:
					return True

			if s.val == t.val:
					return isMatch(s.left, t.left) and isMatch(s.right, t.right)
	
	if isMatch(s, t):
			return True
	if s is None:
			return False
	return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# attempt (AC)
# after many mistakes
class Solution:
    def dfs(self, n1, n2):
        if not n1 and not n2:
            return True
        
        if not n1 or not n2:
            return False
        
        if n1.val == n2.val:
            return self.dfs(n1.left, n2.left) and self.dfs(n1.right, n2.right)
        
        return False
    
    def isSubtree(self, s, t):
        if not s:
            return False
        
        if self.dfs(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

