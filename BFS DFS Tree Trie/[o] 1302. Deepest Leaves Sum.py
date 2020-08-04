
# attempt (AC)
def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        queue = [[root, 0]]
        nodes = []
        lvl = 0
        
        while queue:
            node, curlvl = queue.pop(0)
            
            if curlvl == lvl:
                nodes.append(node)
            else:
                lvl = curlvl
                nodes = [node]
            
            if node.left:
                queue.append([node.left, curlvl+1])
            
            if node.right:
                queue.append([node.right, curlvl+1])
        
        sm = 0
        for node in nodes:
            sm += node.val
        
        return sm
