
# attempt (TLE)
def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        
        queue = [[root.left, 1], [root.right, 1]]
        levels = [[root]]
        mx_depth = 1
        
        while queue:
            node, depth = queue.pop(0)
            
            if len(levels) > depth:
                levels[depth].append(node)
            else:
                levels.append([node])
            
            if node:
                queue.append([node.left, depth+1])
                queue.append([node.right, depth+1])
                mx_depth = max(mx_depth, depth+1)
            else:
                if depth <= mx_depth:
                    queue.append([None, depth+1])
                    queue.append([None, depth+1])
        
        # trim None
        mx = 0
        for i in range(len(levels)):
            level = levels[i]
            start, end = None, None
            
            for j in range(len(level)):
                node = level[j]
                if node and start is None:
                    start = j
                if node:
                    end = j
            
            if not start is None:
                mx = max(mx, end-start+1)
        
        return mx


# solution (AC)
def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return []
        width, level = 0, [(root, 1)]
        # Keep going untill current level has some nodes.
        while len(level):
            # Put all children of current level in next_level.
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:   # Make sure to not put the Null nodes
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2+1))
            level = next_level
        return width