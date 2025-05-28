class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def inseert_at_beg(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(self, data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_pos(self, prev_node, data):
        new_node = Node(data)
        
        if self.head is None:
            print("List is empty.")
            return
        
        current = self.head
        while current:
            if current.data == prev_node:
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
        
        current = self.head
        while current.next.next:
            curent = current.next
        current.next = None

    def delete_by_value(self, prev_node):
        if self.head is None:
            print("List is empty.")
            return
        
        if self.head == prev_node:
            self.head = self.head.next
            return
        
        current = self.head
        while current and current.next:
            if current.next.data == prev_node:
                current.next = current.next.data
                return
            current = current.next
        print("Given node not found.")

    def delete_at_index(self, index):
        if index < 0:
            print("Index out of bound.")
            return
        
        if self.head is None:
            print("List is empty.")
            return
        
        if index == 0:
            self.head ==self.head.next
            return
        
        current = self.head
        count = 0

        while current and count < index-1:
            current = current -1
            count +=1
            if current is None or current.next is None:
                print("Index out of bound.")
                return
        current.next = current.next.next

    def search(self, value):
        if self.head is None:
            print("list is empty.")
            return
        
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def reverse_list(self):
        if self.head is None:
            print("List is empty.")
            return
        
        prev= None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev =current
            current = next_node
        self.head = prev

    def search_index(self, value):
        if self.head is None:
            print("List is empty.")
            return -1
        
        current = self.head
        count = 0

        while current:
            if current.data == value:
                return count
            current = current.next
            count +=1
        return -1
    
    def search_from_nth(self, index):
        if self.head is None:
            print("List is empty.")
            return 
        
        slow = self.head
        fast = self.head

        for _ in range(index):
            if fast is None:
                print("Index out of bound.")
                return
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data
    
    def check_cycle(self):
        if self.head == None:
            print("List is empty.")
            return 
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Cycle Detected.")
                return
        print("No cycle Detected.")
    
    def palindrome_check(self):
        if self.head is None:
            print("List is empty.")
            return 
        
        # Using slow and fast to find the middle of the list

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list

        prev = None
        current = slow

        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        # Compare the first half and the second half

        first= self.head
        second = prev
        while second:
            if first.data != second.data:
                print("Not a palindrome.")
                return
            first = first.next
            second = second.next
        print("IS a Palindrome.")
    


    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end= "->")
            current = current.next
        print("None")
        
            

        

