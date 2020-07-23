

# attempt (AC)
class Solution:
    def swap(self, left, right):
        if not left or not right:
            return left or right
    
        next = right.next
        right.next = left
        left.next = next
        return right
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = pointer = ListNode(None)
        pointer.next = head
        
        while pointer and pointer.next and pointer.next.next:
            pointer.next = self.swap(pointer.next, pointer.next.next)
            pointer = pointer.next.next
        
        return dummy.next