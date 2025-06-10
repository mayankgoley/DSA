class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push_value(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop_data(self):
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
    
    def get_min_value(self):
        return self.min_stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size_stack(self):
        return len(self.stack)
    

s = Stack()
s.push_value(10)
s.push_value(5)
s.push_value(20)
s.push_value(2)
print(s.get_min_value())
s.pop_data()
print(s.get_min_value())


