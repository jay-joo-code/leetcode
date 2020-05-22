

# TODO: attempt using heapq or priority queue


# attempt after looking for ans (accpted)
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
	values = []
	
	for list in lists:
		self.appendValues(list, values)
	
	values.sort()
	head = cur = ListNode(None)
	for value in values:
		cur.next = ListNode(value)
		cur = cur.next
	
	return head.next
		
def appendValues(self, list, values):
	if not list:
		return
	
	values.append(list.val)
	self.appendValues(list.next, values)
