class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) <= 0:
            return True
        return False

    def display(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack

    def size(self):
        return self.size


stack = Stack()
# Operation results when the stack is empty
print(stack.top())
print(stack.pop())
print(stack.is_empty())

# Pushing values to stack
stack.push(5)
stack.push(8)
stack.push(1)

print('Current stack:',stack.display())
print('Value popped from stack :',stack.pop())
print('Current stack:',stack.display())
print('Value on top of stack:',stack.top())
print('Value popped from stack :',stack.pop())
print('Current stack:',stack.display())
print('Stack Empty?' ,stack.is_empty())