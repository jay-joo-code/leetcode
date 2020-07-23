
# attempt (AC) after mistakes
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root: return [None] * k
        
        pointer = root
        length = 1
        
        while pointer.next:
            length += 1
            pointer = pointer.next
        
        part = length // k
        extra = length % k if length > k else 0
        print('extra', extra)
        res = []
        start = p = root
        
        for iter in range(1, k+1):
            if iter == k:
                res.append(start)
            
            else:
                if not p:
                    res.append(None)
                    break
                
                count = 1
                while p.next and count < part:
                    p = p.next
                    count += 1
                
                if extra > 0:
                    extra -= 1
                    p = p.next
                
                next_start = p.next
                p.next = None
                res.append(start)
                start = next_start
                p = start
        
        empty = k - len(res)
        res += [None] * empty
        return res
