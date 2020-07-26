
# attempt (AC)
def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return head
        
        r1 = l1 = ListNode(None)
        r2 = l2 = ListNode(None)
        
        pointer = head
        
        while pointer:
            if pointer.val < x:
                temp = pointer.next
                l1.next = pointer
                pointer.next = None
                pointer = temp
                l1 = l1.next
            else:
                temp = pointer.next
                l2.next = pointer
                pointer.next = None
                pointer = temp
                l2 = l2.next
        
        l1.next = r2.next        
        return r1.next

# solution (AC)
def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next
