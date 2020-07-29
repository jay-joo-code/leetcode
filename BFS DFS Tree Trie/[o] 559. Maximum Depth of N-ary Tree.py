
# attempt (AC)
def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        mdepth = 0
        for child in root.children:
            mdepth = max(mdepth, self.maxDepth(child))
        
        return mdepth + 1
