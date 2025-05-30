class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        popped_value = self.stack.pop()
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()
        return popped_value
    
    def peek(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

s = Stack()
s.push(10)
s.push(5)
s.push(20)
s.push(2)
print(s.get_min())
s.pop()
print(s.get_min())
    

