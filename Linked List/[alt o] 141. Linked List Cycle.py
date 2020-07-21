

# attempt (AC)
def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        
        while slow and fast:
            if not slow.next or not fast.next or not fast.next.next:
                break
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

# alt solution
def hasCycle(self, head):
    fast = slow = head

    while slow and fast and fast.next:
        slow = slow.next                # Step of 1
        fast = fast.next.next           # Setp of 2

        if slow is fast:                # Checking whether two pointers meet
            return True

    return False