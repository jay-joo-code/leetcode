
# attempt (AC)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        values = [root.val]
        for child in root.children:
            values += self.preorder(child)
        
        return values
