
# solution (AC)
def recoverFromPreorder(self, S):
        # need to figure out a way to achieve the line below
        # without using regex
        vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)][::-1]
        
        def fn(level):
            if not vals or level != vals[-1][0]: return None
            
            node = TreeNode(vals.pop()[1])
            node.left = fn(level+1)
            node.right = fn(level+1)
            return node
        
        return fn(0)
