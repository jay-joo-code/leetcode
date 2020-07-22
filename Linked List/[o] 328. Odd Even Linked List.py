

# attempt (AC) on first submit
def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd = head
        first_even = even = head.next
        
        while odd and odd.next and even and even.next:
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            if even.next.next:
                even.next = even.next.next
                even = even.next
            
        odd.next = first_even
        even.next = None
        return head