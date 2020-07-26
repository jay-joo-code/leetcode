
# attempt (AC)
# iterative
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy = ListNode(None)
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return dummy.next

# solution: iterative (accepted)
def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
	head = cur = ListNode(0)
	
	while l1 and l2:
		if l1.val > l2.val:
			cur.next = l2
			l2 = l2.next
		else:
			cur.next = l1
			l1 = l1.next
		cur = cur.next
	cur.next = l1 or l2
	return head.next

# solution: recursive (accepted)
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	if not l1 or not l2:
		return l1 or l2
	
	if l1.val > l2.val:
		l2.next = self.mergeTwoLists(l1, l2.next)
		return l2
	else:
		l1.next = self.mergeTwoLists(l1.next, l2)
		return l1
