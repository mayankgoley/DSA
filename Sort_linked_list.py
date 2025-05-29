class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_by_value(self, prev_val, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current:
            if current.data == prev_val:
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

        while current and count < index -1:
            current = current.next
            count +=1

            if current is None:
                print("Index out of bound.")
                return
        new_node.next = current.next
        current.next = new_node
    
    def print_list(self):

        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("None")

    def find_middle(self):
        if self.head is None:
            print("List is empty.")
            return
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    


    

