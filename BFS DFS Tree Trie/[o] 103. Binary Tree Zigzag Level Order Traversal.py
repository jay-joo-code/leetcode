
# attempt (AC) couple mistakes
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        res = []
        queue = [[root, 0]]
        
        while queue:
            node, depth = queue.pop(0)
            
            if len(res) > depth:
                if depth % 2 == 0:
                    res[depth].insert(0, node.val)
                else:
                    res[depth].append(node.val)
            else:
                res.append([node.val])
            
            if node.right:
                queue.append([node.right, depth+1])
            
            if node.left:
                queue.append([node.left, depth+1])
        
        return res
