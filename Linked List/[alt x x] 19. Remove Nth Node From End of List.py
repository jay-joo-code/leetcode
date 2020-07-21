

# attempt (accepted) after multiple mistakes
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	dummy = ListNode(None)
	dummy.next = head
	nodes = [dummy]
	
	while head:
		nodes.append(head)
		head = head.next
	nodes.append(None)
	nodes[-n-2].next = nodes[-n]
	return dummy.next

# solution 
def removeNthFromEnd(self, head, n):
	# value shifting
	def index(node):
		if not node:
			return 0
		i = index(node.next) + 1
		if i > n:
			node.next.val = node.val
		return i
	index(head)
	return head.next

# solution
def removeNthFromEnd(self, head, n):
	# n ahead
	fast = slow = head
	for _ in range(n):
		fast = fast.next
	if not fast:
		# elt removed is the first elt
		return head.next
	while fast.next:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return head
