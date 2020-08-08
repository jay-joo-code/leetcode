
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

# attempt (AC)
# very slow
class Solution:
    def find_dash(self, s, length):
        if not s: return (0, 0)
        
        res = []
        start = None
        for i in range(len(s)):
            print(start)
            if s[i] == '-':
                if start is None:
                    start = i
                    
            else:
                if not start is None:
                    l = i - start
                    # print(l)
                    if l == length:
                        res.append((start, i))
                    start = None
            
            if len(res) == 2:
                break
            
        return res
    
    def recoverFromPreorder(self, S, depth=0):
        if not S: return None
        
        first_dash_idx = len(S)
        for i in range(len(S)):
            if S[i] == '-':
                first_dash_idx = i
                break
        root = TreeNode(int(S[:first_dash_idx]))
        
        pos = self.find_dash(S, depth+1)
        # print(pos)

        if pos:
            if len(pos) == 1:
                root.left = self.recoverFromPreorder(S[pos[0][1]:], depth+1)
            
            if len(pos) == 2:
                root.left = self.recoverFromPreorder(S[pos[0][1]:pos[1][0]], depth+1)
                root.right = self.recoverFromPreorder(S[pos[1][1]:], depth+1)
        return root
