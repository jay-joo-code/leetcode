
# attempt (accepted) after a couplue mistakes
def reorderList(self, head: ListNode) -> None:
	"""
	Do not return anything, modify head in-place instead.
	"""
	f = head
	order = []
	
	while f != None:
			order.append(f)
			f = f.next
	
	if len(order) == 0 or len(order) == 1:
			return
	
	s = 0
	f = len(order)-1
	
	while s != f:
			order[s].next = order[f]
			s += 1
			if s == f:
					break
			
			order[f].next = order[s]
			f -= 1
	
	order[s].next = None

# solution
def reorderList(self, head):
    if not head:
        return
        
    # find the mid point
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half in-place
    pre = None
		node = slow
    while node:
        pre, node.next, node = node, pre, node.next
    
    # Merge in-place; Note : the last node of "first" and "second" are the same
    first, second = head, pre
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    return 
