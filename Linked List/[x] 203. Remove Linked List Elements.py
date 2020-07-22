
# attempt (AC) after mistakes
# very slow
def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        
        pointer = root = ListNode(None)
        root.next = head
        
        while pointer:
            print('loop')
            while pointer.next and pointer.next.val == val:
                print('skip')
                pointer.next = pointer.next.next
                
            pointer = pointer.next

        return root.next

# solution (AC)
# faster
def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        
        while start.next:
            if start.next.val == val:
                start.next = start.next.next
                
            else:
                start = start.next   
                
        return dummy.next 