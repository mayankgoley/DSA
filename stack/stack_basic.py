# Stack implementation using a list in python
class Stack:
    def __init__(self):
        self.stack = []
    
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            return "Stack is empty"
        
    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            return "Stack is empty"
        
    def isempty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

s = Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.peek())
print(s.pop())
print(s.size())


