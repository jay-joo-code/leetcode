
# attempt (AC)
class Solution:    
    def merge(self, n1, n2):
        if not n1 or not n2:
            return n1 or n2
        
        cur = dummy = ListNode(None)
        
        while n1 and n2:
            if n1.val < n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        
        cur.next = n1 or n2
        return dummy.next
        
    def sortList(self, head):
        if not head or not head.next: return head
        slow = fast = head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        right_start = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(right_start)
        
        merged = self.merge(left, right)
        return merged

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
        
