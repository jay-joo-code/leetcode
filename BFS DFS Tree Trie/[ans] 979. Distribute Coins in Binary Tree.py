
# solution (AC)
def distributeCoins(self, root):
        def dfs(node):
            if not node: return 0, 0
            (lbal, lcnt), (rbal, rcnt) = dfs(node.left), dfs(node.right)
            bal = node.val+lbal+rbal-1
            return bal, lcnt+rcnt+abs(bal)
        return dfs(root)[1]
