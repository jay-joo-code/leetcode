
# solution (AC)
class Solution:
    # merge sort, recursively 
    # break down linked list
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    # merge broken down linked list in order      
    def merge(self, l, r):
        if not l or not r:
            return l or r
        
        # make sure l has lower value
        if l.val > r.val:
            l, r = r, l

        # merge l and r in order
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
            
        # l and r at least one is None
        pre.next = l or r
        return head
        
