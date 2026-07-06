class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.minstack.append(val)
        else:
            prev = self.minstack[-1]
            self.minstack.append(min(val, prev))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
# 3 4 2 6 7 min 2
# 3 4 2 6 7 1 min 1 ->  push(1)
# 3 4 2 6 7 ->  min 2 pop() but how in O(1)