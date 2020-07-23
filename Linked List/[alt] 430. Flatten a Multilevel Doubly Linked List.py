
# attempt (AC)
# but very slow
class Solution:
    def last(self, node):
        if not node: return node
        if not node.next: return node
        return self.last(node.next)
    
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        
        while p:
            if p.child:
                tmp = p.next
                flattened_head = self.flatten(p.child)
                p.next = flattened_head
                flattened_head.prev = p
                flattened_tail = self.last(flattened_head)
                flattened_tail.next = tmp
                if tmp:
                    tmp.prev = flattened_tail
                p.child = None
                p = tmp
            else:
                p = p.next
        
        return head
