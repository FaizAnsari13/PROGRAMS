class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to track the minimum element

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.is_empty():
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def get_min(self):
        if not self.is_empty():
            return self.min_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print("Minimum Element:", stack.get_min())
stack.pop()
print("Minimum Element:", stack.get_min())
stack.pop()
print("Minimum Element:", stack.get_min())
