
# attempt (AC) after mistake
class Solution:
    def recurse(self, node):
        if not node: return
        
        pointer = node.next
        while pointer and node.val == pointer.val:
            node.next = pointer.next
            pointer = pointer.next
        
        self.recurse(node.next)
        
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.recurse(head)
        return head
