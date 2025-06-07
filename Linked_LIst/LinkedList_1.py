class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current  = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_pos(self, prev_node_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Given node not found.")

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index cannot be negative.")
            return
        
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        while current and count < index-1:
            current = current.next
            count +=1
        if current is None:
            print("Index out of bound")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beg(self):
        if self.head is None:
            print("List is empty.")
            return
        
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_index(self, index):
        if self.head == None:
            print("List is empty.")
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        count = 0
        while current and count < index -1:
            current = current.next
            count +=1
        
        if current is None or current.next is None:
            print("Index out of bound")
            return
        
        current.next = current.next.next

    def delete_by_value(self,value):
        if self.head == None:
            print("List is empty.")
            return
        
        current = self.head
        while current.next and current.next.data != value:
            current  = current.next
        
        if current.next is None:
            print("Value not found in the list")
            return
        
        current.next = current.next.next


    def search(self, value):
        if self.head is None:
            print("List is empty.")
            return False
        
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def search_index(self, value):
        if self.head is None:
            print("List is empty.")
            return -1
        
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index +=1
        return -1
    
    def search_value(self, index):
        if self.head is None:
            print("List is empty")
            return None
        
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count +=1
        return None
    
    def reverse_list(self):
        if self.head is None:
            print("List is empty.")
            return
        
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
        

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end ="->")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_end(30)
ll.insert_at_pos(20, 25)
print(ll.search(25))
print(ll.search_index(30))
print(ll.search_value(2))
ll.print_list()
ll.reverse_list()
ll.print_list()

