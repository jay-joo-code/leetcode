
# attempt (AC)
# very slow
def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = prev = ListNode(None)
        dummy.next = head
        r = l = head
        total = l.val
        
        while l:
            if total == 0:
                prev.next = r.next
                l = prev.next
                r = l
                if l:
                    total = l.val
            else:
                if r.next:
                    r = r.next
                    total += r.val
                else:
                    prev = l
                    l = l.next
                    r = l
                    if l:
                        total = l.val
        
        return dummy.next
