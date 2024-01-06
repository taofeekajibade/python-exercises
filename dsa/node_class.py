#!/usr/bin/pyhon3
"""create a node class"""

class Node:
    """define the init method"""
    def __init__(self, data):
        self.head = data
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

    def pop_at_start(self):
        if self.head:
            self.head = self.head.next

linked_list = LinkedList()

linked_list.insert_at_start(15)
linked_list.insert_at_start(23)
linked_list.insert_at_start(35)

print(linked_list.pop_at_start())
print(linked_list)