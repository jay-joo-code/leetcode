
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

# attempt (AC) copied solution
def pathSum(self, root, sum, target=[None]):
        if not root: return 0
        
        if target[0] is None:
            target = [sum]
        
        count = 0
        for t in target:
            if root.val == t:
                count += 1
        
        new_target = [t-root.val for t in target]+[sum]
        return count + self.pathSum(root.left, sum, new_target) + self.pathSum(root.right, sum, new_target)
