class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    if not stack.is_empty():
        temp_stack = Stack()
        while not stack.is_empty():
            temp_stack.push(stack.pop())
        reverse_stack(stack, temp_stack)
    return stack

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Original Stack:", stack.items)
reversed_stack = reverse_stack(stack)
print("Reversed Stack:", reversed_stack.items)
