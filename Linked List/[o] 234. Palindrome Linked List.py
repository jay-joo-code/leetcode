
# attempt (AC)
class Solution:
    def traverse(self, node, values):
        if not node: return
        values.append(node.val)
        self.traverse(node.next, values)
        
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        self.traverse(head, values)
        
        rev = values[::-1]
        print(values, rev)
        
        if values == rev:
            return True
        else:
            return False
