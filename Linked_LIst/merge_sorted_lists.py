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


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end ="->")
            current = current.next
        print("None")

def merge_sorted_lists(head1, head2):
    dummy = Node(-1)
    tail = dummy

    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    
    if head1:
        tail.next = head1
    if head2:
        tail.next = head2
    
    return dummy.next

def print_sorted(head):
    current = head
    while current:
        print(current.data, end = "->")
        current = current.next
    print("None")


list1 = LinkedList()
list1.insert_at_beg(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_end(7)
list1.print_list()

list2 = LinkedList()
list2.insert_at_beg(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
list2.insert_at_end(8)
list2.print_list()

merged_lists = merge_sorted_lists(list1.head, list2.head)

print(merged_lists)
print_sorted(merged_lists)



