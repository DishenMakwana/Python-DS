from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.empty():
            return 'Stack is empty'
        return self.stack.pop()

    def top(self):
        if self.empty():
            return 'Stack is empty'
        return self.stack[-1]

    def empty(self):
        if len(self.stack) <= 0:
            return True
        return False

    def display(self):
        return self.stack

    def size(self):
        return self.size


stack = Stack()
# Operation results when the stack is empty
print(stack.top())
print(stack.pop())
print(stack.empty())

# Pushing values to stack
stack.push(5)
stack.push(8)
stack.push(1)

print('Current stack:',stack.display())
print('Value popped from stack :',stack.pop())
print('Current stack:',stack.display())
print('Value on top of stack:',stack.top())
print('Current stack:',stack.display())
print(stack.empty())