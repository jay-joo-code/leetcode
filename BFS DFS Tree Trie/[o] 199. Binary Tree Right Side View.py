
# attempt (AC)
# slow
def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        queue = [[root, 0]]
        cur_depth = 0
        levels = [[]]
        
        while queue:
            node, depth = queue.pop(0)
            
            if depth == cur_depth:
                levels[depth].append(node.val)
            else:
                cur_depth = depth
                levels.append([node.val])
            
            if node.left: queue.append([node.left, depth+1])
            if node.right: queue.append([node.right, depth+1])
        
        res = []
        for level in levels:
            res.append(level[-1])
        return res
