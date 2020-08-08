
# solution (AC)
def countPairs(self, root: TreeNode, distance: int, depth=0) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l+r <= distance:
                        count += (l+r)
            
            for r in right:
                count +=
            count += sum(l + r <= distance for l in left for r in right)

            res = []
            for n in left + right:
                if n+1 < distance:
                    res.append(n+1)

            return res
        dfs(root)
        return count
