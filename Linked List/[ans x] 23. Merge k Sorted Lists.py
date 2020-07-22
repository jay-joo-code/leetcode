

# TODO: attempt using heapq or priority queue


# attempt after looking for ans (accpted)
class Solution:
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

# attempt 2 with mistakes (AC)
class Solution:
    def append_values(self, node, values):
        if not node: return
        
        values.append(node)
        self.append_values(node.next, values)
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        
        values = []
        
        for head in lists:
            self.append_values(head, values)
        
        if not values:
            return None
        
        values.sort(key=lambda head: head.val)
        
        for i in range(len(values)-1):
            values[i].next = values[i+1]
        
        return values[0]