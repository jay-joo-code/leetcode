
# solution (AC)
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            if pa is None:
                pa = headB  
            else: 
                pa = pa.next
                
            if pb is None:
                pb = headA  
            else: 
                pb = pb.next

        return pa
"""
It only goes through A and B once.
Let's say:
headA = A + O
headB = B + O
where O is the repeated part.
To get to O from headA, the length is A + O + B,
to get to O from headB, the length is B + O + A
This method is simply genius.
"""