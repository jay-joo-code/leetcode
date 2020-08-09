
# solution (AC)
# very fast
def constructFromPrePost(self, pre, post):
        if not pre: return
        
        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]
        
        if not pre: return root
        
        # i is idx that splits post left and right
        i = post.index(pre[0])
        
        root.left = self.constructFromPrePost(pre[:i+1], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+1:], post[i+1:])
        
        return root
        