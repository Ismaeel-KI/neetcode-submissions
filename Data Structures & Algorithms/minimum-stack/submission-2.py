class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
            self.stack.append(val)

        else:
            self.stack.append(val)
            val = min(val, self.min_stack[-1])
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        return self.min_stack[-1]
