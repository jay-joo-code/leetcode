
# solution (AC)
def distributeCoins(self, root):
        # movement direction doesn't matter
        # if balance is +ve, coin moves upwards
        # if balance is -ve, coin moves downwards
        # movement increments by abs of balance at each node
        def dfs(node):
            if not node: return 0, 0
            (lbal, lcnt), (rbal, rcnt) = dfs(node.left), dfs(node.right)
            bal = node.val+lbal+rbal-1
            return bal, lcnt+rcnt+abs(bal)
        return dfs(root)[1]

# attempt (AC) after many mistakes
class Solution:
    def dfs(self, root):
        # returns: (balance, moves)
        if not root: return (0, 0)
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        balance = root.val-1 + left[0] + right[0]
        moves = abs(balance)+left[1]+right[1]
        
        return (balance, moves)
    
    def distributeCoins(self, root):
        return self.dfs(root)[1]
