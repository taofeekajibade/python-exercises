class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_start(self):
        if self.head:
            self.head = self.head.next


linked_list = LinkedList()

# Inserting nodes at the start
linked_list.insert_at_start(3)
linked_list.insert_at_start(7)
linked_list.insert_at_start(12)

# Removing the first node
linked_list.remove_at_start()

