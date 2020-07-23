
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
