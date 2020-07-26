
# attempt (AC) with couple mistakes
class Solution:
    def reverse(self, head, prev=None):
        if not head: return prev
        
        curr = head.next
        head.next = prev
        return self.reverse(curr, head)
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        
        dummy = sp = fp = ListNode(None, head)
        s = f = head
        count = 0
        
        while True:
            if count != k and not f:
                break
                
            elif count == k:
                # reverse
                fp.next = None
                self.reverse(s)
                s.next = f
                sp.next = fp
                sp = fp = s
                s = f
                count = 0
            
            else:
                f = f.next
                fp = fp.next
                count += 1
        
        return dummy.next

# solution (AC)
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next
