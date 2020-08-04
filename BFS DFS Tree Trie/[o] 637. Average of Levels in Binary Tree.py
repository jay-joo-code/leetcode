
# attempt (AC)
def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        
        queue = [[root, 0]]
        level = []
        cur_depth = 0
        res = []
        
        while queue:
            node, depth = queue.pop(0)
            
            if depth == cur_depth:
                level.append(node.val)
            else:
                res.append(sum(level) / len(level))
                cur_depth = depth
                level = [node.val]
            
            if node.left:
                queue.append([node.left, depth+1])
            
            if node.right:
                queue.append([node.right, depth+1])
        
        res.append(sum(level) / len(level))
        return res
