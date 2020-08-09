
# attempt (AC)
def allPossibleFBT(self, N: int) -> List[TreeNode]:
        N -= 1
        
        if N == 0: return [TreeNode(0)]
        
        res = []
        
        for i in range(1, N, 2):
            left_roots = self.allPossibleFBT(i)
            right_roots = self.allPossibleFBT(N-i)
            
            for left in left_roots:
                for right in right_roots:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        
        return res

# solution (AC)
def allPossibleFBT(self, N: int) -> List[TreeNode]:
        N -= 1
        if N == 0: return [TreeNode(0)]
        res = []
        
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res += [root]
        return res

# attempt (AC) after a couple of mistakes
def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if not N: return []
        if N == 1: return [TreeNode(0)]
        if N % 2 == 0: return []
        
        res = []
        
        for l in range(1, N-1, 2):
            r = N-1-l
            left_roots = self.allPossibleFBT(l) or [None]
            right_roots = self.allPossibleFBT(r) or [None]
            for left in left_roots:
                for right in right_roots:
                    root = TreeNode(0)
                    root.left, root.right = left, right
                    res.append(root)
        
        return res