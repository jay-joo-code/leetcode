
# solution (AC)
class MinStack:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x: 'int') -> 'None':
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self) -> 'None':
        if len(self.data) > 1: self.data.pop()

    def top(self) -> 'int':
        return self.data[-1][0]

    def getMin(self) -> 'int':
        return self.data[-1][1]
