class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
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

    def insert_at_index(self, index, data):
        new_node = Node(data)

        if index < 0:
            print("Index cannot be negative")
            return
        
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

    def insert_at_pos(self, prev_node, data):
        new_node = Node(data)

        current = self.head

        while current:
            if current.data == prev_node:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Given node not found.")

    def delete_from_beg(self):
        if self.head is None:
            print("List is empty.")
            return
        
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

        def print_list(self):
            current = self.head
            while current:
                print(current.data, end="->")
                current = current.next
            print("None")

    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty.")
            return
        
        if index < 0:
            print("Index cannot be negative.")
            return
        
        if index ==0:
            self.head = self.head.next
            return
        
        current = self.head
        count =0

        while current and count < index -1:
            current = current.next
            count +=1

        if current is None or current.next is None:
            print("Index out of bound.")
            return
        
        current.next = current.next.next

    def delete_at_pos(sel, prev_node):
        if self.head is None:
            print("List is empty.")
            return
        
        current = self.head
        while current.next and current.next.data !=prev_node:
            current = current.next
        
        if current.next is None:
            print("Given node not found.")
            return
        current.next = current.next.next

    def reverse_list(self):
        prev =None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def count_items(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count
    
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
    
    def find_nth_from_end(self, n):
        if self.head is None:
            print("List is empty.")
            return
        
        fast = self.head
        slow = self.head

        for _ in range(n):
            if fast is None:
                print("n is larger than the length of the list.")
                return
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data
    
    def cycle_detection(self):
        if self.head is None:
            print("List is empty.")
            return
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Cyscle detected.")
                return
        print("No cycle detected.")

        def remove_cycle(self):
            if self.head is None:
                print("List is empty.")
                return
            
            slow = self.head
            fast = self.head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    break

            else:
                print("No cycle detected.")
                return
            
            slow = self.head
            if slow == fast:
                while fast.next != slow:
                    fast = fast.next
                fast.next = None

            else:
                while slow.next !=fast.next:
                    show = slow.next
                    fast = fast.next
            fast.next = None
            print("Cycle removed.")


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")


ll = linkedlist()
ll.insert_at_beg(10)
ll.insert_at_end(20)
ll.insert_at_end(40)
ll.insert_at_pos(20, 30)
ll.print_list()
ll.cycle_detection()
print(ll.find_nth_from_end(2))
print(ll.find_middle())
ll.reverse_list()
ll.print_list()
print(ll.count_items())

                
