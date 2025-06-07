class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
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

    def insert_after_value(self, value, data):
        new_node = Node(data)
        
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        
        current = self.head

        while current:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next

        print("Value not found:")

    def insert_after_index(self, index, data):
        if index < 0:
            print("Index cannot be zero")
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
            count+=1

        if current is None:
            print("Index out of bound.")
            return
            
        new_node.next = current.next
        current.next = new_node
       
    def delete_from_start(self):
        if self.head is None:
            print("List is empty")
            return
        
        self.head  = self.head.next
    
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")

        current = self.head
        while current.next.next:
            current = current.next
        
        current.next = None

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            print("Value not found")
            return

        current.next = current.next.next

    def delete_by_index(self, index):
        if index < 0:
            print("Index cannot be negative")
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

    def search_element(self,value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def reverse_list(self):
        if self.head is None:
            print("List is empty")
            return
        
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev

    def palindrome(self):
        if self.head is None:
            print("List is empty.")
            return
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        
        # Compare
        first = self.head
        second = prev

        while second:
            if first.data != second.data:
                print("Not a Palindrome")
                return

            first = first.next
            second = second.next
        print("Palindrom")    

    def print_list(self):
        if self.head is None:
            print("List is empty.")
        
        current = self.head
        while current:
            print(current.data, end ='->')
            current = current.next
        print(None)

ll = Linked_list()
ll.insert_at_beg(10)
ll.insert_at_beg(20)
ll.insert_at_beg(30)
ll.insert_at_end(40)
ll.insert_after_value(30, 60)
ll.insert_after_index(2, 80)
ll.print_list()
ll.delete_from_start()
ll.delete_from_end()
ll.print_list()
ll.delete_by_index(2)
ll.delete_by_value(10)
ll.print_list()
print(ll.search_element(60))
print(ll.search_element(30))
ll.reverse_list()
ll.print_list()

lll = Linked_list()
lll.insert_at_beg(1)
lll.insert_at_end(2)
lll.insert_at_end(1)
lll.print_list()
lll.palindrome()