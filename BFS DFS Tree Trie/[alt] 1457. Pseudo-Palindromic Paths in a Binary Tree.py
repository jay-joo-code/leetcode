
# attempt (AC)
# way too slow
class Solution:
    def dfs(self, root, path):
        if not root:
            return 0

        if not root.right and not root.left:
            # determine if path is palindromic permutation
            path += [root.val]

            i = 0
            while i < len(path):
                if i < len(path)-1 and path[i] in path[i+1:]:
                    target = path.pop(i)
                    path.remove(target)
                else:
                    i += 1
            print(path)
            if len(path) > 1:
                return 0
            else:
                return 1

        return self.dfs(root.left, path + [root.val]) + self.dfs(root.right, path + [root.val])
    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.dfs(root, [])
