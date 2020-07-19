
# solution (AC)
class Solution:
    def pathSum(self, root, sum):
        return self.helper(root, sum, [sum])

    def helper(self, node, original_sum, targets):
        if not node: return 0
        
        hit = 0
        
        for t in targets:
            # count if sum == target
            if not t-node.val: 
                hit += 1                          
        
        # update the targets
        targets = [t-node.val for t in targets]+[original_sum]
        
        return hit+self.helper(node.left, original_sum, targets)+self.helper(node.right, original_sum, targets)
