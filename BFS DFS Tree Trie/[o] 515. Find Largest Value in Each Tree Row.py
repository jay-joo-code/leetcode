
# attempt (AC)
def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [[root, 0]]
        res = [root.val]
        
        while queue:
            [node, depth] = queue.pop(0)
            
            if node:
                if len(res) > depth:
                    res[depth] = max(res[depth], node.val)
                else:
                    res.append(node.val)
                queue.append([node.right, depth+1])
                queue.append([node.left, depth+1])
        
        return res
