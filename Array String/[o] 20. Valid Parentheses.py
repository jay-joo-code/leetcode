
# attempt (AC)
def isValid(self, s: str) -> bool:
        open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        
        for char in s:
            if char in open_to_close:
                stack.append(open_to_close[char])
            
            if char in open_to_close.values():
                if not stack:
                    return False
                
                if char == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        
        return False
