
# attempt (AC)
# reverse linked list method
class Solution:
    def reverse(self, node, prev=None):
        if not node: 
            return prev

        curr = node.next
        node.next = prev
        return self.reverse(curr, node)
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        r1, r2 = self.reverse(l1), self.reverse(l2)
        dummy = curr = ListNode(None)
        carry = 0
        
        while r1 or r2:
            if r1 and r2:
                sum = r1.val + r2.val + carry
                rem = sum % 10
                carry = sum // 10
                curr.next = ListNode(rem)
                r1 = r1.next
                r2 = r2.next
            
            else:
                node = r1 or r2
                sum = node.val + carry
                rem = sum % 10
                carry = sum // 10
                curr.next = ListNode(rem)
                
                if r1:
                    r1 = r1.next
                else:
                    r2 = r2.next
            curr = curr.next
        
        if carry != 0:
            curr.next = ListNode(carry)
        
        return self.reverse(dummy.next)

# solution (AC)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # turn the lists in to ints
        s1 = 0
        s2 = 0
        while l1: 
            s1 *= 10
            s1 += l1.val
            l1 = l1.next
        while l2: 
            s2 *= 10
            s2 += l2.val
            l2 = l2.next

        # take the sum and reconstruct the number from tail to head
        s3 = s1 + s2
        root = pointer = ListNode(0)
        while s3 > 0:
            new = ListNode(s3 % 10)
            new.next = pointer.next
            pointer.next = new
            s3 //= 10
        return root.next if root.next else ListNode(0)
