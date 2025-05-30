class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top.data
        self.top = self.top.next
        return popped_node
    
    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        if self.top is None:
            return "Stack is empty"
        
        count = 0
        current = self.top
        while current:
            count +=1
            current = current.next
        return count
    
s = Stack()

s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())
print(s.size())