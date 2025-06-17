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

    def insert_at_pos(self, prev, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == prev:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Given node not found")

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index cannot be negative")
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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")


    def is_palindrome(self):
        # Find the middle of the list
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Compate the first half and second half of the list

        left = self.head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True

    
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(2)
ll.insert_at_end(1)
ll.print_list()
print(ll.is_palindrome())